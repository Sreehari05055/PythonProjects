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
            pswrd = codecs.encode(getpass.getpass('Enter new password: '), 'rot_13')
            again = codecs.encode(getpass.getpass('re-enter password: '), 'rot_13')
            if pswrd == again:
                with open('saving_ps.txt', 'r') as f:
                    file = f.read()
                    f.close()
                    new_file = file.replace((usr+':'+passwd+':'+name),(usr+':'+pswrd+':'+name))
                    with open('saving_ps.txt', 'w') as f:
                         f.write(new_file)
                         f.close()
    else:
        print('Access denied')