from mongoengine import *
connect("metest")

class Test(Document):
    stringy = StringField(required=True)

class Test1(EmbeddedDocument):
    stringz = StringField(required=True)

class Test2(Document):
    ref1 = ReferenceField(Test)
    ref2 = ReferenceField(Test)
    emb = EmbeddedDocumentField(Test1)

test = Test(stringy = "this is a Test")
test.save()
