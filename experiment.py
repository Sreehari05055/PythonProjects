import json
import getpass
from saving_ps import save
if __name__ == '__main__':    
    pass
question = input('Login/Signup: ').lower()
if question == "signup":
    def password_s():
        dict = {}   
        while True:
            username = input("Create username: ")
            if username in save:
                print("Username already exists")
                continue
            special_characters = '!@#$%&()-_[]}{;:"./<>?'
            numbers = '1234567890'
            password = getpass.getpass("Create password: ")
            try:
                if len(password) <= 6:
                    print('Password should be a minimum of 12 characters')
                    continue
                elif any(map(lambda x: x in password, special_characters)):
                    if any(map(lambda y: y in password, numbers)):
                        password_1 = getpass.getpass("Re-Enter password: ")
                        if password == password_1:
                            dict[username] = password
                            with open("saving_ps.py", "a") as f:
                                json.dumps(save.update(dict),f)
                                f.write('\n')
                                return
                        else:
                            print('passwords do not match')
                            continue
                    else:
                        print('Please use numeric digits')
                        continue
                else:
                    print("Please use a stronger password")
                    continue
            except Exception as e:
                print(e)
            break
    password_s()
else:
    if question == "login":
        def login():    
            while True:
                try:
                    username_1 = input("Enter username: ")
                    password_2 = getpass.getpass("Enter password: ")
                    if passwords[username_1] == password_2:
                        print("ok")
                        return
                    else:
                        print("Username or Password incorrect")
                        continue
                except KeyError:
                    print("Username or Password incorrect")
        login()