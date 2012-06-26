import sys
sys.path.insert(0, '../src')

######################################################

from pyDalvickParser import *
dex = Dalvik.fromfilename('./samples/classes.dex')

print "List of methods:"
for method in dex.methods.methods:
	print "\t%s %s" % (method["class"], method["name"])
