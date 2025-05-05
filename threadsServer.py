from socket  import *
from constCS import * #-
import threading

def connect_client(con, addr):

    print(f"[Thread] cliente: {addr}")

    while True:               
        data = conn.recv(1024)   # receive data from client
        if not data: break       # stop if client stopped

        #decodifica os dados
        calculo = bytes.decode(data)

        #separa os valores que tem um espaço entre si em um vetor
        valores = calculo.split(" ")

        #pegar os valores da conta
        valor1 = int(valores[0])
        valor2 = int(valores[1])
        op = valores[2] # operacao sum, sub, div

        # checando a operacao correta
        if (op == 'sum'):
            res = valor1 + valor2
        elif (op == 'sub'):
            res = valor1 - valor2
        elif (op == 'div'):
            if (valor2 == 0):
                res = 'error division by zero'
            else:
                res = valor1/valor2
        else:
            res = 'error'

        
        conn.send(str.encode(str(res))) # return sent data


    conn.close()               # close the connection
    print(f"[Thread] Conexão finalizada com {addr}")

print("[Servidor] Esperando conexão...")

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

while True:
    conn, addr = s.accept()
    threading.Thread(target=connect_client, args=(conn, addr)).start()