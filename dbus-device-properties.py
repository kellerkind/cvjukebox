import dbus
bus = dbus.SystemBus()
obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/drives/TSSTcorp_CDDVDW_SE_S084C_SATASLIM00003008cae')
iface = dbus.Interface(obj, 'org.freedesktop.DBus.Properties') # Here we use this 'magic' interface
for i in iface.GetAll('org.freedesktop.UDisks2.Drive'):
    print i

print iface.Get('org.freedesktop.UDisks2.Drive', 'MediaChangeDetected')
