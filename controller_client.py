import socket
import time
from util import send_message, receive_message

HOST = '192.168.122.1'
PORT = 5555


def start_dialog(conn):
    while True:
        recv = receive_message(conn)
        send_message(conn, recv)
        if not recv:
            print('Connection broke')
            break


def connect_to_server(my_socket: socket.socket, host: str, port: int):
    try:
        my_socket.connect((host, port))
        print('Connection established')
        return True
    except socket.error as e:
        print(e)
        time.sleep(1)
        return False


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            is_connected = connect_to_server(conn, HOST, PORT)
            if is_connected:
                start_dialog(conn)


if __name__ == '__main__':
    main()
