import RPi.GPIO as gpio
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '10.0.0.130'    # Change this to your Raspberry Pi IP address
host_port = 8000

en1 = 25
en2 = 27
gpio.setmode(gpio.BCM)
gpio.setup(en1,gpio.OUT)
gpio.setup(en2,gpio.OUT)

gpio.setup(17, gpio.OUT) #right wheels
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT) #left wheels
gpio.setup(24, gpio.OUT)

p1 = gpio.PWM(en1,1000)
p2 = gpio.PWM(en2,1000)

p1.start(50)
p2.start(50)


def forward():
 p1.ChangeDutyCycle(75)
 p2.ChangeDutyCycle(75)
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, True)
 gpio.output(24, False)

def reverse():
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 
 
def turnRight():
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(0.1)
 stop()
 
def turnLeft():
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(0.1)
 stop()


def stop():
 gpio.output(17, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)

 

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command 
            'curl -I http://server-ip-address:port' 
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command 
            'curl http://server-ip-address:port' 
        """
        html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <h1>Senior Design Robot Project</h1>
            <p>Current GPU temperature is {}</p>
            <p>Move: </p>
            <p><a href="/f">Forward</a> </p>
            <p><a href="/r">Reverse</a></p>
            <p><a href="/tr">Turn Right</a> </p>
            <p><a href="/tl">Turn Left</a> </p>
            <p><a href="/stop">Stop</a></p>
            <div id="status"></div>
            <script>
                document.getElementById("status").innerHTML="{}";
            </script>
            </body>
            </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            satus='home'
        elif self.path=='/f':
            forward()
            status='Forward'
        elif self.path=='/r':
            reverse()
            status='Backwards'
        elif self.path=='/tr':
            turnRight()
            stop()
            status='turning right'
        elif self.path=='/tl':
            turnLeft()
            stop()
            status='turning left'
        elif self.path=='/stop':
            stop()
            status='Stop'
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))
  
  
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()