// Restauración aislada en PGlite (Postgres en memoria): descifra, carga y calcula métricas agregadas.
import fs from "node:fs"; import crypto from "node:crypto"; import { PGlite } from "@electric-sql/pglite";
const [file, keyFile] = process.argv.slice(2);
const raw = fs.readFileSync(file); const key = Buffer.from(fs.readFileSync(keyFile, "utf8"), "base64");
const d = crypto.createDecipheriv("aes-256-gcm", key, raw.subarray(0, 12)); d.setAuthTag(raw.subarray(12, 28));
const plain = Buffer.concat([d.update(raw.subarray(28)), d.final()]);
const { data, fotos } = JSON.parse(plain);
const db = new PGlite();
await db.exec(`create table productos(codigo text primary key, empresa text, producto text, talla text, genero text, stock_inicial int, updated_at timestamptz, activo boolean);
create table entradas(id bigint primary key, codigo text, cantidad int, anulado boolean);
create table salidas(id bigint primary key, codigo text, cantidad int, anulado boolean);
create table personal(id bigint primary key, trabajador text);`);
for (const p of data.productos) await db.query("insert into productos values($1,$2,$3,$4,$5,$6,$7,$8)", [p.codigo, p.empresa, p.producto, p.talla, p.genero, p.stock_inicial, p.updated_at, p.activo]);
for (const t of ["entradas", "salidas"]) for (const r of data[t]) await db.query(`insert into ${t} values($1,$2,$3,$4)`, [r.id, r.codigo, r.cantidad, r.anulado]);
for (const r of data.personal) await db.query("insert into personal values($1,$2)", [r.id, r.trabajador]);
const q = async (s) => (await db.query(s)).rows[0];
const out = {
  productos: (await q("select count(*)::int n from productos")).n,
  personal: (await q("select count(*)::int n from personal")).n,
  entradas: (await q("select count(*)::int n, sum(cantidad) filter (where not anulado)::int vivas from entradas")),
  salidas: (await q("select count(*)::int n, sum(cantidad) filter (where not anulado)::int vivas from salidas")),
  queda_total: (await q(`select sum(p.stock_inicial + coalesce(e.s,0) - coalesce(s.s,0))::int t from productos p
     left join (select codigo, sum(cantidad) s from entradas where not anulado group by 1) e using (codigo)
     left join (select codigo, sum(cantidad) s from salidas where not anulado group by 1) s using (codigo)`)).t,
  huella_saldos: (await q(`select md5(string_agg(p.codigo || ':' || (p.stock_inicial + coalesce(e.s,0) - coalesce(s.s,0)), ',' order by p.codigo)) h from productos p
     left join (select codigo, sum(cantidad) s from entradas where not anulado group by 1) e using (codigo)
     left join (select codigo, sum(cantidad) s from salidas where not anulado group by 1) s using (codigo)`)).h,
  fotos: Object.keys(fotos).length,
  fotos_integras: Object.values(fotos).filter(f => crypto.createHash("sha256").update(Buffer.from(f.b64, "base64")).digest("hex") === f.sha256).length,
};
console.log(JSON.stringify(out));
