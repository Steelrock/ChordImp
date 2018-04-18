import urllib2
import urllib
import json

def main():

    serviceurl = 'http://homol.redes.unb.br/uiot-raise/client'
    url = serviceurl
    print "Retrieving", url

    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6IjdlZWY2ZDYwMTFlMzg1MDdhZjg0OGQ3NjIyMWFiMWQyYjQ1YTBjNzQifQ.LHcMJCCX6aTh-Xt9d4jjvyoyTmhnj3A7_Jvm8ZSNa5I'
    req = urllib2.Request(url)
    req.add_header('Authorization',token)
    uh = urllib2.urlopen(req)
    data = uh.read()
    js = json.loads(data)
    print len(js)
    # kk = json.loads(data)
    cont=10
    print js["code"]
    dados=str(js["clients"][cont]["name"])+str(js["clients"][cont]["chipset"])
    print dados

    
if __name__ == '__main__':
    main()
