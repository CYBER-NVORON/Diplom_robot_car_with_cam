from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
import time, random
from AlphaBot import AlphaBot
from camera_opencv import Camera
import socket

app = Flask(__name__)

@app.route('/<FUNCTION>')
def command(FUNCTION=None):
    car.setPWMA(float(speed))
    car.setPWMB(float(speed))
    exec(FUNCTION.replace("<br>", "\n"))
    return ""

def left():
    car.left()
    print("Turn left")

def right():
    car.right()
    print("Turn right")

def back():
    car.backward()
    print("Turn back")

def forward():
    car.forward()
    print("Turn straight")

def stop():
    car.stop()
    print("Stop")

def left_servo():
    print("Turn left")

def right_servo():
    print("Turn right")

def down_servo():
    print("Turn back")

def up_servo():
    print("Turn straight")

def stop_servo():
    print("Stop")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def videostreaming_generator():
    """Видео стриминг генератор"""
    yield b'--frame\r\n'
    while True:
        yield b'Content-Type: image/jpeg\n\n' + Camera().get_frame() + b' --frame'


@app.route('/video_feed')
def video_feed():
    """Маршрут потоковой передачи видео"""
    return Response(videostreaming_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    car = AlphaBot()
    speed = 50
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip=s.getsockname()[0]
    s.close()
    app.run(debug=True, host=ip)