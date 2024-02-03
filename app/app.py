import csv
import json
 
# JSONファイルのロード
with open('test.json', 'r',encoding="utf-8") as f:
    json_dict = json.load(f)
with open('sensor_output.csv', 'w', newline='') as f:
    print(json_dict.keys())
    writer = csv.DictWriter(f, fieldnames=json_dict.keys(), 
                            doublequote=True, 
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(json_dict)