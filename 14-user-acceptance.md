# 14 · Aceptación del responsable

Pruebas que solo puede hacer el responsable, porque usan su correo, su teléfono o datos reales. Marcar cada una con fecha y resultado.

## Admin — https://fundigsac-admin.vercel.app

| # | Paso | Resultado esperado | OK / fecha |
| --- | --- | --- | --- |
| A1 | Entrar con el Gmail de administrador temporal y el código que llega al correo | Abre «Para hoy». Una línea fina se dibuja bajo la barra superior solo la primera vez | |
| A2 | Cambiar tema e idioma desde la barra superior | Cambian al instante; en el teléfono siguen en Ajustes | |
| A3 | Ajustes → Altura de las filas → Compacta → Guardar | Las tablas de Cuentas muestran filas más bajas (solo en computadora) | |
| A4 | Cuentas → Invitar personal con un correo de la empresa y el rol que corresponda | La persona recibe la invitación cuando el dominio esté verificado en Resend | |
| A5 | Cuando llegue la primera hoja real del Libro de Reclamaciones: asignarla, responderla | El estado pasa a Respondida; el consumidor recibe la respuesta por correo (requiere dominio verificado) | |

## Sitio — https://fundigsac-web.vercel.app

| # | Paso | Resultado esperado | OK / fecha |
| --- | --- | --- | --- |
| W1 | Abrir la portada en una ventana privada | Una tubería con válvula se dibuja bajo la cabecera en 1,5 s y desaparece; los botones funcionan desde el inicio | |
| W2 | Enviar una cotización real (o una de prueba marcada «PRUEBA», que luego se cancela desde el Admin con ese motivo) | Pantalla de confirmación con folio COT-2026-…; aparece en Admin → Solicitudes | |
| W3 | Libro de Reclamaciones | Solo con un reclamo real. No registrar hojas de prueba: el correlativo es legal y no debe tener huecos | |

## Stock — https://fundigsac-stock-dashboard.vercel.app

| # | Paso | Resultado esperado | OK / fecha |
| --- | --- | --- | --- |
| S1 | Abrir la app instalada; si aparece «Hay una versión nueva», tocar Actualizar | Carga la versión del 10/11 | |
| S2 | Celular: Más → Resumen | Se ve el Resumen con «Ver gráfico de 30 días» | |
| S3 | Computadora: Trabajadores | Tabla con Área, Unidades recibidas y Última entrega | |
| S4 | Registrar una entrega real como de costumbre | Se guarda igual que antes; una línea azul cruza bajo la banda al abrir la app | |

## Pendientes del responsable

1. Verificar el dominio `fundigsac.com` en Resend (registros DNS) y avisar para cambiar el remitente y las bandejas a direcciones de la empresa.
2. Migrar Resend a la cuenta de la empresa y reemplazar `RESEND_API_KEY` en Vercel (`fundigsac-admin`, Preview y Production).
3. Exportar los favoritos de Chrome (`.html`) si se quiere ampliar la investigación de diseño.
