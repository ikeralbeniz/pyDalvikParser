import sys
sys.path.insert(0, '../src')

######################################################

from pyDalvickParser import *
apk = AndroidApp('./samples/Chess.apk')

if apk.isvalidAPK == True:
	print "Is a valid APK\n"
	print "List of methods:"
	for method in apk.dex.methods.methods:
		print "\t%s %s" % (method["class"], method["name"])
else:
	print "Is not a valid APK"
