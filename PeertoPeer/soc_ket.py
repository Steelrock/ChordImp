import socket
import sys

# Create a TCP/IP socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print "hostname:", hostname
print "IP:", IP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (IP, 12666)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Listen for incoming connections
message="ola Mestre"
sock.send(message)
print "Para sair Pressione Enter"
try:
    # Receive the data in small chunks and retransmit it
    while True:
        try: data = sock.recv(2**20)
        except: break
        print data
        if data:
            print ">>>"
            dados=raw_input()
            if len(dados) < 1:
                break
            sock.send(dados)
        else:
            print 'no more data from', self.s
            break          
finally:
    # Clean up the connection
    print "finalizando"
sock.close()

