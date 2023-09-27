from tinydb import TinyDB, Query


db = TinyDB('database.json')

db.insert(
    {
        "realm": "Mirrodim",
        "type": "Steel",
        "experience": "20000",
        "level": "35",
        "gold": "10000",
        "food": "0",
        "building": "3",
        "unit": "101"
    }

)
