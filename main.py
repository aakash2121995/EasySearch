import json
import urllib

location = raw_input("Enter the location: ")

url = 'http://maps.googleapis.com/maps/api/geocode/json?'


url = url + urllib.urlencode({'senson':'false','address':location})

print "Retrieving " + url

fileData = urllib.urlopen(url).read()

print "Retrieved " + str(len(fileData)) + " Characters"

dObj = json.loads(str(fileData))

#print json.dumps(dObj,indent=4)

latitude = dObj["results"][0]["geometry"]["location"]["lat"]
longitude = dObj["results"][0]["geometry"]["location"]["lng"]

print "Latitude : %f Longitude: %f" % (latitude,longitude)

location = dObj['results'][0]['formatted_address']

print location