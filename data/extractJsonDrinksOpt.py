import requests
import json
import urllib.request


count = 0

for i in range (11000,18000):
	# Request Link, Make Json, Image
	idUrl = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=" + str(i)	
	idData = requests.get(idUrl).json()
	count = count + 1

	# Check if page is null or not, else
	if  (idData["drinks"] == None) :
		continue
 
	# Dump and Retrieve Data
	imgUrl = idData["drinks"][0]["strDrinkThumb"]
	
	with open('test.txt', "a") as file:
		file.write('\n\n')
		json.dump(idData, file, ensure_ascii = True)

	urllib.request.urlretrieve(imgUrl, idData["drinks"][0]["idDrink"] + ".jpg")
	
print ('done')
print (count)
