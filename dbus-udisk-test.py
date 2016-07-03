import dbus
from dbus.mainloop.glib import DBusGMainLoop

from gi.repository import GObject

def property_changed(device):
    print 'Property changed for %s' % (device)


#must be done before connecting to DBus
DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()

bus.add_signal_receiver(property_changed,
                        signal_name = "PropertyChanged")

obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/drives/TSSTcorp_CDDVDW_SE_S084C_SATASLIM00003008cae')
iface = dbus.Interface(obj, 'org.freedesktop.DBus.Properties') # Here we use this 'magic' interface

iface.connect_to_signal('PropertyChanged', property_changed)

#start the main loop
mainloop = GObject.MainLoop()
mainloop.run()
