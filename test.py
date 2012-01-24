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

t = Test(stringy = "this is a Test")
t.save()
t1 = Test1(stringz="this is a Test1")
t2 = Test2(ref1=t, ref2=t, emb=t1)
t2.save()
