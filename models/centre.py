import peewee as pw
import datetime
from models.base_model import BaseModel

class Centre(BaseModel):
    name = pw.CharField()
    location = pw.CharField()