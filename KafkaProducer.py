from confluent_kafka import Producer
import time
# Создаем конфигурацию продюсера
conf = {'bootstrap.servers': 'localhost:9093'}

# Создаем продюсера
p = Producer(conf)

# Отправляем сообщение
while True:
    p.produce('123', key='key', value='value')
    time.sleep(0.005)
    timestamp = time.time()
    print(timestamp)
# Ожидаем завершения отправки всех сообщений
p.flush()