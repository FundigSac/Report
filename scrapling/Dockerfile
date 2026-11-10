# Imagen reproducible del rastreador de competencia de FUNDIGSAC.
# Se construye desde esta carpeta (Report/scrapling), sin usar el clon local de Scrapling:
#
#   docker build -t fundig-scrapling:1.1 .
#
# Pruebas (no salen a internet):
#   docker run --rm --entrypoint python fundig-scrapling:1.1 -m pytest -q -p no:cacheprovider
#
# Rastreo de un sitio o del manifiesto, montando una carpeta de trabajo en /trabajo:
#   docker run --rm -v "<carpeta>:/trabajo" fundig-scrapling:1.1 https://ejemplo.pe /trabajo/salida/ejemplo.json \
#       --dir-cache /trabajo/cache --dir-trazas /trabajo/salida/trazas
#   docker run --rm -v "<carpeta>:/trabajo" fundig-scrapling:1.1 --manifiesto /app/sources.json \
#       --salida-dir /trabajo/salida/datos --dir-cache /trabajo/cache --dir-trazas /trabajo/salida/trazas
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt \
    && useradd --create-home --uid 10001 rastreador \
    && mkdir -p /trabajo \
    && chown rastreador:rastreador /trabajo

COPY parse.py fetch.py scrape.py export.py test_parse.py sources.json /app/
COPY fixtures /app/fixtures

USER rastreador
ENTRYPOINT ["python", "/app/scrape.py"]
CMD ["--help"]
