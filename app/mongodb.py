import pymongo

account = 'yuxp0130'
pwd = 'Aa09260130'
url = f"mongodb+srv://{account}:{pwd}@cluster0.omkx4hi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
myClient = pymongo.MongoClient(url)

# for db in myClient.list_database_names():
#     print(db)

myDB = myClient['newDB']
myCol = myDB['members']


def getMembers():
    return myCol


data = myCol.find_one(
    {'password': 'Aa7389988!'}
)

if data is None:
    print('帳密有誤')
else:
    print(data)

for col in myCol.find({'password': 'Aa7389988!'}):
    print(col)

myClient.close()
