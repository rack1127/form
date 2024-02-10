import csv
import json
import cv2
from pyzbar.pyzbar import decode

def to_csv(json_dict): 
    json_dict= json.loads(json_dict)       
    with open('sensor_output.csv', 'w', newline='') as f:
        # print(json_dict.keys())
        writer = csv.DictWriter(f, fieldnames=json_dict.keys(), 
                                doublequote=True, 
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerow(json_dict)

def capture():
    # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    frame = cv2.imread('qrcode.png', cv2.IMREAD_UNCHANGED)
    tmp = ""

    while True:
        # カメラから1フレーム読み取り
        # ret, frame = cap.read()

        if frame is not None:
            # QRコードを認識
            data = decode(frame)
            # QRコードのデータ(SJIS)をUTF-8に変換
            value = data[0][0].decode('utf-8', 'ignore')
            print(value)

            # 値が空でなく、かつ、ひとつ前のデータ同じではないとき
            if value != "" and value != tmp:
                # データを一時保管
                tmp = value
                to_csv(value)

            # ウィンドウ表示
            cv2.imshow('frame', frame)

        # Qキー押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    # cap.release()
    cv2.destroyAllWindows()

capture()