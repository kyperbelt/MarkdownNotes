import sys
import socket
from socket import AF_INET, SOCK_DGRAM


clientPackets = {}


def create_server(port):
    
    # create and bind server to listen at given port
    serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', port))
    


    print("UDP Ping Server is listening on port :", port)
            
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)

        print("%s %s"% ("Recieved PING from", clientAddress))
        print("Send PONG to " + str(clientAddress))
        serverSocket.sendto("Recieved PONG from ".encode(), clientAddress)

        address, _ = clientAddress
        if (_check_loss(address, int(message.decode()))):
            print(f"Packet from {clientAddress} was lost.")


def _check_loss(address, value)->bool:
    loss = False
    if (not (address in clientPackets) or (value < clientPackets[address][-1]) ):
        clientPackets[address] = [0]
    if (value > clientPackets[address][-1] + 1):
        loss = True
    clientPackets[address].append(value)
    clientPackets[address].sort()
    return loss


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 pingsvr.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    create_server(port)

if __name__ == "__main__":
    main()
