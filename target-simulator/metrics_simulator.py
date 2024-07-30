from prometheus_client import start_http_server, Gauge, Counter
import random
import time

# Definir as métricas
# Métricas gerais
api_status = Gauge('api_status', 'Status of the API', ['api_name'])
broker_status = Gauge('broker_status', 'Status of the message broker', ['broker_name'])
bus_status = Gauge('bus_status', 'Status of the bus', ['bus_name'])
database_status = Gauge('database_status', 'Status of the database', ['database_name'])
microservice_status = Gauge('microservice_status', 'Status of the microservice', ['service_name'])
pod_status = Gauge('pod_status', 'Status of the pod', ['pod_name'])

# Métricas adicionais para o Message Broker
broker_queue_size = Gauge('broker_queue_size', 'Number of messages in the broker queue', ['queue_name'])
broker_dlq_size = Gauge('broker_dlq_size', 'Number of messages in the broker DLQ', ['queue_name'])

# Métricas adicionais para o Pod
pod_mem_usage = Gauge('pod_mem_usage', 'Pod % mem usage', ['pod_name'])
pod_cpu_usage = Gauge('pod_cpu_usage', 'Pod % CPU usage', ['pod_name'])


# Função para simular métricas
def generate_metrics():
    while True:
        # Simular status (0: down, 1: up)
        api_status.labels('api_1').set(random.choices([0, 1], [1, 4])[0])
        broker_status.labels('broker_1').set(random.choices([0, 1], [1, 4])[0])
        bus_status.labels('bus_1').set(random.choices([0, 1], [1, 1])[0])
        database_status.labels('database_1').set(random.choices([0, 1], [1, 4])[0])
        pod_status.labels('pod_1').set(random.choices([0, 1], [1, 4])[0])
        microservice_status.labels('service_1').set(random.choices([0, 1], [1, 4])[0])
        microservice_status.labels('service_2').set(random.choices([0, 1], [1, 4])[0])

        # Simular tamanho das filas do Message Broker
        broker_queue_size.labels('main_queue').set(random.randint(0, 100))
        broker_dlq_size.labels('dlq_queue').set(random.randint(0, 100))

        # Simular consumo de recursos do Pod
        pod_mem_usage.labels('pod_1').set(random.randint(0, 100))
        pod_cpu_usage.labels('pod_1').set(random.randint(0, 100))

        time.sleep(5)


if __name__ == '__main__':
    # Iniciar o servidor HTTP na porta 8000
    start_http_server(8000)
    generate_metrics()
