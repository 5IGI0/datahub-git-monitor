import os

DATAHUB_API_BASE=os.getenv("DATAHUB_API_BASE", default="http://127.0.0.1:8000/api/v1/") # do not forget to put / at the end
DATAHUB_API_KEY=os.getenv("DATAHUB_API_KEY") # not implemented server-side