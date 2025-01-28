import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://myproject:myproject@myproject.wqcf3.mongodb.net/?retryWrites=true&w=majority&appName=myproject"
)

result = str(client)

if "connect=True" in result:
    try:
        print("CONFIG DB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("CONFIG DB CONNECTION FAILED ❌")
    except:
        pass

COLLECTIONS = client["ANOTHER_DATABASE"]
BLACKLISTED_SKS = COLLECTIONS["ANOTHER_COLLECTION"]  # Change to the actual collection name
TOKEN_DB = COLLECTIONS["CONFIG_COLLECTION"]           # Change to the actual collection name
SKS_DB = COLLECTIONS["CONFIG_COLLECTION"]             # Change to the actual collection name
