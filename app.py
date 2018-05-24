import csv

from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	data=request.get_json()
	print(data.keys())
	datatosend=[]
	dataitem={}
	with open('bank_branches.csv', encoding="utf8") as myFile:  
		reader = csv.reader(myFile, quotechar='|')
		if data["type"]=="1":
			if "ifsc" in data.keys():
				ifsc = data["ifsc"]
				for row in reader:
					if row[0]==ifsc:
						dataitem={"ifsc":row[0],"bank_id":row[1],"branch":row[2],"address":row[3],"city":row[4],"district":row[5],"state":row[6],"bank_name":row[7]}
				if not dataitem:
					dataitem["failure"]="No Data found of the given IFSC number"
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
				for row in reader:
					if row[4]==city and row[7]==bank_name:
						dataitem={"ifsc":row[0],"bank_id":row[1],"branch":row[2],"address":row[3],"city":row[4],"district":row[5],"state":row[6],"bank_name":row[7]}
						datatosend.append(dataitem)
				if len(datatosend)==0:
					dataitem["failure"]="No Data found of the Bank Name and City Combination"
					datatosend.append(dataitem)
			else:
				dataitem["failure"]="Incorrect Parameters Supplied"
				datatosend.append(dataitem)
			
			return json.dumps({'response':datatosend}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
	app.run()
