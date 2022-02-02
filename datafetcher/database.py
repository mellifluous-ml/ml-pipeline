from pymongo import MongoClient
from umongo import Document, fields, validate
from umongo.frameworks import PyMongoInstance


db = MongoClient().test
instance = PyMongoInstance(db)


@instance.register
class SeriesDocument(Document):
    series_instance_uid = fields.StringField(required=True)
    study_instance_uid = fields.StringField(required=True)
    modality = fields.StringField(required=True)
    series_date = fields.StringField(required=True)
    series_description = fields.StringField(required=True)
    body_part_examined = fields.StringField(required=True)
    series_number = fields.StringField(required=True)
    collection = fields.StringField(required=True)
    patient_id = fields.StringField(required=True)
    manufacturer = fields.StringField(required=True)
    manufacturer_model_name = fields.StringField(required=True)
    software_versions = fields.StringField(required=True)
    image_count = fields.StringField(required=True)
    timestamp = fields.StringField(required=True)

    class Meta:
        collection_name = "image_series"


SeriesDocument.ensure_indexes()

#
# Series(
#     collection="dummy_collection",
#     body_part="dummy_body_part",
#     modality="dummy_modality",
#     ).commit()
