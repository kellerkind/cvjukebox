from pylms import server

s = server.Server(hostname='rpi-1')

p = s.get_players()[0]
p.play
