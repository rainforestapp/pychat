import Pyro4
import uuid
import hashlib

class Room(object):
    users = {}
    inbox = {}
    msg = []

    def add_me(self, name):
        if not self.users.has_key(name):
            user_uuid = uuid.uuid1()
            self.users[name] = user_uuid
            return user_uuid
        else:
            return "User already exists!"

    def log_off(self, name, uuid):
        if self.users.has_key(name):
            if self.users[name] == uuid:
                self.users.pop(name)
            else:
                return "Supplied uuid does not match!"
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

    def get_my_msg(self, name, uuid):
        if self.users.has_key(name):
            if str(self.users[name]) == str(uuid):
                return self.inbox[name]
            else:
                return "Supplied uuid does not match!"

room = Room()

Pyro4.config.HMAC_KEY = 'Nikhil'
daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(room)             # register the greeting object as a Pyro object
ns.register("room", uri)  # register the object with a name in the name server

print "Ready. Object uri =", uri      # print the uri so we can use it in the client later
daemon.requestLoop() 
