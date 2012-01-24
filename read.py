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

for i in Test2.objects:
    print i.id, i.ref1.stringy, i.ref2.stringy, i.emb.stringz
