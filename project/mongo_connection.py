from pymongo import MongoClient
class MongoDbConnect:
    '''Class to connect and use mongo on generic way
    
    Args:
        db (str): Database to connect

    Attributes:
        db (str): Database to connect
    '''
 

    def __init__(self, db):
        ''' Method to start connection and select DataBase'''
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente[db]

    def insert_object(self, collection, obj):
        ''' Method to insert generic object in generic collection '''
        try:
            collec = self.banco[collection]
            print('**************************************************************************')
            print('*INSERT {} IN {}*'.format(obj, collection))
            print('**************************************************************************')
            object_id = collec.insert_one(obj).inserted_id
            print(object_id)
            return True, object_id
        except Exception as excet:
            print(excet)
            raise

    def insert_mult_objects(self, collection, objects):
        ''' Method to insert generic objects in generic collection '''
        try:
            print('**************************************************************************')
            print('*INSERT {} IN {}*'.format(objects, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            collec.insert_many(objects)
            return True
        except Exception as excet:
            print(excet)
            raise

    def get_object_generic(self, collection, key, value):
        ''' Method to get generic object in generic collection'''
        try:
            print('**************************************************************************')
            print('*GET {} ON {} FROM {}*'.format(key, value, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            objc = collec.find_one({key: value})
            return objc
        except Exception as excet:
            print(excet)
            raise

    def get_mult_object_generic(self, collection, key, value):
        ''' Method to get generic object in generic collection'''
        try:
            print('**************************************************************************')
            print('*GET {} ON {} FROM {}*'.format(key, value, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            objc = collec.find({key: value})
            return objc
        except Exception as excet:
            print(excet)
            raise

    def get_mult_object_generic_two_camp(self, collection, camps):
        ''' Method to get generic object in generic collection'''
        try:
            print('**************************************************************************')
            print('*GET ON {} FROM {}*'.format(camps, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            objc = collec.find(camps)
            return objc
        except Exception as excet:
            print(excet)
            raise

    def update_object_generic_id(self, collection, id, key, new_value):
        ''' Method to update generic object in generic collection by ID'''
        try:
            print('**************************************************************************')
            print('*UPDATE {} TO {} ON _id = {} FROM {}*'.format(key, new_value, id, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            objc = collec.update_one({'_id': id}, {'$set': {key:new_value}})
            return objc
        except Exception as excet:
            print(excet)
            raise

    def update_object_generic(self, collection, camps, k_update, new_v):
        ''' Method to update generic objects in generic collection by KEY'''
        try:
            print('**************************************************************************')
            print('UPDATE {} TO {} ON {} FROM {}'.format(k_update, new_v, camps, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            objc = collec.update_many(camps, {'$set': {k_update:new_v}})
            return objc
        except Exception as excet:
            print(excet)
            raise

    def delete_by_id(self, collection, id):
        ''' Method to delete generic objects by _id'''
        try:
            print('**************************************************************************')
            print('*DELETE ON _id =  {} FROM {}*'.format(id, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            collec.delete_one({"_id": id})
            return True
        except Exception as excet:
            print(excet)
            raise

    def delete_by_service(self, collection, camps):
        ''' Method to delete generic objects by service'''
        try:
            print('**************************************************************************')
            print('*DELETE ON {} FROM {}*'.format(camps, collection))
            print('**************************************************************************')
            collec = self.banco[collection]
            collec.delete_one(camps)
            return True
        except Exception as excet:
            print(excet)
            raise

    def close(self):
        ''' Method to close connection with mongo'''
        self.cliente.close()
