from Task3 import dict
import getpass
import codecs
from Task3 import read_stuff
if __name__ == '__main__':
    def write2():
        values_present = read_stuff()
        usr = input('Enter username: ')
        passwd = codecs.encode(getpass.getpass('Enter password: '), 'rot_13')
        if (usr, passwd) in dict.keys():
            name = dict[usr,passwd]
            with open('saving_ps.txt', 'r') as f:
                file = f.read()
                f.close()
                new_file = file.replace((usr+':'+passwd+':'+name),(''))
                with open('saving_ps.txt', 'w') as f:
                    f.write(new_file)
                    f.close()

    write2()