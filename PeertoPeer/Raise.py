#import requests 
import json
import urllib

# serviceurl = 'https://raise.homol.uiot.org/uiot-raise/client/list/?tokenId=b0206dfff802a20cdb7d5f535c3d071a'


def main():

    serviceurl = 'http://homol.redes.unb.br/uiot-raise/client'
    url = serviceurl #+ urllib.urlencode({'tokenId':'false'})
    print "Retrieving", url
    __aa = urllib.request.Request(url)
    __aa = urllib.request.Request.add_header('Authorization','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6ImRmNjhjNDkxZmVmODQ5ZmVjZmU3NzU3MzIwNjJlYzVlMWIyN2U0NDAifQ.6PbgTABZlk36Bl_x9mMDzEf8Wd8JYdFcrdrgNHgJlXM')
    uh = urllib.urlopen(__aa)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    return 

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        return 

    print json.dumps(js, indent=4)
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    dados=str(lat)+","+str(lng)
    urldata = 'https://maps.google.com/?q=' + dados 
    # + ',' +lng
    return urldata

if __name__ == '__main__':
    main()
