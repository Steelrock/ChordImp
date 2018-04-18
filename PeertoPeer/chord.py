# author: Homero Silva

import random
from server.ServerP2P import ServerP2P
from server.ClientP2P import ClientP2P
from threading import Thread
from domain import *
import urllib2
import json
# import requests 
import socket
import chordLibServer 
import cPickle

k = 600
MAX = k #2**k


def decr(value,size):
    if size <= value:
        return value - size
    else:
        return MAX-(size-value)
        

def between(value,init,end):
    if init == end:
        return True
    elif init > end :
        #shift = MAX - init
        init = 0
        #end = (end +shift)%MAX
        #value = (value + shift)%MAX
    return init < value < end

def Ebetween(value,init,end):
    if value == init:
        return True
    else:
        return between(value,init,end)

def betweenE(value,init,end):
    if value == end:
        return True
    else:
        return between(value,init,end)

def attribNode(xNode):
    chordLibServer.ServerNode = xNode
 
def returnNode():
    return chordLibServer.ServerNode 

    

class Node:
    def __init__(self,id,ipadd):
        self.id = id

        self.code = id
        self.ipAddrNode = ipadd
        self.idSuccessor = None
        self.idPredecessor = None
        self.ipAddrSuccessor = None
        self.ipAddrPredecessor = None

        self.finger = {}
        self.start = {}
        print '==== Carregado Dados do Raise ===='
        serviceurl = 'http://homol.redes.unb.br/uiot-raise/client'
        print "URL: "+serviceurl
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6ImE5OGRjOThjNTQ4MDNjYmEyYzk4ZjJhODc2MzgwOTY4OTk5MDY2ZTMifQ.e86j4gPN4h_Kv0jIAVIYf3-XgwNUcu_FSj-pRwdVXKc'
        req = urllib2.Request(serviceurl)
        req.add_header('Authorization',token)

        try: uh = urllib2.urlopen(req)
        except: uh = None
        if uh == None:
            print '==== Erro obter URL data ===='
            return 
        data = uh.read()
        #print(data)
        try: js = json.loads(data)
        except: js = None
        if str(js["code"]) == str('200'):
            cont=0
            print "Carregando ..."
            # contado na base hoje temos 1963 entradas
            for i in range(k): 
                while cont <= 10500:
                    try: 
                        if len(str(js["clients"][cont+1]["name"])) > 0  and str(js["clients"][cont]["name"]) == chordLibServer.tipoObjeto : 
                             try:
                                ipAdd = socket.gethostbyname(socket.gethostname())
                                dados=str(js["clients"][cont]["name"])+str(js["clients"][cont]["chipset"])+str(cont) + ipAdd
                                self.start[i] = str(hash(dados))
                                chordLibServer.totalObjetos = chordLibServer.totalObjetos + 1
                                # print cont,str(hash(dados))
                                cont = cont + 1
                                break
                             except: break #print "error1 on " + str(cont)
                    except: break # print "+or2 on " + str(cont) 
                    cont = cont +1

    def successor(self):
        return self.finger[0]
    
    def find_successor(self,id):  
        if betweenE(id,self.predecessor.id,self.id):
            return self
        n = self.find_predecessor(id)
        return n.successor()
    
    def find_predecessor(self,id):
        if id == self.id:
            return self.predecessor
        n1 = self
        while not betweenE(id,n1.id,n1.successor().id):
            n1 = n1.closest_preceding_finger(id)
        return n1
    
    def closest_preceding_finger(self,id):
        for i in range(k-1,-1,-1):
            if between(self.finger[i].id,self.id,id):
                return self.finger[i]
        return self
        
    
    def join(self,n1):
        chordLibServer.totalNodes = chordLibServer.totalNodes + 1
        if self == n1:
             for i in range(k):
                 self.finger[i] = self
             self.predecessor = self
        else:
            self.init_finger_table(n1)
            self.update_others()  
           # Move keys !!! 

    def remoteJoin(self,n1):
        chordLibServer.totalNodes = chordLibServer.totalNodes + 1
        self.init_finger_table(n1)
        print "update others"
        self.update_others()  

            
    def init_finger_table(self,n1):
        self.finger[0] = n1.find_successor(self.start[0])
        self.predecessor = self.successor().predecessor
        self.successor().predecessor = self
        self.predecessor.finger[0] = self
        for i in xrange(1,len(self.finger)):
            try:
                if Ebetween(self.start[i+1],self.id,self.finger[i].id):
                    self.finger[i+1] = self.finger[i]
                else :
                    self.finger[i+1] = n1.find_successor(self.start[i+1])
            except: i=len(self.finger)

    def update_others(self):
        for i in xrange(1,len(self.finger)):
            try:
                prev  = decr(self.id,2**i)
                p = self.find_predecessor(prev)
                if prev == p.successor().id:
                    p = p.successor()
                p.update_finger_table(self,i)
            except: i=len(self.finger)
            
    def update_finger_table(self,s,i):
        if Ebetween(s.id,self.id,self.finger[i].id) and self.id!=s.id:
                self.finger[i] = s
                p = self.predecessor
                p.update_finger_table(s,i)

    def update_others_leave(self):
        for i in range(k):
            prev  = decr(self.id,2**i)
            p = self.find_predecessor(prev)
            p.update_finger_table(self.successor(),i)
    # not checked 
    def leave(self):
        self.successor().predecessor = self.predecessor
        self.predecessor.setSuccessor(self.successor())
        self.update_others_leave()
        
    def setSuccessor(self,succ):
        self.finger[0] = succ
        

