from mongoengine import *
from classes import *

connect("metest")

for i in Test2.objects:
    print i.id, i.ref1.stringy, i.ref2.stringy, i.emb.stringz
