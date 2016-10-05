import socket

server = socket.socket()
server.bind((socket.gethostname(), 23))
server.listen(1)

while True:
    print("Awaiting message.")
    (client, address) = server.accept()
    client.send(b"Complimenti! Hai scoperto un segreto. Invia il tuo telegram username e vediamo chi altri lo scopre!\n")
    client.recv(1024) # Ignora i dati di connessione iniziali
    recv_bytes = client.recv(1024)
    recv_string = str(recv_bytes)
    client.send(b"Addio.\n")
    client.close()
    file = open("solved.txt", "r+")
    file.write(file.read() + recv_string + "\n")
    file.close()

