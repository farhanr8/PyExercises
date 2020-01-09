'''
@author: S M Farhanur Rahman
@NetID: sxr190032
@Date: 09/11/2019
Reference:
- https://docs.python.org/2/library/socket.html#example
- https://utdallas.app.box.com/s/gi1myjbbjqr83y2flllpusf1pdluivkd/file/519060898897
'''

from socket import *

HOST = gethostname()    # 192.168.1.88
PORT = 2000             # As shown in course PPT

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    print '\nServer Listening...'
    conn, addr = s.accept()
    print '\nConnected by', addr

    try:
        request = conn.recv(1024)               # HTTP request from browser
        print '\nClient Request:', request

        # Open the file that is in the first line of the HTTP request header
        filename = request.split()[1]
        filename = filename[1:]
        print '\nClient Requesting File:', filename
        f = open(filename)
        filecontent = f.read()

        print '\nFile Found'
        conn.send("HTTP/1.1 200 OK\r\n\r\n")    # Send OK HTTP header line to client
        conn.send(filecontent)                  # Send the content of the file to client

        conn.close()

    except IOError:
        print '\nFile Not Found'

        # Send ERROR HTTP header line to client
        conn.send("HTTP/1.1 404 Not Found\r\n")

        conn.close()

s.close()