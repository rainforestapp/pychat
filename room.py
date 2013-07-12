import Pyro4

class Room(object):
    users = []

    msg = []

    def add_me(self, name):
        self.users.append(name)
        return "Hello, {0}. Added.\n".format(name)

    def get_users(self):
        return self.users

    def push_msg(self, msg):
        self.msg.append(msg)
        return msg

    def get_msg(self):
        return ' '.join(self.msg)

room = Room()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(room)             # register the greeting object as a Pyro object
ns.register("room", uri)  # register the object with a name in the name server

print "Ready. Object uri =", uri      # print the uri so we can use it in the client later
daemon.requestLoop() 
