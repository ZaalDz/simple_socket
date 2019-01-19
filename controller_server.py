import socket
from threading import Thread
from util import send_message, receive_message

HOST = ''
PORT = 5555


def accepting_connection(my_socket: socket.socket) -> socket.socket:
    print('Trying to accept connection')
    connection, address = my_socket.accept()
    print('Connection established')
    return connection


def threaded_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.bind(('0.0.0.0', PORT))
        my_socket.listen(0)
        connection = accepting_connection(my_socket)
        with connection as conn:
            while True:
                user_input = input()
                if len(user_input) > 0:
                    send_message(conn, user_input)
                    response = receive_message(conn)
                    print(response)


if __name__ == '__main__':
    Thread(target=threaded_client).start()
