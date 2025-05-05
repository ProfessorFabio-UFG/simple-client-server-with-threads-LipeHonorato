from socket  import *
from constCS import * #-
import threading
from time import *
from random import *
from multiprocessing import Process

operacoes = [
    (3, 3, 'div'),
    (20, 4, 'sub'),
    (7, 7, 'sum'), 
]

tempototal = 0

for i, (v1, v2, op)  in enumerate(operacoes):
    print("===============================")
    sleep_time = randint(0,10) # tempo de espera simulado
    sleep(sleep_time) # simulando espera
    print(f"{i} Está inativo por {sleep_time}s")
    tempototal += sleep_time # soma dos segundos de espera no total

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # connect to server (block until accepted)

    calculo = f"{v1} {v2} {op}"
    s.send(calculo.encode())
    data = s.recv(1024)

    print(f"Resultado: {calculo} = {data.decode()}")
    s.close()
print("===============================")

print(f"Tempo total sem threads no cliente: {tempototal:.2f} segundos")