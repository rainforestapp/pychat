import Pyro4

class Room(object):
    users = []

    inbox = {}

    msg = []

    def add_me(self, name):
        if name not in self.users:
            self.users.append(name)
            return "Hello, {0}. Added.\n".format(name)
        else:
            return "User already exists!"

    def log_off(self, name):
        if name in self.users:
            self.users.remove(name)
        return "Logged off"

    def get_users(self):
        return self.users

    def push_msg(self, msg):
        self.msg.append(msg)
        return msg

    def get_msg(self):
        return ' '.join(self.msg)

    def send_msg_to_user(self, user, msg):
        if user in self.users:
            if not self.inbox.has_key(user):
                self.inbox[user] = []
            self.inbox[user].append(msg)
        return "Sent"

    def get_my_msg(self, name):
        return self.inbox[name]

room = Room()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(room)             # register the greeting object as a Pyro object
ns.register("room", uri)  # register the object with a name in the name server

print "Ready. Object uri =", uri      # print the uri so we can use it in the client later
daemon.requestLoop() 
