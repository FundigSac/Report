# Imagen del rastreador de datos públicos para el estudio de competencia de FUNDIGSAC.
#
# Se construye desde la raíz del proyecto ("Sitio web") con dos contextos: esta carpeta y el clon local de Scrapling.
#
#   docker build -t fundig-scrapling --build-context scrapling=Scrapling -f Report/competencia/scripts/Dockerfile Report/competencia/scripts
#
# Uso, montando la carpeta donde se guardará el JSON:
#
#   docker run --rm -v "<carpeta>:/salida" fundig-scrapling https://ejemplo.pe /salida/ejemplo.json
#
# El extra [fetchers] instala paquetes de Python únicamente. Esta imagen no descarga navegadores
# y el rastreador usa solo el Fetcher HTTP simple.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

# Solo se copia lo necesario para instalar el paquete; se excluyen .git, documentación y pruebas.
COPY --from=scrapling pyproject.toml README.md LICENSE MANIFEST.in setup.cfg /opt/Scrapling/
COPY --from=scrapling scrapling /opt/Scrapling/scrapling

RUN pip install "/opt/Scrapling[fetchers]" \
    && useradd --create-home --uid 10001 rastreador \
    && mkdir -p /salida \
    && chown rastreador:rastreador /salida

COPY scrape.py /app/scrape.py

USER rastreador
WORKDIR /app

ENTRYPOINT ["python", "/app/scrape.py"]
CMD ["--help"]
