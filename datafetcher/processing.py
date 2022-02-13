import json
from pathlib import Path

from data_models import SeriesMetadata
from database import SeriesDocument


series = json.load(Path("streamed_series.json").open())
for entry in series:
    series_model = SeriesMetadata(**entry)
    doc = SeriesDocument(**dict(series_model))
    doc.commit()
series_model
