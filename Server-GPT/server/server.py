import pyrebase
import time
from adafruit_servokit import ServoKit

config = {
  "apiKey": "AIzaSyBprqeKV3fOZtKRObEXKMM3i1vDOg1a6Qw",
  "authDomain": "pupper-robot.firebaseapp.com",
  "databaseURL": "https://pupper-robot-default-rtdb.firebaseio.com",
  "storageBucket": "pupper-robot.appspot.com",
  "serviceAccount" : "pupper-robot-firebase-adminsdk-xwj78-f056f6fdab.json"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()


def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

pi = ServoKit(channels=16)

import socket
import threading

def handler(c,a):
    global connections
    while True:
        data = c.recv(2014)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 2500))
sock.listen(1)
print("Waiting..")
connections = []

while True:
    c, a =sock.accept()
    
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    
    connections.append(c)
    print(connections)

    my_stream = db.child("f").stream(stream_handler)
    my_data = db.child("f").get()
    print("data : ", my_data.val())
	#     print("1")
	#         print("stream", my_stream["data"])
	#         print("new : ", data)
	#         print("servo_data : ", servo_data)

	#pigpio.error: 'pulsewidth not 0 or 500-2500'

    if (my_data.val() == 1):
        pi.set_servo_pulsewidth(15, 1500)
        time.sleep(3)
        db.child('f').set(4)
    elif (my_data.val() == 0):
        pi.set_servo_pulsewidth(15, 2500)
        time.sleep(1)
        db.child('f').set(4)


