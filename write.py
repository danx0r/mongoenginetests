from mongoengine import *
from classes import *

connect("metest")

Test.drop_collection()
Test2.drop_collection()

t = Test(stringy = "this is a Test")
t.save()
t1 = Test1(stringz="this is a Test1")
t2 = Test2(ref1=t, ref2=t, emb=t1)
t2.save()

for i in Test2.objects:
    print i.id, i.ref1.stringy, i.ref2.stringy, i.emb.stringz
