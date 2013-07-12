import Pyro4

#uri=raw_input("What is the Pyro uri of the greeting object? ").strip()
name=raw_input("What is your name? ").strip()

Pyro4.config.HMAC_KEY = 'Nikhil'
#room=Pyro4.Proxy("PYRONAME:room")          # get a Pyro proxy to the greeting object
room=Pyro4.Proxy("PYRO:obj_6f81576f462c4ff1bdd6e4bedc2a880f@192.168.0.164:60389`")
room.add_me(name)   # call method normally
remote_uuid = room.add_me('remote')
print "Users are ", room.get_users()
room.push_msg("Hello")
room.push_msg("World")
print "Broadcast Messages are: ", room.get_msg()
print room.send_msg_to_user('remote', 'Hi there')
print remote_uuid
print room.get_my_msg('remote', remote_uuid)
