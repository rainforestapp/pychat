from pydht import DHT
host1, port1 = "localhost", 3000
dht1 = DHT(host1, port1)
host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, boot_host=host1, port1)
# OUT:   File "<input>", line 1
# OUT: SyntaxError: non-keyword arg after keyword arg
dht2 = DHT(host2, port2, boot_host=host1, boot_port=port1)
dht1["test"] = "Hello world"
dht2["test"]
# OUT: u'Hello world'
