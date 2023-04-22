import pymongo

if __name__ == '__main__':
    print("Hello World")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
#     after this now i can make the database
    db = client["Samridhi"]
    # after this we will create collection
    collections = db['mysamplecollections']
    # one = collection.find_one({'name':'Sam'})
    # allDocs = collections.find({'Location': 'Noida'}).limit(2)
    # # print(allDocs.count())
    # for item in allDocs:
    #     print(item)
    prev = {"Name":"Ram"}
    nextt = {"$set":{"Location": "kochi"}}
    up = collections.update_many(prev,nextt)
    print(up.modified_count)
