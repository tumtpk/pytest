from pymongo import MongoClient
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



client = MongoClient("mongodb+srv://tumtpk:1234@cluster0.tggsm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


db = client.todo_app

collection_name = db["todos_app"]
students_collection = db["students"]
courses_collection = db["courses"]
