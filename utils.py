from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=MongoClient(),
    port=int(2000),
    username=dj19,
    password=aa09094553940
    )
    db_handle = client['djdb']
    return db_handle, client