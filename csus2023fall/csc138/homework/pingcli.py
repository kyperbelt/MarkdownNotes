import sys
import socket
import time
from socket import AF_INET, SOCK_DGRAM
from socket import timeout


def create_client(svr_ip, svr_port):

    # number of packets sent
    sent = 0

    # number of packets recieved
    received = 0

    RTT_list = []


    for i in range(1, 11):  # loop


        # create udp socket with a one second timeout
        clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(1)

        start = time.time()

        # message that we are sending to server
        try:
            # We increment number of packets sent
            sent += 1
            clientSocket.sendto(f"{i}".encode(), (svr_ip, svr_port))

            # we increment the number of packets recieved 
            message, serverAddress = clientSocket.recvfrom(2048)
            received += 1
            end = time.time()
            elapsed_time = (end - start) * 1000
            print("%s%s %s"%(message.decode() , str(serverAddress), "(RTT: %.3fs ms)" % elapsed_time ))


            RTT_list.append(elapsed_time)

        except timeout:
            # we timed out for ping packet response
            print("Request timed out for sequence %d" % i)

        clientSocket.close()

    # sort the list to get it from min to max
    RTT_list.sort()

    # calculate the recieved rate percentage
    received_rate = (received / sent) * 100

    # print out stats
    print("\nPing Statistics: \nSent = %s, Received = %s, Lost Rate = %s%%\n"%(sent, received, (100 - received_rate)))

    print("Minimum RTT = %.3f ms, Maximum RTT = %.3f ms, Average RTT = %.3f ms\n"%(RTT_list[0], RTT_list[-1],round(sum(RTT_list)/len(RTT_list), 5)))


def main():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    svr_ip = sys.argv[1]
    svr_port = int(sys.argv[2])
    create_client(svr_ip, svr_port)


if __name__ == "__main__":
    main()
