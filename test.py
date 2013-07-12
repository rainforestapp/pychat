from pydht import DHT

host, port = '192.168.0.6', 3000
dht = DHT(host, port, boot_host='192.168.0.164', 3000)

dht["test"] = "Hello world"
dht["test"]
# OUT: u'Hello world'
