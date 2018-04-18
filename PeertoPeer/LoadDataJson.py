import requests 
import json
import urllib

serviceurl = 'http://homol.redes.unb.br/uiot-raise/client/list/?tokenId=a006106aadaee517669627ff737ee281'

def main():

    url = serviceurl 
    print 'Retrieving', url

    try: uh = urllib.urlopen(url)
    except: uh = None
    if uh == None:
        print '==== Erro obter URL data ===='
        return 

    # uh = urllib.urlopen(url)
    # print uh.getcode
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    #try: js = json.dumps(data)
    except: js = None
    print("The response contains {0} properties".format(len(js)))
    print "Code: " + str(js["values"][1]["name"])
    if str(js["code"]) == str('200'):
        print '==== Loading ===='
        cont=0
        # contado na base hoje temos 1963 entradas
        while cont <= 1995:
            try: 
                if len(str(js["values"][cont+1]["name"])) > 0: # and str(js["values"][cont]["name"]) == "Bia":
                    try:
                        print "------- Dados objeto: " + str(cont)
                        print str(js["values"][cont]["name"])
                        print str(js["values"][cont]["chipset"])
                        print str(js["values"][cont]["mac"])
                        print str(js["values"][cont]["serial"])
                        print str(js["values"][cont]["processor"])
                        print str(js["values"][cont]["channel"])
                        # print str(js["values"][cont]["deviceId"])
                        print "---------------"
                    except: print "error1 on " + str(cont)
            except: print "error2 on " + str(cont) 
            cont = cont +1

    

if __name__ == '__main__':
    main()
