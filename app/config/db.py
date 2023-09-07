from pymongo import MongoClient

account = 'yuxp0130'
pwd = 'Aa09260130'
url = f"mongodb+srv://{account}:{pwd}@cluster0.omkx4hi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
db_connection = MongoClient(url)
db = db_connection['ptc']
# collection = db['fixInfos']
# db_connection.close()
