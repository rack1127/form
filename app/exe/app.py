import os
import sys
from playsound import playsound
import csv
import json
import cv2
from pyzbar.pyzbar import decode

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def to_csv(json_dict): 
    json_dict= json.loads(json_dict)
    with open('sensor_output.csv', 'a+', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=json_dict.keys(), 
                                doublequote=True, 
                                quoting=csv.QUOTE_ALL)
        f.seek(0)
        if f.read() == "":
            writer.writeheader()
        writer.writerow(json_dict)

def replace():
    with open('sensor_output.csv', "r") as f:
        s = f.read()
        s = s.replace("syurui","種類").replace("seito_yourname","生徒の名前").replace("seito_schoolnumber","学籍番号").replace("seito_phonenumber","生徒の電話番号").replace("ippan_yourname","名前").replace("ippan_phonenumber","電話番号").replace("ippan_yourplace","お住まいの地域").replace("hogosya_yourname","保護者の名前").replace("kids_yourname","お子様の名前").replace("kids_schoolnumber","お子様の学籍番号").replace("hogosya","保護者").replace("seito","生徒").replace("ippan","一般")
    with open('sensor_output.csv', "w") as f:
        f.write(s)

def capture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) # カメラ画像の横幅を1280に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) 
    tmp = ""

    while True:
        # カメラから1フレーム読み取り
        ret, frame = cap.read()
        if frame is not None:
            # QRコードを認識
            data = decode(frame)
            if not data == []:
                value = data[0][0]

                # 値が空でなく、かつ、ひとつ前のデータ同じではないとき
                if value != "" and value != tmp:
                    playsound(resource_path("read.mp3"))
                    # データを一時保管
                    tmp = value
                    to_csv(value)
                    replace()

            # ウィンドウ表示
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('window', frame)

        # Qキー押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cv2.destroyAllWindows()

capture()