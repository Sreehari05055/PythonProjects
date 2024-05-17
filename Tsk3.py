default_file = 'saving_ps.txt'
dict = {}
def read_stuff():
    with open(default_file,'r') as f:
        for line in f:
            if len(line.split()) == 0:
                continue
            username, password, name, mail  = line.strip().split(':')
            dict[username,password] =  name, mail
    return dict
if __name__ == '__main__':
    print(read_stuff())
