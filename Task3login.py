from Task3 import read_stuff
from Task3 import dict
import getpass
import codecs
if __name__ == '__main__':
    def login():
        values_present = read_stuff()
        usr = input('Enter username: ')
        passwd = codecs.encode(getpass.getpass('Enter password: '), 'rot_13')
        if (usr,passwd) in dict.keys():
            print('Access Granted')
        else:
            print('Access denied')
    login()