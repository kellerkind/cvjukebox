import dbus
bus = dbus.SystemBus()
obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
iface = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
for d in iface.GetManagedObjects():
  print d
