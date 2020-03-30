import business as bn

if __name__ == "__main__":
    for obj in bn.get_pass_service_usr('test', 'testt'):
        print(obj)
    a = bn.delet('test', 'testt')
    print(a)
    for obj in bn.get_pass_service_usr('test', 'testt'):
        print(obj)