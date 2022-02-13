import json
from pathlib import Path
from typing import Optional

import requests
import uvicorn
from fastapi import FastAPI, Query

from data_models import SeriesMetadata
from database import SeriesDocument

app = FastAPI()

base_url = "https://services.cancerimagingarchive.net/nbia-api/services/v1"


@app.get("/")
@app.get("/home")
def home():
    return {"message": "home"}


@app.get("/collections")
def list_collections():
    return [
        elem.get("Collection")
        for elem in requests.get(f"{base_url}/getCollectionValues").json()
        if elem.get("Collection")
        ]


@app.get("/body-parts")
def list_body_parts():
    return [
        elem.get("BodyPartExamined")
        for elem in requests.get(f"{base_url}/getBodyPartValues").json()
        if elem.get("BodyPartExamined")
        ]


@app.get("/series")
def list_series():
    with requests.get(f"{base_url}/getSeries", stream=True) as response:
        series_metadata = response.json()

    # json.dump(series_metadata, Path("streamed_series.json").open("w"))
    series = [SeriesMetadata(**entry) for entry in series_metadata]
    return repr(series[0])

    # breakpoint()
    # series_docs = [SeriesDocument(**entry.dict()) for entry in series]
    return series_metadata


@app.get("/modalities")
def list_modalities(collection: Optional[str] = None,
                    body_part: Optional[str] = Query(None, alias="body-part")):
    if collection and body_part:
        query_suffix = f"?Collection={collection}&BodyPartExamined={body_part}"
    elif collection:
        query_suffix = f"?Collection={collection}"
    elif body_part:
        query_suffix = f"?BodyPartExamined={body_part}"
    else:
        query_suffix = ""
    return [
        elem.get("Modality")
        for elem in requests.get(f"{base_url}/getModalityValues/{query_suffix}").json()
        if elem.get("Modality")
        ]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)
