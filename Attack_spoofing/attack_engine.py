import socket

# Create a socket object
attack_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get local machine name
attack_socket.bind(('10.196.100.64', 4800))

# Receive no more than 1024 bytes

print('listening for messages...')

while True:
    data, addr = attack_socket.recvfrom(1024)
    print(addr)
    print('Received from %s: %s' % (addr, data))
