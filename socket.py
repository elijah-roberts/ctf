import socket
import base64

PORT = 4055
HOST = "challenges.neverlanctf.com"

def main():
"""
This CTF event required us to connect to a port, decode the text response, and send it back multiple times in under 10 seconds.
"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    request = f"GET / HTTP/1.1\nHost: {HOST}\n\n".encode()
    s.connect((HOST, PORT))
    questions = 0
    while questions < 10:
        result = s.recv(10000)
        print(result)
        encoded_string = result.decode("utf-8").split("\n")[-1].split(':')[-1].strip()
        print(encoded_string)
        decoded_string = base64.b64decode(encoded_string).decode("UTF-8")
        print(decoded_string)
        s.send(bytes(decoded_string, 'utf-8'))
        questions +=  1


if __name__ == '__main__':
    main()
