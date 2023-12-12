default_file = 'saving_ps.txt'
dict = {}
def read_stuff():
    with open(default_file,'r') as f:
        for line in f:
            username, password, name  = line.strip().split(':')
            dict[username,password] =  name
    return dict
def login(passwd):
    values_present = read_stuff()
    return values_present[passwd]
if __name__ == '__main__':
    print(read_stuff())