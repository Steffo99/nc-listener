import socket

# Crea un socket
server = socket.socket()
# Assegnagli la porta 23 e l'indirizzo "principale" del computer
server.bind((socket.gethostname(), 23))
# Accetta massimo 1 connessione alla volta
server.listen(1)

while True:
    print("Awaiting message.")
    # Accetta una connessione rispondendo al SYN
    (client, address) = server.accept()
    # Manda dati
    client.send(b"Complimenti! Hai scoperto un segreto. Invia il tuo telegram username e vediamo chi altri lo scopre!\n")
    # Richiedi dati con una window size di 1024
    client.recv(1024)
    recv_bytes = client.recv(1024)
    # Converti i byte ricevuti in una stringa
    recv_string = str(recv_bytes)
    # Rispondi al messaggio
    client.send(b"Addio.\n")
    # Chiudi la connessione con il client mandando un FIN e richiedendo l'invio di un FIN da parte del client
    client.close()
    # Salva la stringa ricevuta su file
    file = open("solved.txt", "a+")
    file.write(recv_string + "\n")
    file.close()

