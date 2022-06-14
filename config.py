import yaml


with open('config.yaml') as f:
    config = yaml.load(f, yaml.FullLoader)

Modules = config['Modules']
Message_Host = config['RabbitMQ']['Host']
Message_Queue = config['RabbitMQ']['Queue']
Message_Key = config['RabbitMQ']['Routing_key']
