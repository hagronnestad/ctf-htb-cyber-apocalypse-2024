import socket

IP = "83.136.254.223"
PORT = 49978

def client():
    run = True
    ready = False
    buffer = ""
    words = ""
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to the server
    client_socket.connect((IP, PORT))
    
    while run:
        data = client_socket.recv(1)

        if not data:
            continue

        character = data.decode('utf-8')
        buffer += character
        print(character, end="")

        if "Are you ready? (y/n)" in buffer:
            client_socket.send("y".encode('utf-8'))
            client_socket.send("\n".encode('utf-8'))
            print("y", end="")
            buffer = ""

        if "Ok then! Let's go!" in buffer:
            ready = True
            buffer = ""
        
        if ready and buffer.strip().startswith("GORGE") or buffer.strip().startswith("FIRE") or buffer.strip().startswith("PHREAK"):
            words = buffer.strip().split(", ")

        if "What do you do?" in buffer:
            response = ""

            for i in range(len(words)):
                if words[i] == "GORGE":
                    response += "STOP"
                if words[i] == "FIRE":
                    response += "ROLL"
                if words[i] == "PHREAK":
                    response += "DROP"
                if i < (len(words)-1):
                    response += "-"
                    
            buffer = ""
            words = ""
            print(response, end="")
            client_socket.send((response).encode('utf-8'))
            client_socket.send("\n".encode('utf-8'))            

        if "HTB" in buffer:
            run = False
            break

        if character == '\n':
            buffer = buffer.replace("\n", "")
            buffer = ""

	# Close the connection from the client side
    client_socket.close()

if __name__ == '__main__':
    client()
