"""
GSC Insights — Extrae datos de Google Search Console
Uso: python gsc_query.py --url "https://example.com/..." --days 90
     python gsc_query.py --days 90   (dominio completo)

Credenciales: lee GOOGLE_APPLICATION_CREDENTIALS del entorno (.env del proyecto).
Sitio GSC:    lee GSC_SITE del entorno, o lo deriva del dominio de la URL.
"""
import argparse, json, os, sys
from datetime import datetime, timedelta
from pathlib import Path

# Cargar variables de entorno desde un archivo .env si está disponible.
# Búsqueda agnóstica: usa la ruta indicada en SEO_DOTENV si existe, o busca
# automáticamente un .env subiendo desde el directorio de trabajo actual.
try:
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(os.environ.get("SEO_DOTENV") or find_dotenv(usecwd=True))
except ImportError:
    pass

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

def _get_credentials():
    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path:
        raise RuntimeError(
            "Define la variable de entorno GOOGLE_APPLICATION_CREDENTIALS con la "
            "ruta al archivo JSON de la cuenta de servicio de Google Cloud."
        )
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"No se encontró el archivo de credenciales: {creds_path}")
    return service_account.Credentials.from_service_account_file(creds_path, scopes=SCOPES)

def _get_site_url(page_url: str | None) -> str:
    """Deriva sc-domain:<dominio> a partir de la URL, o usa GSC_SITE del entorno."""
    site = os.environ.get("GSC_SITE")
    if site:
        return site
    if page_url:
        from urllib.parse import urlparse
        domain = urlparse(page_url).netloc
        return f"sc-domain:{domain}"
    raise ValueError("Pasa --url o define GSC_SITE en el entorno.")

def get_gsc_data(page_url=None, days=90, row_limit=500):
    creds = _get_credentials()
    site_url = _get_site_url(page_url)
    service = build("searchconsole", "v1", credentials=creds)

    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=days)

    request_body = {
        "startDate": str(start_date),
        "endDate": str(end_date),
        "dimensions": ["query"],
        "rowLimit": row_limit,
        "startRow": 0,
    }

    if page_url:
        request_body["dimensionFilterGroups"] = [{
            "filters": [{
                "dimension": "page",
                "operator": "equals",
                "expression": page_url
            }]
        }]

    response = service.searchanalytics().query(siteUrl=site_url, body=request_body).execute()

    rows = response.get("rows", [])
    results = []
    for row in rows:
        results.append({
            "query": row["keys"][0],
            "clicks": row.get("clicks", 0),
            "impressions": row.get("impressions", 0),
            "ctr": round(row.get("ctr", 0) * 100, 2),
            "position": round(row.get("position", 0), 1)
        })

    return {
        "site": site_url,
        "page_filter": page_url or "domain-wide",
        "period_days": days,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "total_rows": len(results),
        "rows": results
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL específica a filtrar", default=None)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--limit", type=int, default=500)
    args = parser.parse_args()

    data = get_gsc_data(page_url=args.url, days=args.days, row_limit=args.limit)
    print(json.dumps(data, ensure_ascii=False, indent=2))
