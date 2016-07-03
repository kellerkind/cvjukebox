from pydbus import SystemBus
from gi.repository import GObject

def print_state(a, b, c):
    print a
    print b.keys()
    print c

bus = SystemBus()
dev = bus.get('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/drives/TSSTcorp_CDDVDW_SE_S084C_SATASLIM00003008cae')

dev.PropertiesChanged.connect(print_state)
GObject.MainLoop().run()
