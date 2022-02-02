from pydantic import BaseModel, Field


class SeriesMetadata(BaseModel):
    series_instance_uid: str = Field(None, alias="SeriesInstanceUID")
    study_instance_uid: str = Field(None, alias="StudyInstanceUID")
    modality: str = Field(None, alias="Modality")
    series_date: str = Field(None, alias="SeriesDate")
    series_description: str = Field(None, alias="SeriesDescription")
    body_part_examined: str = Field(None, alias="BodyPartExamined")
    series_number: str = Field(None, alias="SeriesNumber")
    collection: str = Field(None, alias="Collection")
    patient_id: str = Field(None, alias="PatientID")
    manufacturer: str = Field(None, alias="Manufacturer")
    manufacturer_model_name: str = Field(None, alias="ManufacturerModelName")
    software_versions: str = Field(None, alias="SoftwareVersions")
    image_count: str = Field(None, alias="ImageCount")
    timestamp: str = Field(None, alias="TimeStamp")
