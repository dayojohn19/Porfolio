
# file getting earthquake data from internet

from django.shortcuts import render
import json
import urllib.request
from django.http import JsonResponse
#using json module to load the string data into a dictionary
def printResults(data,request):
    #putting it into a Python
    theJSON = json.loads(data)
    #access the contents parse by the JSON
    #this are on the website
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number if events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " Events Recorded")
    Magnitude = 'Magnitude'
    #getting the place where it occured
    def res():
        a = []
        for i in theJSON["features"]:
            a.append((i["properties"]["place"] , i["properties"]["mag"], Magnitude))
        return a
    print("-----------\n")
    return res()

def printCount(data,request):
    #putting it into a Python
    theJSON = json.loads(data)
    #access the contents parse by the JSON
    #this are on the website
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number if events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " Events Recorded")
    Magnitude = 'Magnitude'
    #getting the place where it occured
    def res():
        a = []
        for i in theJSON["features"]:
            a.append((i["properties"]["place"],Magnitude , i["properties"]["mag"]))
        return a
    print("-----------\n")
    return count




def main(request):
    #this url list all earthquake 
    #using the free data feed from the USGS

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"

    #check if it is 200 then it is working
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        result = printResults(data,request)
        count = printCount(data,request)

    else:
        data = ("Recieved error, cannot parse results")

    return render(request, 'application/earthquake.html',{
        'data':printResults(data, request),
        "data2":data,
        'count':count
    })

# if __name__ == "__main__":
#     main()


