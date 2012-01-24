from mongoengine import *

class Test(Document):
    stringy = StringField(required=True)

class Test1(EmbeddedDocument):
    stringz = StringField(required=True)

class Test2(Document):
    ref1 = ReferenceField(Test)
    ref2 = ReferenceField(Test)
    emb = EmbeddedDocumentField(Test1)

