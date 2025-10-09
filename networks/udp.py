# UDP Server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM = UDP
server.bind(("127.0.0.1", 5500))

print("UDP server listening...")
while True:
    data, addr = server.recvfrom(1024)
    print("Received:", data.decode(), "from", addr)
    server.sendto(b"Hello UDP Client!", addr)


# we dont have to worry about buffers, file descriptors, looping, accepting 