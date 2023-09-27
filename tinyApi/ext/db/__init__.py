from tinydb import TinyDB, Query, where


Serach = Query()
def init_db():
    db = TinyDB('tinyApi/ext/db/database.json', 
                indent=4, 
                sort_keys=True
                )
    return db