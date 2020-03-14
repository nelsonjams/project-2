# Dependencies
import requests
import pymongo
import json
import chardet

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# drop previous database so there is no duplicate
client.drop_database('nyc_311_data')


# Define database and collection
db = client.nyc_311_data 
collection = db.airQuality
collection = db.asbestos
collection = db.leadDust
collection = db.industrialWaste
collection = db.mold
collection = db.waterQuality

# URL of page to be scraped

baseURL = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?"

date = "$where=created_date between '2019-03-07T02:12:00.000' and '2020-03-07T02:12:00.000'"

airQuality = "&complaint_type=Air Quality"
asbestos = "&complaint_type=Asbestos"
leadDust = "&complaint_type=Construction Lead Dust"
industrialWaste = "&complaint_type=Industrial Waste"
mold = "&complaint_type=Mold"
waterQuality = "&complaint_type=Water Quality"

# Create a url for each complaint type, decode json, and load to Mongodb

airQuality_url = (baseURL + date + airQuality)
aQ = requests.get(airQuality_url)
Cybermen = json.loads(aQ.content.decode(chardet.detect(aQ.content) ["encoding"]))
# print(Cybermen)
db.airQuality.insert_many(Cybermen)

asbestos_url = (baseURL + date + asbestos)
asb = requests.get(asbestos_url)
Daleks = json.loads(asb.content.decode(chardet.detect(asb.content) ["encoding"]))
# # print(Daleks)
db.asbestos.insert_many(Daleks)

leadDust_url = (baseURL + date + leadDust)
lD = requests.get(leadDust_url)
Davros = json.loads(lD.content.decode(chardet.detect(lD.content) ["encoding"]))
db.leadDust.insert_many(Davros)

industrialWaste_url = (baseURL + date + industrialWaste)
iW = requests.get(industrialWaste_url)
Supernova = json.loads(iW.content.decode(chardet.detect(iW.content) ["encoding"]))
db.industrialWaste.insert_many(Supernova)

mold_url = (baseURL + date + mold)
m = requests.get(mold_url)
Rick = json.loads(m.content.decode(chardet.detect(m.content) ["encoding"]))
db.mold.insert_many(Rick)

waterQuality_url = (baseURL + date + waterQuality)
wQ = requests.get(waterQuality_url)
Tammy = json.loads(wQ.content.decode(chardet.detect(wQ.content) ["encoding"]))
db.waterQuality.insert_many(Tammy)

print("Your boos mean nothing, I've seen what makes you cheer - Rick Sanchez")

# # TARDIS = json.loads(r.content.decode(chardet.detect(r.content) ["encoding"]))

# # allcomplaint = db.collection.distinct("complaint_type")

# # print(allcomplaint)