# Descrição do Sistema

## Aplicação Servidor (server.py)
Inicialmente o servidor está esperando conexões do cliente em loop. Após a conexão, o servidor recebe o cálculo da aplicação cliente, separa os valores e a operação em um vetor, verifica qual é a operação escolhida e calcula o resultado. Em seguida o resultado é enviado para a aplicação cliente e a conexão é encerrada.

## Aplicação Cliente com threads (threadsClient.py)
O processo cliente envia para o servidor 3 requisições com uma operação matemática em cada requisição. Para simular um tempo de espera, cada thread possui um tempo de espera aleatório de 0 a 10 segundos, no qual fica inativa, ao finalizar o tempo de espera a requisição é enviada para o servidor.

## Aplicação Cliente sem threads (noThreadsClient.py)
O processo cliente envia para o servidor 3 requisições com uma operação matemática em cada requisição. Para simular um tempo de espera, cada requisição que vai ser enviada possui um tempo de espera aleatório de 0 a 10 segundos, durante esse tempo o processo fica inativo, ao finalizar o tempo de espera a requisição é enviada para o servidor.

## Comparação do tempo de execução

**a) Threads no servidor**
Com threads apenas no servidor as requisições só são enviadas após a anterior ter finalizado, portanto o tempo de espera é maior, já que cada requisição tem que esperar a anterior, como há um tempo aleatório de 10s de espera, no pior caso todas as requisições serão finalizadas em 30 segundos.

**b) Thread no cliente e servidor**
Com threads no servidor e no cliente, as requisições são enviadas simultaneamente, nenhuma requisição precisa esperar outra, apenas o seu tempo de espera e como há um tempo aleatório de 10s de espera, no pior caso todas as requisições serão finalizadas em 10 segundos, portanto muito mais rápido.
