from mongoengine import Document, StringField, IntField

class Countries(Document):
  name = StringField(max_length=100)
  capitale = StringField(max_length=100)
  id = IntField()