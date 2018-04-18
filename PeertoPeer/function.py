import urllib
import json
import requests 
import urllib
from chord import *


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def createMapData(local):
    address = local #raw_input('Enter location: ')
    if len(address) < 1 : return 

    url = serviceurl + urllib.urlencode({'sensor':'false', 
            'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        return 

    # print json.dumps(js, indent=4)
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    dados=str(lat)+","+str(lng)
    urldata = 'https://maps.google.com/?q=' + dados 
    # + ',' +lng
    return urldata

def getRaiseData(self,xNo):
    
    serviceurl = 'http://homol.redes.unb.br/uiot-raise/client/list/?tokenId=a006106aadaee517669627ff737ee281'
    url = serviceurl 
    # print 'Retrieving', url

    try: uh = urllib.urlopen(url)
    except: uh = None
    if uh == None:
        print '==== Erro obter URL data ===='
        return 

    # uh = urllib.urlopen(url)
    # print uh.getcode
    data = uh.read()
    # print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    # print("The response contains {0} properties".format(len(js)))
    # print "Code: " + str(js["values"][1]["name"])
    if str(js["code"]) == str('200'):
        print '==== Loading ===='
        cont=0
        # contado na base hoje temos 1963 entradas
        xNo.start = {}
        xNo.finger = {}
        while cont <= 535:
            #try: 
            if len(str(js["values"][cont+1]["name"])) > 0  and str(js["values"][cont]["name"]) == "ASUS_Z00T":
                # try:
                    ipAdd = "10.125.8.75"
                    dados=str(js["values"][cont]["name"])+str(js["values"][cont]["chipset"])+str(cont) + ipAdd
                    xNo.start[cont] = dados
                    print cont,dados
                    """
                    ipAdd = "10.125.8.75"
                    dados=str(js["values"][cont]["name"])+str(js["values"][cont]["chipset"])+str(cont) + ipAdd
                    codeHash = hash(dados)
                    xnode = Node(str(codeHash),ipAdd)
                    xnode.ipAddrNode = ipAdd   
                    xnode.code = codeHash
                    x1 = Node(str(codeHash),ipAdd)
                    print cont
                    xNo.join(xnode)
                    print "depois"
                    
                    print "------- Dados objeto: " + str(cont)
                    print str(js["values"][cont]["name"])
                    print str(js["values"][cont]["chipset"])
                    print str(js["values"][cont]["mac"])
                    print str(js["values"][cont]["serial"])
                    print str(js["values"][cont]["processor"])
                    print str(js["values"][cont]["channel"])
                    print str(js["values"][cont]["deviceId"])
                    print "---------------"
                    """
                #except: print "error1 on " + str(cont)
                #finally: print "ok"
            #except: print "error2 on " + str(cont) 
            cont = cont +1

    

