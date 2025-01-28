import traceback
import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://myproject:myproject@myproject.wqcf3.mongodb.net/?retryWrites=true&w=majority&appName=myproject"
)
result = str(client)

if "connect=True" in result:
    try:
        print("MONGODB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("MONGODB CONNECTION FAILED ❌")
    except:
        pass

folder = client["NEW_DATABASE"]
usersdb = folder.NEW_USERS
chats_auth = folder.NEW_CHATS
gcdb = folder.NEW_GC
sksdb = client["ANOTHER_DATABASE"].ANOTHER_COLLECTION
confdb = client["ANOTHER_DATABASE"].CONFIG_COLLECTION
