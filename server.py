from pydht import DHT

host, port = '192.168.0.164', 3000
dht = DHT(host, port, boot_host=host1, port1)
