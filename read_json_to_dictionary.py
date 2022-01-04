import json

def read_json_to_dictionary():
	with open('C:/Users/user/Desktop/detect_license_plate/data/json/', 'r',encoding='UTF8') as f:
		json_data	= json.load(f)
	print(type(json_data))
	return json_data

read_json_to_dictionary()