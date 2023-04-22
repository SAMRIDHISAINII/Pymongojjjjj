import pymongo

if __name__ == '__main__':
    print("Hello World")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    alldatabases = client.list_database_names()
    print(alldatabases)
    col = client['Sam']
    print(col.list_collection_names())
