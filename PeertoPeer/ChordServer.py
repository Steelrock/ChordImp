# Homero Silva
from chord import *
#import function as Fcc
#import Mapa as Mp
from server.ServerP2P import ServerP2P
from server.ClientP2P import ClientP2P
from threading import Thread
import socket
import chordLibServer 
import grafico


# from domain import Node


def main():    
    ## Codifica o codigo do no    
    hostName = socket.gethostname()
    hostIpAdd = socket.gethostbyname(hostName)
    ipAdd = hostIpAdd 
    codeHash = hash(ipAdd) 
    print "Inicia e cria uma thread do servidor"
    try:
        p2pServer = ServerP2P(hostIpAdd)
        processo=Thread(target=p2pServer.run)
        processo.start()
    except: 
        print "erro ao criar thread"
        return

    print "===================================================="
    print "Server:", hostName
    print "IP:" ,hostIpAdd
    print "Porta: 12666"
    print "Objeto de Pesquisa RAISE: " + chordLibServer.tipoObjeto
    try: 
        n1 = Node(str(codeHash),ipAdd)       
    except:
        print "Erro ao criar node"
    finally:
        print "No criado, anel inicial montado !"
    print "total de Objetos no node: " + str(chordLibServer.totalObjetos)
    print "===================================================="       
    n1.join(n1)    
    attribNode(n1)    
    

    #n2.join(n1)
    #n3.join(n1) 
      
    
    #print "Finger Tables"
    #showFinger(n1)
    #showFinger(n2)
    #showFinger(n3)
    #showFinger(n4)

    # n4.leave()

    # printNodes(n1)

    # showFinger(n1)
    # showFinger(n2)
    # showFinger(n3)

    #key = 5
    #print searchData(n3,key)         
    
    #dados que deverao ser modificados no futuro.
    #address = raw_input('Enter location: ')
    #Mp.loadMap(Fcc.createMapData(address))


if __name__ == "__main__":

    main()