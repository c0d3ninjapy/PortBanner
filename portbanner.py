import socket, sys

# Coded by c0deninja
# Discord: http://discord.gg/JV6pu5q
# Connects to a specific port and prints out the banner.
# This script is useful for pen testers to check the version of the service running on that port.
# EX: python portbanner.py IP PORT

if len(sys.argv) !=3:
	print ("Usage portbanner.py <host> <port>")
	sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	data = s.connect((host, port))
	banner = s.recv(1024)
	if data == 0:
		print (banner)
except socket.error:
	print ("couldn't connect to host")
