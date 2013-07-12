import Pyro4
Pyro4.config.HMAC_KEY = 'Nikhil'
nameserver = Pyro4.locateNS(host='192.168.0.6', port=9090)
nameserver.list()
uri = nameserver.lookup('room')
proxy = Pyro4.Proxy(uri)
proxy.get_users()
proxy.add_me("Russ")
proxy.get_msg()

