from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    #Kümmert sich um eingehende Clients
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s ist verbunden." % client_address)
        client.send(bytes("Namen eingeben und ENTER druecken!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Hi %s! Wenn du den Chatroom verlassen möchtest, gibe "{quit}" in den Chat ein.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s ist beigetreten!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s hat sich verpisst." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix ist für die Identifizierung
    #sendet eine Nachricht an alle Clients

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Wartet auf Clients...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
