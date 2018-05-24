import requests
import json,time

# x={"homeid":"Home1","roomid":"Room1","devname":"Light1","username":"xyz","status":"1","timertime":"2018-01-23 07:18:21"}
# x={"type":"fetcharduino","homeid":"Home1","ardid":"Ard1"}
# x={"type":"checklogin","bhama":"","adhar":"6543211"}
# x={"Type":"changeoverallranks"}
# x={"Type":"findpercentage"}
x={"type":"1","ifsc":"ZSBL0000341"}
# x={"type":"2","bankname":"ZILA SAHAKRI BANK LIMITED GHAZaIABAD","city":"GHAZIABAD"}
# x={"Type":"changeoverallranks"}
resp = requests.post("https://fylework.herokuapp.com",json=x)
print(resp.json())
# while True:
# 	resp = requests.post("http://localhost:7824",json=x)
# 	print(resp.json())
# 	time.sleep(5)

