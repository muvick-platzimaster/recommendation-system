from pymongo import MongoClient

#conenection to DB
host = 'HOST'
user = 'USER'
password = 'PASSWORD'
name = 'NAME'

uri = f"mongodb+srv://{user}:{password}@{host}/{name}?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['muvick-data-app']
