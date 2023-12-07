# Working with MongoDB

# MongoDB is a document based database. it is a unstructured database.

import pymongo

client = pymongo.MongoClient("mongodb+srv://aliabbas8152:paikarali8152@aliabbas8152.h1podr5.mongodb.net/?retryWrites=true&w=majority")

db = client['School']  # creating a database

coll_create = db["my_record"]  # creating a collectio inside the database

# data = {"name":"ali", "class": "DS", "time": "8:00"}    # inserting records in the form of dictionary which is called documents in MongoDB

# coll_create.insert_one(data)    # inserting records into "my_record"

# data1 = {"mail_id":"ali@gmail.com", "phone_number":123456789}

# coll_create.insert_one(data1)

# data2 = {"course":['ds', "web dev", "python"], "mentor":["ali", "abbas", "paikar"]}

# coll_create.insert_one(data2)

# data3 = [
#     {"name":"ali", "address":"delhi"},
#     {"name":"abbas", "address":"new delhi"},
#     {"name":"jawed", "address":"old delhi"},
#     {"name":"paikar", "address":"Aligarh"},
#     {"name":"hasan", "address":"lko"},
#     {"name":"haider", "address":"jaunpur"},
#     {"name":"anwar", "address":"gaon"},
#     {"name":"salman", "address":"RBL"},
#     {"name":"ali", "address":"delhi"},
# ]

# coll_create.insert_many(data3)


# data4 = {
#     "name":"notebook",
#     "quantity":50,
#     "rating":[{"score":8}, {"score":9}],
#     "size": {"height":11, "width":8.5, "unit":"inch"},
#     "status":"A",
#     "tags":["college-rules", "perforated"]
# }

# coll_create.insert_one(data4)

# list_of_records = [
#     {
#         "company name": "iNeuron",
#         "product":"AI",
#         "course":"ML"
#     },
#     {
#         "company name": "iNeuron",
#         "product":"AI",
#         "course":"DS"
#     },
#     {
#         "company name": "iNeuron",
#         "product":"AI",
#         "course":"DL"
#     }
# ]

# coll_create.insert_many(list_of_records)


# for i in coll_create.find():
#     print(i)


# random_data = [
#     {'_id':'3', "Company":"Ali inc.", "Faculty":"Ali"},
#     {'_id':'4', "Company":"Ali inc.", "Faculty":"Abbas"},
#     {'_id':'5', "Company":"Ali inc.", "Faculty":"Jawed"},
#     {'_id':'6', "Company":"Ali inc.", "Faculty":"Paikar"}
# ]

# coll_create.insert_many(random_data)


# for i in coll_create.find():
#     print(i)


# coll_create.find_one()



# for i in coll_create.find({"Company": "Ali inc."}):
#     print(i)


# for i in coll_create.find({"_id": {'$gte':'4'}}):    # $gte is for greater than or equal to
#     print(i)


# for i in coll_create.find({"_id": {'$gt':'4'}}):    # $gte is for greater than
#     print(i)


# for i in coll_create.find({"_id": {'$lte':'4'}}):    # $lte is for lesser than or equal to
#     print(i)    


# for i in coll_create.find({"_id": {'$lt':'4'}}):    # $gte is for greater than
#     print(i)




# coll_create.update_many({'company name':'iNeuron'}, {"$set":{'company name':"Ali inc."}})




# for i in coll_create.find():
#     print(i)


coll_create.drop()       # it deletes the entire collection