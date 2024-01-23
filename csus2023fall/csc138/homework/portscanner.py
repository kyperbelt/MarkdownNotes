
import sys
import socket


# Scan a single socket and get the service name
def scan(hostname, protocol, sockt, port):
        try:
            sock = socket.socket(socket.AF_INET, sockt)
            sock.connect((hostname, port))
            service = socket.getservbyport(port, protocol.lower())
            print(f"port {port} open: {service}")
            sock.close()
        except socket.error:
            print(f"port {port} closed")


def get_socket_type(protocol):
    # return the socket type depending on the protocol
    if protocol == "TCP":
        return socket.SOCK_STREAM
    elif protocol == "UDP":
        return socket.SOCK_DGRAM
    else: 
        # invalid socket so return None
        return None


def start():
    # Check that argument count is valid
    if len(sys.argv) != 5:
        print("usage: python3 portscan.py <hostname> <protocol> <portlow> <porthigh>")
        sys.exit(1)

    hostname = sys.argv[1]
    protocol = sys.argv[2].upper()
    portlow = int(sys.argv[3])
    porthigh = int(sys.argv[4])

    sockt = get_socket_type(protocol)
    if sockt == None: 
        # we want to exit if the protocol is not udp or tcp
        print(f"invalid {protocol}. Specify 'udp' or 'tcp")
        sys.exit(1)


    # Loop through ports and attempt to connect
    print(f"scanning host={hostname}, protocol={protocol}, ports: {portlow} -> {porthigh}")
    for port in range(portlow, porthigh+1):
        scan(hostname, protocol, sockt, port)


if __name__ == "__main__":
    start()
