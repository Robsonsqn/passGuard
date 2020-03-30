from mongo_connection import MongoDbConnect

def insert_new_pass(service, usr, pswr):
    '''Method to insert new password object in database

    Args:
        sevice (string): Service to authenticate with this password
        usr (string): Username to connect with this password
        pswr (string): Password to store in database

    Raises:

    Returns:
        object_password: Password save in database with _id
    '''
    mongo_conect = MongoDbConnect('test')
    collection = "pass_bank"
    pss = {
        'service' : service,
        'user' : usr,
        'password' : pswr
    }
    retorn = mongo_conect.insert_object(collection, pss)
    mongo_conect.close()
    return retorn

def get_pass_service(service):
    '''Method to get an password object in database by service

    Args:
        sevice (string): Service to serach in database

    Raises:

    Returns:
        object_password: Objects password
    '''
    mongo_conect = MongoDbConnect('test')
    collection = "pass_bank"
    retorn = mongo_conect.get_mult_object_generic(collection, 'service', service)
    mongo_conect.close()
    return retorn

def get_pass_service_usr(service, usr):
    '''Method to get an password object in database by service and username

    Args:
        sevice (string): Service to serach in database
        usr (string) : User to search in database

    Raises:

    Returns:
        object_password: Objects password
    '''
    mongo_conect = MongoDbConnect('test')
    collection = "pass_bank"
    camps = {'service' : service, 'user' : usr}
    retorn = mongo_conect.get_mult_object_generic_two_camp(collection, camps)
    mongo_conect.close()
    return retorn

def update_pass_usr_service(service, usr, paswr):
    '''Method to update an password object in database by service ans username

    Args:
        sevice (string): Service to serach in database
        usr (string): Username to serach in database
        passwr (string): New password to update in database

    Raises:

    Returns:
        object_password: Objects password
    '''
    mongo_conect = MongoDbConnect('test')
    collection = "pass_bank"
    camps = {'service' : service, 'user' : usr}
    retorn = mongo_conect.update_object_generic(collection, camps, 'password', paswr)
    mongo_conect.close()
    return retorn

def delet(service, usr):
    '''Method to remove an password object in database by service and username

    Args:
        sevice (string): Service to serach in database
        usr (string): Username to serach in database

    Raises:

    Returns:
        bool: removed?
    '''
    mongo_conect = MongoDbConnect('test')
    collection = "pass_bank"
    camps = {'service' : service, 'user' : usr}
    retorn = mongo_conect.delete_by_service(collection, camps)
    mongo_conect.close()
    return retorn
