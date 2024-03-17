import csv
import json

import cv2
from pyzbar.pyzbar import decode


def parse_data(data):
    csv_data = {
        "name": "",
        "id": "",
        "tel": ""
    }
    data = json.loads(data)
    for key in data.keys():
        csv_data[key] = data[key]
    return csv_data


def to_csv(data):
    with open("sample.csv", "a+", encoding='utf8', newline="") as file_object:
        # ①csv.DictWriterの第2引数に配列でヘッダーを指定する
        dw_object = csv.DictWriter(file_object, list(data.keys()))

        # ファイル先頭にファイルポインタを移動
        file_object.seek(0)

        # 新規ファイルであればヘッダー書き込み
        if file_object.read() == "":
            # ②writeheader()を実行すると①で指定したヘッダーが書き込まれる
            dw_object.writeheader()

        # ③writerow()で一行ずつ書き込む
        dw_object.writerow(data)


def capture():
    # カメラデバイス取得
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    frame = cv2.imread('qrcode.png', cv2.IMREAD_UNCHANGED)
    tmp = ""

    while True:
        # カメラから1フレーム読み取り
        # ret, frame = cap.read()

        if frame is not None:
            # QRコードを認識
            data = decode(frame)
            print(data)
            # QRコードのデータ(SJIS)をUTF-8に変換
            value = data[0][0].decode('utf-8', 'ignore')
            # print(value)

            # 値が空でなく、かつ、ひとつ前のデータ同じではないとき
            if value != "" and value != tmp:
                # データを一時保管
                tmp = value
                to_csv(parse_data(value))

            # ウィンドウ表示
            cv2.imshow('frame', frame)

        # Qキー押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()


capture()