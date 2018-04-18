import matplotlib
matplotlib.use("Agg")
import sys,os,string,threading
from time import sleep
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import random

class geraGrafico(object):

    def geraMelhorCaminho():
	    g=nx.Graph()
	    _file = open("prouter.dll","r")
	    for lin in _file:
		    ipo = lin.split("|")[0].rstrip()
		    ipd = lin.split("|")[1].rstrip()
		    pso = lin.split("|")[2].rstrip()
		    if pso == "0":
			    g.add_edge(str(ipo),str(ipd),peso=int(pso))
	    _file.close()

	    for rl in rota_ativa:
		    ipo = rl.split("|")[0].rstrip()
		    ipd = rl.split("|")[1].rstrip()
		    pso = rl.split("|")[2].rstrip()
		    g.add_edge(str(ipo),str(ipd),peso=int(pso))

	    try:
		    print("Tem Rota? ",nx.has_path(g,"192.168.1.1","192.168.2.1"))
		    _custo = nx.dijkstra_path_length(g,"192.168.1.1","192.168.2.1","peso")
		    addCusto(_custo)
		    melhorCaminho = nx.shortest_path(g,"192.168.1.1","192.168.2.1","peso")
	    except nx.NetworkXException as eee:
		    print(eee)
	    #Remove outras rotas do grafo
	    g.clear()
	    k=0
	    kmax = len(melhorCaminho)-1
	    for _remo in melhorCaminho:
		    g.add_edge(melhorCaminho[k],melhorCaminho[k+1])
		    k+=1
		    if (k+1 == len(melhorCaminho)):
			    break

	    print(melhorCaminho)

	    pos=nx.spring_layout(g)
	    color_map = [(random(),random(),random()) for i in range(1)]
	    nx.draw_networkx(g,pos,nodelist=["192.168.2.1"],node_size=1000,font_size=6)
	    nx.draw_networkx(g,pos,nodelist=["192.168.1.1"],node_size=1000,font_size=6)
	    nx.draw(g,pos,node_color = color_map,node_size=100,with_labels=False,font_size=6)
	    plt.savefig("./app/static/grafo.png",dpi=150)
	    print("Caminho Gerado")
	    return melhorCaminho