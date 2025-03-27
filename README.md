Hello there,

I made this project to showcase a simple solution for short-term memory in AI.

For this project i have used MongoDB as my database.


**Setup vitual environment**

If you currently dont have a .venv or base file please use this command to create one.
***This will create a file directory called base with everything***

On Mac:
```
python3 -m venv base
```

On Windows:
```
python -m venv base
```
When the file is created, you can enter the virtual environment like this.

On Mac:
```
source base/bin/activate
```
On Windows:
```
base/Scripts/activate
```

**Relevant imports**

For relevant imports use this command:
```
pip install -r requirements.txt
```

For adding additional imports to the requirements file use this command:
```
pip freeze > requirements.txt
```

**How to run the application**

This project is using FastApi, with uvicorn.

To run access the api endpoint use this command:

```
uvicorn main:app --reload
```

Also remember to set up a MongoDB account and populate the DB connection with your own:

```
client = MongoClient("mongodb://localhost:27017/")
db = client["chat_memory"]
collection = db["conversations"]
model = "gemma2:9b"
```


Happy programming :)
