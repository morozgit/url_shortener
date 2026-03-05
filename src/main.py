from fastapi import FastAPI
import uvicorn
from api.link_api import router as router_link

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

app = FastAPI(title="URL Shortener")

app.include_router(router_link)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)