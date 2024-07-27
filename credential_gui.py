import random
import codecs
from email.message import EmailMessage
import ssl, smtplib
import mysql.connector
import getpass

try:
    #The db connects to the database

    db = mysql.connector.connect(host="Your_server", user="root", password="your_password", database="credentials")

    cursor = db.cursor()

    #The sql code below checks for tables in the credentials database

    cursor.execute("""SELECT table_name 
    FROM information_schema.tables
    WHERE table_schema = "credentials"
    AND table_name = 'userdata';""")

    data = cursor.fetchone()

    #If table doesnt exist it create the userdata table

    if not data:
        cursor.execute(
            "CREATE TABLE userdata(username VARCHAR(25), password VARCHAR(100), name VARCHAR(200), email VARCHAR(200))")

        db.commit()

    else:
        pass
except Exception as e:
    print("Error: "+e)

    #The submit_login function checks for the username and encoded password in the mysql database and grants access accordingly
def submit_login():
    try:
        usr_1 = str(usrnmae).strip()
        passwd_1 = str(passwd).strip()
        passwd_11 = codecs.encode(passwd_1, 'rot_13')
        query3 = """SELECT username, password FROM userdata
                    where username = %s
                    and password = %s;"""
        cursor.execute(query3, (usr_1, passwd_11))
        result = cursor.fetchone()
        if result:
            print("Access Granted")
        else:
            print("Access Denied")

        return
    except Exception as e:
        print("Error: "+e)
    return
#The forgot_pssword function checks for username and email address in
# the sql db and if it exists and OTP is sent to the email
def forgot_pssword():
    try:
        global rand_num, usrname
        usrname = str(usr_21).strip()
        mail = str(email_add).strip()
        rand_num = ""
        for i in range(6):
            rand_num += str(random.randint(0, 9))

        query3 = """SELECT username, email FROM userdata
                    where username = %s
                    and email = %s;"""
        cursor.execute(query3, (usrname, mail))
        result = cursor.fetchone()
        if result:
            email_sender = 'Your_email_address'
            email_password = 'app_specific_password'

            email_reciever = mail
            subject = 'Reset your password'
            email = EmailMessage()
            email['From'] = email_sender
            email['to'] = email_reciever
            email['Subject'] = subject
            email.set_content("Your OTP is: " + rand_num)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, email.as_string())
            recognition()
        else:
            print("User does not exists in database")
    except Exception as e:
        print("Error: "+e)
    return

# The recognition function gets the OTP code entered by the user
def recognition():

    global new_pass58

    new_pass58 = input("Enter the code: ")

    codemit()
    return 
# If the code entered and the OTP code are the same the change_psswd function is assigned
def codemit():
    new_pas_get = str(new_pass58).strip()
    if new_pas_get == str(rand_num):

        change_psswd()
    else:

        print("INCORRECT CODE")

    return

# The change_psswd function gets user input for their new password and asks to re-enter it
def change_psswd():
    global new_pass, re_passwd

    new_pass = input("Enter New Password : ")

    # By uncommenting the lines of code below you will enable getpass that hides the users password when typing

    #user = getpass.getuser()
    #re_passwd = getpass.getpass("Re-Enter Password : %s" %user)

    # If you are uncommenting the lines above please comment the line of code below

    re_passwd = input("Re-Enter Password : ")

    passwd_submit()

    return

# The passwd_submit function checks if both passwords entered in
# change_psswd() match and updates the sql db if it does
def passwd_submit():
    try:
        changing_passwd = str(new_pass).strip()
        reset_paswd = str(re_passwd).strip()
        if changing_passwd == reset_paswd:
            passwd_45 = codecs.encode(changing_passwd, 'rot_13')
            query4 = """UPDATE userdata
                        SET password = %s
                        WHERE username = %s;"""
            cursor.execute(query4, (passwd_45, usrname))
            db.commit()
            result = cursor.rowcount
            if result > 0:

                print("Password has been changed")

            else:
                print("Error, Try again later")
        else:

            print("Passwords do not match")
    except Exception as e:
        print("Error: "+e)
    return

# The submit_signup checks the sql db if the username already exists if not it
# adds the username,password,name and email to the sql db
def submit_signup():
    try:
        eml = str(email).strip()
        name_2 = str(name).strip()
        passwd_2 = str(paswd).strip()

        passwd_12 = codecs.encode(passwd_2, 'rot_13')

        usr_2 = str(usrnmae_1).strip()

        query1 = """SELECT username from userdata
                    where username = %s"""
        cursor.execute(query1, (usr_2,))

        result = cursor.fetchone()

        if result:

            print("Username Already Exists")

        else:

            query2 = """INSERT INTO userdata(username,password,name,email)
                        VALUES(%s,%s,%s,%s)"""
            cursor.execute(query2, (usr_2, passwd_12, name_2, eml))
            db.commit()

            print("Account Created Successfully")
    except Exception as e:
        print("Error: "+e)
    return

# The login function gets user input for their username and password
def login():
    global usrnmae, passwd

    usrnmae = input("Username: ")

    print("Type '1' if you forgot your password")

    #By uncommenting the lines of code below you will enable getpass that hides the users password when typing

    #user = getpass.getuser()
    #passwd = getpass.getpass("Password: %s"%user)

    # If you are uncommenting the lines above please comment the line of code below

    passwd = input("Password: ")
    if passwd == '1':
        forgot_password()
    else:
        submit_login()

    return

#The signup function gets user input for their email address,name,password and username
def signup():
    global email, name, paswd, usrnmae_1

    email = input("Email Address : ")

    name = input("Full Name : ")

    paswd = input("Create Password : ")

    usrnmae_1 = input("Create Username : ")

    submit_signup()
    return

#The forgot_password function gets user input for their email address and username
def forgot_password():
    global email_add, usr_21

    email_add = input("Enter email address : ")

    usr_21 = input("Enter Username : ")

    forgot_pssword()
    return
# Main method to instantiate the process
if __name__ == '__main__':
    while True:
        print("1) Login")
        print("2) SignUp")
        result = input((" Enter 1 or 2: "))
        match result:
            case "1":
                login()
            case "2":
                signup()
            case _:
                print("Not recognized! Enter '1' or '2'")
        break
