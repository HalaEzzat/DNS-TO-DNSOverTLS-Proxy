import socket
import threading
from dnslib import *
import ssl



# DNS server configuration
DNS_SERVER = '1.1.1.1'
DNS_PORT = 853
RECV_BUFFER_SIZE = 4096


def handle_request(client_sock, client_addr):
    try:
        data=client_sock.recv(1024)
        # Receive the DNS query from the client
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create a TLS connection to the DNS server
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations('/etc/ssl/certs/ca-certificates.crt')
        wrappedSocket = context.wrap_socket(server_sock, server_hostname=DNS_SERVER)
        wrappedSocket.connect((DNS_SERVER , DNS_PORT))
        # Send the DNS query over TLS to the server
        wrappedSocket.sendall(data)

        # Receive the response from the server over TLS
        # First receive the length of the message as a 2-byte prefix
        response_data = wrappedSocket.recv(RECV_BUFFER_SIZE)

        # Send the response back to the client
        client_sock.sendall(response_data)

    except Exception as e:
        print(f'Error handling request from {client_addr}: {e}')
    finally:
        client_sock.close()
        server_sock.close()


def main():
    # Create a server socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('0.0.0.0', 12853))
    server_sock.listen()

    print('DNS-over-TLS proxy listening on port 12853...')

    # Accept incoming client connections and spawn a thread to handle each request
    while True:
        client_sock, client_addr = server_sock.accept()
        threading.Thread(target=handle_request, args=(client_sock, client_addr)).start()


if __name__ == '__main__':
    main()
