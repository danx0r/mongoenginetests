from mongoengine import *
from classes import *

connect("metest")

for i in Test2.objects:
    print i.id, i.ref1.stringy, i.ref2.stringy, i.emb.stringz

o = Test2.objects(emb__stringz = "Test1_2")
for i in o:
    print i.id, i.ref1.stringy, i.ref2.stringy, i.emb.stringz
