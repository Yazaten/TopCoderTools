# -*- coding: utf-8 -*-

#from collections import defaultdict
import urllib2
import json
import sys
import time

API_URL = 'http://api.topcoder.com/v2/data/srm/statistics/tops'
#?rankType=Competitors&pageIndex=1&pageSize='

def requestBody( ind ):
	time.sleep(1)
	url = API_URL \
		+ '?rankType=Competitors&pageIndex=' \
		+ str(ind) \
		+ '&pageSize=100'
	try:
		res = urllib2.urlopen(url).read();
		return res;
	except urllib2.HTTPError as e:
#		print 'The server couldn\'t fulfill the request.'
#		print 'Error code: ', e.code
		return None
	except urllib2.URLError as e:
#		print 'We failed to reach a server.'
#		print 'Reason: ', e.reason
		return None


def appendCompetitorData( body, competitorList ):
	dicted_json = json.loads( body )

	for competitor in dicted_json["data"]:
		competitorList.append( competitor["rating"] )


def getRatingList():
	competitorRatingList=[]
	ind = 1
	while True:
		body = requestBody( ind )
		if body is None : break

		appendCompetitorData( body, competitorRatingList )

		ind+=1

	return competitorRatingList


rateList = getRatingList()

for elm in rateList:
	print elm
