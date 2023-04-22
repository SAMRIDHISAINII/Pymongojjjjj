import pymongo

if __name__ == '__main__':
    print("Hello World")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
#     after this now i can make the database
    db = client["Samridhi"]
    # after this we will create collection
    collections = db['mysamplecollections']
    # after this insert a document iska bina it wont work
    # dictionary = {'name': 'sam', 'marks': 45}
    # collections.insert_one(dictionary)
    # dictionary3 = {'name': 'sam7', 'marks': 95}
    # collections.insert_one(dictionary3)
    # dictionary5 = {'name': 'sam87', 'marks': 25}
    # collections.insert_one(dictionary5)

#     making it simple
    insert_These = [
        {'_id': 1,'Name': 'Sam', 'Location' : 'Noida', 'Marks': 89},
        {'Name': 'Ram', 'Location': 'Greater Noida', 'Marks': 99},
        {'Name': 'Cam', 'Location': 'Delhi', 'Marks': 79},
        {'Name': 'Tam', 'Location': 'Gurgaon', 'Marks': 70}
    ]
    collections.insert_many(insert_These)