def hash(line):
    import sha
    key=long(sha.new(line).hexdigest(),16)
    return key
    

def printNodes():
    node = returnNode()
    strRet = "\n"
    strRet = strRet + ' Ring nodes:\n' 
    end = node
    strRet = strRet + node.id  + "\n"
    cont = 1
    while end != node.successor():
        node = node.successor()
        strRet = strRet + node.id   + "\n"
        cont = cont + 1
    strRet = strRet + '-----------'  + "\n"
    strRet = strRet + "Total Nodes: " + str(cont)  + "\n"
    strRet = strRet + '-----------'  + "\n"
    return strRet

def showFinger():
    node = returnNode()
    strRet = "\n"
    cObj=0
    strRet = strRet + 'Finger table of node ' + str(node.id) + "\n"
    strRet = strRet + 'start:node' + "\n"
    for i in range(chordLibServer.totalObjetos):
        strRet = strRet + str(node.start[i]) +' : ' +str(node.finger[i].id)  + "\n"
        cObj = cObj + 1
    strRet = strRet + "Total Objetos: " + str(cObj) + "\n"
    return strRet

def showFingerAll():
    node = returnNode()
    strRet = "\n"
    strRet = strRet + 'Ring nodes:\n' 
    end = node
    # strRet = strRet + node.id  + "\n"
    cont = 1
    while end != node.successor():
        strRet = strRet + node.id   + "\n"
        cObj=0
        i=0
        total = (len(node.finger)-1)
        strRet = strRet + 'Finger table of node ' + str(node.id) + "\n"
        strRet = strRet + 'start:node' + "\n"
        for i in range(total):
            try:
                strRet = strRet + str(node.start[i]) +' : ' +str(node.finger[i].id)  + "\n"
                cObj = cObj + 1
            except: i=total                   
        strRet = strRet + "Total Objetos: " + str(cObj) + "\n"
        cont = cont + 1
        node = node.successor()

    cObj=0
    i=0
    total = (len(node.finger)-1)
    strRet = strRet + 'Finger table of node ' + str(node.id) + "\n"
    strRet = strRet + 'start:node' + "\n"
    for i in range(total):
        try:
            strRet = strRet + str(node.start[i]) +' : ' +str(node.finger[i].id)  + "\n"
            cObj = cObj + 1
        except: i=total                   
    strRet = strRet + "Total Objetos: " + str(cObj) + "\n"
    strRet = strRet + '-----------'  + "\n"
    strRet = strRet + "Total Nodes: " + str(cont)  + "\n"
    strRet = strRet + '-----------'  + "\n"
    return strRet


def searchData(node,key):
    print "Search ....."
    print "Key: " + str(key)
    end = node
    print "Initi From Node: " + str(end.id)
    while end != node.successor():
        for i in range(k):
            if node.start[i] == key:
                # print node.start[i] == key 
                return "Found on Node:" + str(node.id)
            # print node.start[i]
        node = node.successor()
        # print "while: " + str(node.id) +" " + str(end.id)
    for i in range(k):
        if node.start[i] == key:
            return "Found on Node:" + str(node.id)
        # print node.start[i]        
    return "Not Found"

def printStatus():
    strRet = "** Status do Node **\n"
    strRet = strRet + "-------------------\n"
    strRet = strRet + "Total Nodes: " + str(chordLibServer.totalNodes) + "\n"
    strRet = strRet + "Total Objetos: " + str(chordLibServer.totalObjetos) + "\n"
    strRet = strRet + "Total Requisicoes: " + str(chordLibServer.totalRequisicoes) + "\n"
    strRet = strRet + "-------------------\n"
    return strRet

def initJoin(strDados):
    ip = strDados[9:]
    n2 = returnNode()
    strSerie = cPickle.dumps(n2,-1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = (ip, 12666)
    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    sock.send(strSerie)
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            try: 
                data = sock.recv(chordLibServer.sizeObject)
                sdata = cPickle.loads(data)
                n2=CH.returnNode()
                localnode=n2
                n2 = sdata
                n2.remoteJoin(localnode)
                break
            except: 
                print "erro de initjoin"
                break

    finally:
        # Clean up the connection
        print "finalizado initjoin"
    sock.close()
    # return strSerie





