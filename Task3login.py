from Task3 import read_stuff
from Task3 import dict
import getpass
import codecs
if __name__ == '__main__':
    values_present = read_stuff()
    usr = input('Enter username: ')
    if usr in dict.keys():
        passwd = codecs.encode(getpass.getpass('Enter password: '), 'rot_13')
        if passwd == dict[usr]:
                print('Access Granted')
        else:
            print('Username or password incorrect')
    else:
        print('Username or password incorrect')
