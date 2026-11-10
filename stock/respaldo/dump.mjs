// Respaldo lógico de Stock: lee con la clave pública (igual que la app), guarda JSON + fotos, todo cifrado.
import fs from "node:fs"; import path from "node:path"; import crypto from "node:crypto";
import { createClient } from "@supabase/supabase-js";
const [envFile, outDir, keyFile] = process.argv.slice(2);
const env = Object.fromEntries(fs.readFileSync(envFile, "utf8").split(/\r?\n/).filter(l => l.includes("=")).map(l => [l.slice(0, l.indexOf("=")), l.slice(l.indexOf("=") + 1).trim()]));
const sb = createClient(env.VITE_SUPABASE_URL, env.VITE_SUPABASE_ANON_KEY, { auth: { persistSession: false } });
const TABLES = ["productos", "personal", "entradas", "salidas", "pedidos", "ajustes", "editores", "ia_uso"];
const data = {}; const report = {};
for (const t of TABLES) {
  const rows = []; let from = 0;
  for (;;) { const { data: d, error } = await sb.from(t).select("*").range(from, from + 999); if (error) { report[t] = "ERROR " + error.code; break; } rows.push(...d); if (d.length < 1000) break; from += 1000; }
  data[t] = rows; if (!report[t]) report[t] = rows.length;
}
const files = fs.readFileSync("names.txt","utf8").trim().split("|"); let fotoErr = 0; let fotoBytes = 0; const fotos = {};
for (const p of files) { const r = await fetch(`${env.VITE_SUPABASE_URL}/storage/v1/object/public/evidencias/${p}`); if (!r.ok) { fotoErr++; continue; } const buf = Buffer.from(await r.arrayBuffer()); fotoBytes += buf.length; fotos[p] = { sha256: crypto.createHash("sha256").update(buf).digest("hex"), b64: buf.toString("base64") }; }
report.fotos = files.length; report.fotosDescargadas = Object.keys(fotos).length; report.fotosError = fotoErr; report.fotosBytes = fotoBytes;
const plain = Buffer.from(JSON.stringify({ creado: new Date().toISOString(), proyecto: "vdxhhuzivzbtbiahjork", data, fotos }));
const key = crypto.randomBytes(32); const iv = crypto.randomBytes(12);
const c = crypto.createCipheriv("aes-256-gcm", key, iv); const enc = Buffer.concat([c.update(plain), c.final()]);
fs.mkdirSync(outDir, { recursive: true });
const name = `stock-${new Date().toISOString().slice(0, 10)}.json.enc`;
fs.writeFileSync(path.join(outDir, name), Buffer.concat([iv, c.getAuthTag(), enc]));
fs.writeFileSync(keyFile, key.toString("base64"));
report.archivo = name; report.sha256Plano = crypto.createHash("sha256").update(plain).digest("hex"); report.bytesCifrados = enc.length + 28;
console.log(JSON.stringify(report));
