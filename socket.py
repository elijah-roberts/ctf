import socket
import base64
import time

PORT = 4055
HOST = "challenges.neverlanctf.com"
SECONDS = 10

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time_end = time.time() + SECONDS
    while time.time() < time_end:
        result = s.recv(10000)
        print(result)
        encoded_string = result.decode("utf-8").split("\n")[-1].split(':')[-1].strip()
        print(encoded_string)
        decoded_string = base64.b64decode(encoded_string).decode("UTF-8")
        print(decoded_string)
        s.send(bytes(decoded_string, 'utf-8'))
    


if __name__ == '__main__':
    main()
