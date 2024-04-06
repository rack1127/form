import os
import sys
import pygame
import csv
import json
import cv2
from pyzbar.pyzbar import decode
from ja_cvu_normalizer.ja_cvu_normalizer import JaCvuNormalizer

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def play_mp3(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def to_csv(json_dict): 
    json_dict= json.loads(json_dict)
    ja_cvu_normalizer = JaCvuNormalizer()
    json_dict['yourname'] = ja_cvu_normalizer.normalize(json_dict['yourname'])
    with open('sensor_output.csv', 'a+',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=json_dict.keys(), 
                                doublequote=True, 
                                quoting=csv.QUOTE_ALL)
        f.seek(0)
        if f.read() == "":    
            writer.writeheader()
        writer.writerow(json_dict)

def capture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) # カメラ画像の横幅を1280に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) 
    # frame = cv2.imread('qrcode.png', cv2.IMREAD_UNCHANGED)
    tmp = ""

    while True:
        # カメラから1フレーム読み取り
        ret, frame = cap.read()
        if frame is not None:
            # QRコードを認識
            data = decode(frame)
            if not data == []:
                # QRコードのデータ(SJIS)をUTF-8に変換
                value = data[0][0].decode('utf-8', 'ignore')
                print(value)

                # 値が空でなく、かつ、ひとつ前のデータ同じではないとき
                if value != "" and value != tmp:
                    play_mp3(resource_path("read.mp3"))
                    # データを一時保管
                    tmp = value
                    to_csv(value)

            # ウィンドウ表示
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('window', frame)

        # Qキー押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    # cap.release()
    cv2.destroyAllWindows()

capture()