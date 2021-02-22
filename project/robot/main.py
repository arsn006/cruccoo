# -*- coding: utf-8 -*-
import socket
import time
import picamera
import motor
import model
import led

host = 'localhost'
port = 10500
duration = 1    # 何秒間動作を続けるか
'''
def shoot(fn):
    # カメラ初期化
    with picamera.PiCamera() as camera:
        # 解像度の設定
        camera.resolution = (1024, 768)
        # 撮影の準備
        camera.start_preview()
        # 準備している間、少し待機する
        time.sleep(2)
        # 撮影して指定したファイル名で保存する
        camera.capture(fn)
        print('complete')
'''
# Juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# モーターのインスタンス化
dcmotor1 = motor.DC_Motor_DRV8835(a_phase=14, a_enbl=23)
dcmotor2 = motor.DC_Motor_DRV8835(a_phase=15, a_enbl=24)

# 学習済みモデルのインスタンス化
svm_model = model.Predict_SVM()

# LEDモデルのインスタンス化
led_model = led.LED()

res = ''
while True:
    # 音声認識の区切りである「改行+.」がくるまで待つ
    while (res.find('\n.') == -1):
        # Juliusから取得した値を格納していく
        msg = sock.recv(1024)
        res += msg.decode("utf-8")

    word = ''
    for line in res.split('\n'):
        # Juliusから取得した値から認識文字列の行を探す
        index = line.find('WORD=')
        print('OK')
        #print("line", line)
        # 認識文字列があったら...
        if index != -1:
            # 認識文字列部分だけを抜き取る
            line = line[index + 6 : line.find('"', index + 6)]
            # 文字列の開始記号以外を格納していく
            if line != '[s]':
                word = word + line

        # 「クルックーおいで」という文字列を認識したら...
        if word == "クルックーおいで":
            #shoot('my_pic.jpg')
            svm_model.predict()
            dcmotor1.fwd()
            dcmotor2.fwd()
            led_model.lighting(2, 0.5)
            #time.sleep(duration)
            dcmotor1.stop()
            dcmotor2.stop()
            print("クルックーおいで")
        elif word == "前に進め":
            print("motor")
            dcmotor1.fwd()
            dcmotor2.fwd()
            print("led")
            led_model.lighting(2, 0.5)
            #time.sleep(duration)
            print("m stop")
            dcmotor1.stop()
            dcmotor2.stop()
            print("前に進め")
        elif word == "後ろに下がれ":
            print("motor")
            dcmotor1.back()
            dcmotor2.back()
            print("led")
            led_model.lighting(2, 0.5)
            #time.sleep(duration)
            print("m stop")
            dcmotor1.stop()
            dcmotor2.stop()
            print("後ろに下がれ")
        elif word == "右に曲がれ":
            dcmotor1.back()
            dcmotor2.fwd()
            led_model.lighting(1, 0.5)
            #time.sleep(duration)
            dcmotor1.stop()
            dcmotor2.stop()
            print("右に曲がれ")
        elif word == "左に曲がれ":
            dcmotor1.fwd()
            dcmotor2.back()
            led_model.lighting(1, 0.5)
            #time.sleep(duration)
            dcmotor1.stop()
            dcmotor2.stop()
            print("左に曲がれ")
        elif word == "全体止まれ":
            print("motor")
            dcmotor1.stop()
            dcmotor2.stop()
            print("全体止まれ")
        
        print("word", word)
        res = ''

