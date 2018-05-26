import csv
import MySQLdb
from flask import Flask,request
import json
app = Flask(__name__)

db = MySQLdb.connect(host="db4free.net",  # your host 
                     user="fyletask",       # username
                     passwd="",     # password
                     db="fyletask")   # name of the database

@app.route('/',methods=['GET', 'POST'])
def index():
	cur = db.cursor()
	data=request.get_json()
	print(data.keys())
	datatosend=[]
	dataitem={}
	with open('bank_branches.csv', encoding="utf8") as myFile:  
		reader = csv.reader(myFile, quotechar='|')
		if data["type"]=="1":
			if "ifsc" in data.keys():
				ifsc = data["ifsc"]
				query = "SELECT a.`ifsc`,b.`name` AS 'bankname',a.`branch`,a.`address`,a.`city`,a.`district`,a.`state` FROM `branches` AS a,`banks` AS b WHERE a.`ifsc`='"+ifsc+"' AND a.`bank_id`=b.`id`"
				cur.execute(query)
				results = cur.fetchall()
				if len(results)==0:
					dataitem["failure"]="No Data found of the given IFSC number"
				else:
					dataitem=results[0]
			else:
				dataitem["failure"]="Incorrect Parameters Supplied"
			datatosend.append(dataitem)
			return json.dumps({'response':datatosend}), 200, {'ContentType':'application/json'}
		elif data["type"]=="2":
			if "bankname" in data.keys() and "city" in data.keys():
				city = data["city"]
				city = city.upper()
				bank_name = data["bankname"]
				bank_name = bank_name.upper()
				query = "SELECT a.`ifsc`,b.`name` AS 'bankname',a.`branch`,a.`address`,a.`city`,a.`district`,a.`state` FROM `branches` AS a,`banks` AS b WHERE b.`name`='"+bank_name+"' and b.`id`=a.`bank_id` and a.`city`='"+city+"'"
				cur.execute(query)
				if len(results)==0:
					dataitem["failure"]="No Data found of the Bank Name and City Combination"
					datatosend.append(dataitem)
				else:
					for i in results:
						datatosend.append(i)
			else:
				dataitem["failure"]="Incorrect Parameters Supplied"
				datatosend.append(dataitem)
			
			return json.dumps({'response':datatosend}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
	app.run()
