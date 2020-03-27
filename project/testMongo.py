from mongo_connection import MongoDbConnect

if __name__ == "__main__":
    con = MongoDbConnect('test')
    collection = 'PassProgram'
    obj = [
        {
            "_id": 7,
            "service": "mine",
            "user": "teste01",
            "pass": "123456"
        },
        {
            "_id": 6,
            "service": "mine",
            "user": "teste01",
            "pass": "123456"
        }
    ]
    id = con.insert_mult_objects(collection, obj)
    print(id)
    _ = con.update_object_generic_id(collection, 7, 'user', 'teste02')
    ret = con.get_object_generic(collection, '_id', 7)
    print(ret)
    _ = con.update_object_generic(collection, 'service', 'mine', 'pass', 'olaUpdate')
    ret = con.get_object_generic(collection, '_id', 7)
    print(ret)
    _ = con.delete_by_service(collection, 'mine')
    con.close()