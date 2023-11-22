from experi import passwords
import getpass
if __name__ == '__main__':
    pass
question = input('Login/Signup: ').lower()
if question == "signup":
    def password_s():
        username = input("Create username: ")
        while True:
            dict = {}
            special_characters = '!@#$%&()-_[]}{;:"./<>?'
            numbers = '1234567890'
            password = getpass.getpass("Create password: ")
            try:
                if len(password) <= 6:
                    print('Please use a longer password')
                    continue
                elif any(map(lambda x: x in password, special_characters)):
                    if any(map(lambda y: y in password, numbers)):
                        password_1 = getpass.getpass("Re-Enter password")
                        if password == password_1:
                            passwords.update({username,password_1})
                            return
                        else:
                            print('passwords do not match')
                    else:
                        print('Please use numeric digits')
                        continue
                else:
                    print("Please use a stronger password")
                    continue
            except:
                pass
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