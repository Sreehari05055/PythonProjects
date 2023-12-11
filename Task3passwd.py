import codecs 
import getpass 
from Task3 import read_stuff
from Task3 import dict
if __name__ == '__main__':
    dict_3 = {}
    values_present = read_stuff()
    usr = input('Enter username: ')
    passwd = codecs.encode(getpass.getpass('Enter current password: '), 'rot_13')
    if (usr,passwd) in dict.keys():
           name = dict[usr,passwd]
           del dict[usr,passwd]
           pswrd = codecs.encode(getpass.getpass('Enter new password: '), 'rot_13')
           again = codecs.encode(getpass.getpass('re-enter password: '), 'rot_13')
           if pswrd == again:
                with open('saving_ps.txt', 'r') as f:
                    for line in f:
                        usr_2, pswd, name1 = line.strip().split(':')
                        dict[usr_2, pswd] = name1
                    f.close()
                with open('saving_ps.txt', 'a') as w:
                    w.write('\n')
                    w.write(usr)
                    w.write(':')
                    w.write(pswrd)
                    w.write(':')
                    w.write(name)
    else:
        print('Access denied')