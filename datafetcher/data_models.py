from pydantic import BaseModel, Field


class SeriesMetadata(BaseModel):
    series_instance_uid: str = Field("___", alias="SeriesInstanceUID")
    study_instance_uid: str = Field("___", alias="StudyInstanceUID")
    modality: str = Field("___", alias="Modality")
    series_date: str = Field("___", alias="SeriesDate")
    series_description: str = Field("___", alias="SeriesDescription")
    body_part_examined: str = Field("___", alias="BodyPartExamined")
    series_number: str = Field("___", alias="SeriesNumber")
    collection: str = Field("___", alias="Collection")
    patient_id: str = Field("___", alias="PatientID")
    manufacturer: str = Field("___", alias="Manufacturer")
    manufacturer_model_name: str = Field("___", alias="ManufacturerModelName")
    software_versions: str = Field("___", alias="SoftwareVersions")
    image_count: str = Field("___", alias="ImageCount")
    timestamp: str = Field("___", alias="TimeStamp")
