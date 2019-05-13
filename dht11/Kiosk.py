# coding: utf-8
from guizero import App, Drawing
import RPi.GPIO as GPIO
import dht11, time, datetime

# LCD 화면 크기 
# $ fbset -s 명령어로 알아낼 수 있음.
width = 800
height = 480

app = App( width=width, height=height )

# 윈도우 크기를 최대화 함.
app.tk.attributes("-fullscreen",True)

# Drawing 객체 생성.
d = Drawing(app, width=width, height=height)

w = width
h = height
        
d.rectangle( 0, 0, w, h, color="light blue", outline=True, outline_color="white")

if 0 : 
    d.oval(30, 30, 50, 50, color="white", outline=True)
    d.oval(170, 30, 190, 50, color="white", outline=True)
    d.triangle(110, 90, 120, 110, 100, 110, color="black")
    d.line(50, 180, 50, 160, color="red", width=5)
    d.line(50, 180, 170, 180, color="red", width=5)
    d.line(170, 180, 170, 160, color="red", width=5)
    d.text(10, 10, "Hello", color="red", size=12) 
pass

# GPIO 초기화 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# 14 번 GPIO 핀을 통하여 습도, 온도를 읽어 들임.
dht11 = dht11.DHT11(pin=14)

# 시간을 한국 시간에 맞추는 방법
# 아래의 명령어를 터미널에서 실행한다.
# $ sudo apt install ntpdate
# $ sudo ntpdate ntp.ubuntu.com 

temperature = -1000
humidity = -1
# 화면 그래픽을 업데이트 함.
def update_screen() :
    date = datetime.datetime.now() 
    print("Last valid input: " + str( date ))

    # 전체 화면을 clear 함.
    d.rectangle( 0, 0, w, h, color="light blue", outline=True, outline_color="white")

    m = w/10
    x = m
    y = h/2 - 20
    text = "%d월 %d일" % ( date.month, date.day )
    d.text( x, y, text, color="white", font="Helvetica 24 bold", size=36 ) 
    
    y = y + 60
    text = "%02d분 %02d초" % ( date.minute, date.second )
    d.text( x, y, text, color="white", font="Helvetica 24 bold", size=50 ) 

    x = w*3/5 
    d.line( x, h/10, x, h*9/10, color="white", width=4)

    # 온도 습도 데이터 읽기
    result = dht11.read()

    global temperature
    global humidity

    if result.is_valid(): 
        temperature = result.temperature 
        humidity = result.humidity
        print("Temperature: %d C" % temperature )
        print("Humidity: %d %%" % humidity )  
    else :
        print( "WARN: dht11 data is invalid!")
    pass

    if temperature > -1000 :  
        text = "%s" % temperature  
    else :
        text = "__"
    pass

    x = w*3/5 + 100
    y = h/2 - 10 
    d.text( x, y, text, color="white", font="Helvetica 24 bold", size=50 ) 

    x = w*3/5 + 200 
    d.text( x, y, "°C", color="white", font="Helvetica 24 bold", size=20 )
        

    # 1000 mili sec 후에 시간을 업데이트 한다.
    d.after(1000, update_screen ) 
pass 

# 1000 mili sec 후에 시간을 업데이트 한다.
d.after(1000, update_screen ) 

# 앱을 화면에 표시함
app.display()

# end