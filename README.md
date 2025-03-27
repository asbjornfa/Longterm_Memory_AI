Hello there,

I made this simple piece of code to store a conversation with an AI longterm.

For this project i have used MongoDB as my database.

You will get all neccesary imports by entering the command below:

```
pip install -r requirements.txt   
```

Also remember to set up a MongoDB account and populate the DB connection with your own:

```
client = MongoClient("mongodb://localhost:27017/")
db = client["chat_memory"]
collection = db["conversations"]
model = "gemma2:9b"
```

Happy programming :)
