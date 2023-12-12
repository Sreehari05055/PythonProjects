import getpass
import codecs
if __name__ == '__main__':    
        dict_1 = {}
        name_1 = input('Enter full name: ')
        pswrd = codecs.encode(getpass.getpass('Create password: '), 'rot_13')
        if len(pswrd) >= 8:
            while True:
                    usr_1 = input('Create username: ')
                    try:   
                        with open('saving_ps.txt', 'r') as f:
                            for line in f:
                                usr, pswd, name1 = line.strip().split(':')
                                dict_1[usr] = pswd, name1
                        if (usr_1) in dict_1.keys():
                            print('Username already exists, try again')
                            break
                        else:
                            with open('saving_ps.txt', 'a') as w:
                                w.write('\n')
                                w.write(usr_1)
                                w.write(':')
                                w.write(pswrd)
                                w.write(':')
                                w.write(name_1)
                                w.close()
                            print('You have signed in')
                    except IndexError:
                        print('nice')
                    break
        else:
             print('Please use a longer password')