#!/usr/bin/env python
import zbar, json
import threading
from pydbus import SystemBus
from gi.repository import GObject
import os
from pylms import server

class MediaDeviceThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self) 
        self.bus = SystemBus()
        try:
            self.dev = self.bus.get('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/drives/TSSTcorp_CDDVDW_SE_S084C_SATASLIM00003008cae')
            #self.dev = self.bus.get('org.freedesktop.UDisks2', '/org/freedesktop/UDisks/devices/sr0')
        except KeyError:
            print "CD LW not connected"
            quit()
        self.media = self.dev.MediaAvailable

    def _print(*a):
        print a

    def run(self):
        with self.dev.PropertiesChanged.connect(self._print) as d:
            if self.media:
                print "Media still inserted..."
		# self.dev.Eject()
            GObject.MainLoop().run()
        
class BarcodeScan(threading.Thread):

    def __init__(self):

	self.use_x11 = False
        threading.Thread.__init__(self) 
        # create a Processor
        self.proc = zbar.Processor()
        # configure the Processor
        self.proc.parse_config('enable')
        # initialize the Processor
        self.device = '/dev/video0'

	# disable x11 so no window is initialized
	# workaround taken from so:27143692
        self.proc.init(self.device, self.use_x11)
        self.data = {}
        s = server.Server(hostname='rpi-1')
        s.connect()
        self.player = s.get_players()[0]

    def detect(self):
	from datetime import datetime
        if os.path.exists('data.json'):
            self.data = json.load(open('data.json'))

        print "Detecting Barcode..."
        # enable the preview window
        self.proc.visible = self.use_x11
        # read at least one barcode (or until window closed)
        self.proc.process_one()
	ts = datetime.now().strftime('%Y-%m-%d %H:%M:%s')
        # hide the preview window
        self.proc.visible = False
        # extract results
        for symbol in self.proc.results:
            # do something useful with results
            print '[%s] decoded' % ts, symbol.type, 'symbol', '"%s"' % symbol.data
            if symbol.data in self.data:
                if not self.data[symbol.data]['media_path']:
                    print "Barcode %s already exists in DB but is not assigned" % symbol.data
                    return
                print "Playing %s..." % self.data[symbol.data]['media_path']
                self.player.playlist_play(self.data[symbol.data]['media_path'])
                return
            self.data[symbol.data] = {'music': True, 'media_path': ''}
            json.dump(self.data, open('data.json', 'w'), indent=4)


if __name__ == '__main__':

    '''
    t = MediaDeviceThread() 
    t.daemon = False
    t.start()
    '''
    t = BarcodeScan()
    t.daemon = True
    t.start()
    while True:
        import time
        time.sleep(1)
        t.detect()
