import calendar
import datetime
import requests
import json
import urllib
from iso8601 import parse_date
from apixu_client import ApixuClient
from apixu_exception import ApixuException

def iso2unix(timestamp):
    # use iso8601.parse_date to convert the timestamp into a datetime object.
    parsed = parse_date(timestamp)
    # now grab a time tuple that we can feed mktime
    timetuple = parsed.timetuple()
    # return a unix timestamp
    return calendar.timegm(timetuple)

def main():
    api_key = 'eb2a0633229b456ba6093557151106' #current api key borrowed from the C# functionality on github
    client = ApixuClient(api_key) #api function instatiated to enable use of api functions
    current = client.getCurrentWeather(q='nairobi') #current weather data in Nairobi
    timestamp = datetime.datetime.now().isoformat('T') #converting date time now to iso 8601 format
    unix = iso2unix(timestamp) #converting current 'timestamp' to unix timestamp
    usum = sum(map(int, str(unix))) #sum of digits in the unix timestamp
    devname = "Eleazar Yewa Harold" #name of developer doing this code
    #passing data above to json format below 'postdata'
    postdata = {
        "name": devname,
        "timestamp": str(timestamp),
        "unix": str(unix),
        "sum": str(usum),
        "temperature_celsius": str(current['current']['temp_c']),
        "humidity": str(current['current']['humidity'])
    }

    urlpost = "https://hooks.zapier.com/hooks/catch/1604383/mw5sh8/" #passing posting url
    post = requests.post(urlpost, data=postdata) #function to post json data on the url above
    print(post.content) #return message of the posting

if __name__ == '__main__': main()