import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("172.28.242.141",16011))
    s.sendall(b"Hello")
    data=s.recv(1024)
    print("Received:",repr(data))