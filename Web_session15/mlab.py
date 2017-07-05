import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds129442.mlab.com:29442/langtuhaihoa

host = "ds129442.mlab.com"
port = 29442
db_name = "langtuhaihoa"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())