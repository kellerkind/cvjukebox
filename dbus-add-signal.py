#!/usr/bin/env python

import dbus      # for dbus communication (obviously)
import gobject   # main loop
from dbus.mainloop.glib import DBusGMainLoop # integration into the main loop

def handle_resume_callback():
    print "System just resumed from hibernate or suspend"

def handle_suspend_callback():
    print "System about to hibernate or suspend"

DBusGMainLoop(set_as_default=True) # integrate into main loob
bus = dbus.SystemBus()             # connect to dbus system wide
bus.add_signal_receiver(           # defince the signal to listen to
    handle_resume_callback,            # name of callback function
    'Resuming',                        # singal name
    'org.freedesktop.UPower',          # interface
    'org.freedesktop.UPower'           # bus name
)



bus.add_signal_receiver(           # defince the signal to listen to
    handle_suspend_callback,            # name of callback function
    'PropertyChanged',                        # singal name
    'org.freedesktop.UPower',          # interface
    'org.freedesktop.UPower'           # bus name
)

loop = gobject.MainLoop()          # define mainloop
loop.run()                         # run main loop
