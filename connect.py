import pymongo

if __name__ == '__main__':
    print("Hello World")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
