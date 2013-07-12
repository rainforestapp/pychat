from pydht import DHT
import time

dht = DHT('192.168.0.164', 3000, boot_host='192.168.0.6', boot_port=3000)

print dht['test']
