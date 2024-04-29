import socket
import threading
import time
import json
    
if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 40999))
    
    # Vytvoření slovníku s hodnotami pro volání
    # method a id jsou příklady příkazů z API
    call_values = {'jsonrpc': '2.0', 'method': 'GetSystemTime', 'id': 'GetSystemTime'}

    # Převod slovníku na řetězec JSON
    json_string = json.dumps(call_values)

    # Převod řetězce JSON na bajty
    bytes_to_send = json_string.encode('utf-8')

    # Odeslání bajtů přes socket
    client_socket.send(bytes_to_send)
    response = client_socket.recv(4096)  # Přečte až 4096 bajtů (můžete upravit podle potřeby)

    # Převod bajtů na řetězec
    response_string = response.decode('utf-8')

    # Vypsání odpovědi
    print("Response from server:", response_string)
    