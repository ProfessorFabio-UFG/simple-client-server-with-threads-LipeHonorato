from socket  import *
from constCS import * #-
import threading
import time
from random import *

def request(valor1, valor2, op, delay=0):
    time.sleep(delay) # simulação do tempo de espera
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # connect to server (block until accepted)

    calculo = f"{valor1} {valor2} {op}"
    s.send(calculo.encode())
    data = s.recv(1024)
    print(f"[Resultado] {calculo} = {data.decode()}")
    s.close()

if __name__ == "__main__":
    inicio = time.time()

    threads = []

    operacoes = [
        (3, 3, 'div'),
        (20, 4, 'sub'),
        (7, 7, 'sum'), 
    ]

    for i, (v1, v2, op)  in enumerate(operacoes):
        sleep_time = randint(0,10)
        t = threading.Thread(target=request, args=(v1, v2, op, sleep_time))
        print(f"[Thread] {i} está inativa por {sleep_time}s")
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    fim = time.time()
    print(f"Tempo total com threads no cliente: {fim - inicio:.2f} segundos")