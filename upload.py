from mongoConnection import db
def upload(data,type='verbal'):
    collection = db[type]  # Replace with your collection name
    collection.insert_one(data)
    print("inserted to "+type)
    return True


if __name__ == "__main__":
    upload({
        "question":"bottle",
        "answer":"water"
    })