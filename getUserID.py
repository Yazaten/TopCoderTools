# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from collections import defaultdict
import urllib2

NAME="Yazaten"


def getID(userName):
	xml = urllib2.urlopen( 'http://api.topcoder.com/v2/users/search?handle=' + userName )
	#
	for line in xml:
		if line.find("userId")!=-1:
			return line.strip().split(" ")[1]
	return -1



userId=getID(NAME)

print userId