from Tsk3 import read_stuff
from Tsk3 import dict
import random
import codecs
from tkinter import *
from email.message import EmailMessage
import ssl, smtplib

def submit_login():
        read_stuff()
        usr_1 =  str(usrname_entry.get()).strip()
        passwd_1 = str(passwd_entry.get()).strip()
        passwd_11 = codecs.encode(passwd_1, 'rot_13') 
        if (usr_1,passwd_11) in dict.keys():
            window_2 = Toplevel()
            window_2.geometry('850x500')
            Access = Label(window_2,text='Access Granted ')
            Access.config(font = ('Arial', 20))
            Access.place(x=300,y=200)
        else:
            window_3 = Toplevel()
            window_3.geometry('850x500')
            Access_1 = Label(window_3,text='Access Denied ')
            Access_1.config(font = ('Arial', 20))
            Access_1.place(x=300,y=200)
        window.destroy()
        return
def forgot_pssword():
    global rand_num,usrname,mail
    rand_num = ""
    for i in range(6):
        rand_num += str(random.randint(0,9))
    dict_3 = {}
    usrname = str(usr2_entry.get()).strip()
    mail = str(email_entry.get()).strip()
    with open('saving_ps.txt', 'r') as f:
        for line in f:
            if len(line.split()) == 0:
                continue
            usr, pswd, name1, gmail = line.strip().split(':')
            dict_3[usr, gmail] = pswd, name1
    if (usrname, mail) in dict_3.keys(): 
        email_sender = 'sreekuttankzm@gmail.com'
        email_password = 'zwqg nnjp xztt mamu'
        reciever = str(email_entry.get()).strip()
        email_reciever = reciever
        subject = 'Reset your password'
        email = EmailMessage()
        email['From'] = email_sender
        email['to'] = email_reciever
        email['Subject'] = subject
        email.set_content("Your OTP is: "+ rand_num)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender, email_reciever, email.as_string())
        window_44.destroy()
        recognition()
    else:
        window_44.destroy()
        win = Toplevel()
        win.geometry('850x500')
        access = Label(win,text='Access Denied')
        access.config(font = ('Arial', 20))
        access.place(x=200,y=200)
        window_44.destroy()
    return
def recognition():
    global window_58,newpas_entry58
    window_58 = Toplevel()
    window_58.geometry('850x500')
    new_pass58 = Label(window_58,text='Enter the code: ')
    new_pass58.config(font = ('Arial', 20))
    new_pass58.place(x=200,y=200)
    newpas_entry58 = Entry(window_58, width=20, borderwidth=3,)
    newpas_entry58.place(x=350, y=200)
    subission_5 = Button(window_58, text='Submit', command=codemit).place(x=350,y=260)
def codemit(): 
    new_pas_get = str(newpas_entry58.get()).strip()
    if new_pas_get == str(rand_num):
        window_58.destroy()
        change_psswd()
    else:
        window_58.destroy()
        window_59 = Toplevel()
        window_59.geometry('850x500')
        new_pass59 = Label(window_59,text='INCORRECT CODE ')
        new_pass59.config(font = ('Arial', 30))
        new_pass59.place(x=300,y=200)
    return
def change_psswd():
    global window_55,newpas_entry,repasswd_entry
    window_55 = Toplevel()
    window_55.geometry('850x500')
    new_pass = Label(window_55,text='Enter New Password : ')
    new_pass.config(font = ('Arial', 20))
    new_pass.place(x=200,y=200)
    newpas_entry = Entry(window_55, width=20, borderwidth=3,)
    newpas_entry.place(x=400, y=200)
    re_passwd = Label(window_55,text='Re-Enter Password : ')
    re_passwd.config(font = ('Arial', 20))
    re_passwd.place(x=213,y=230)
    repasswd_entry = Entry(window_55,show='*', width=20, borderwidth=3,)
    repasswd_entry.place(x=400, y=230)
    subission = Button(window_55, text='Submit', command=passwd_submit).place(x=390,y=260)
    return
def passwd_submit():
    changing_passwd = str(newpas_entry.get()).strip()
    chaning_passwd_again = str(repasswd_entry.get()).strip()
    if changing_passwd == chaning_passwd_again:
            passwd_45 = codecs.encode(changing_passwd, 'rot_13')
            with open('saving_ps.txt', 'r') as f:
                for line in f:
                    if len(line.split()) == 0:
                        continue
                    file = f.read()
            with open('saving_ps.txt', 'r') as f:
                    for line in f:
                        a, b, c ,d = line.strip().split(':')
                        if a == usrname:
                            changes = file.replace((a+':'+b+':'+c+':'+d),(a+':'+passwd_45+':'+c+':'+d))
                            with open('saving_ps.txt', 'w') as f:
                                f.write(changes)
                                f.close()
                                win_1 = Toplevel()
                                win_1.geometry('850x500')
                                new_pass = Label(win_1,text='Password has been changed')
                                new_pass.config(font = ('Arial', 20))
                                new_pass.place(x=200,y=200)
                                window_55.destroy()
                        else:
                            continue
    else:
            win_2 = Toplevel()
            win_2.geometry('850x500')
            new_pass = Label(win_2,text='Passwords do not match')
            new_pass.config(font = ('Arial', 20))
            new_pass.place(x=200,y=200)
            window_55.destroy()
def submit_signup():
        dict_1 = {}
        eml = str(emaail_entry.get()).strip()
        name_2 = str(name_entry.get()).strip()
        passwd_2 = str(passwd1_entry.get()).strip()
        passwd_12 = codecs.encode(passwd_2, 'rot_13') 
        usr_2 =  str(usrname1_entry.get()).strip()
        if '@gmail.com' not in eml:
            submit_signup()
        else:
            with open('saving_ps.txt', 'r') as f:
                for line in f:
                    if len(line.split()) == 0:
                        continue
                    usr, pswd, name1, gmail = line.strip().split(':')
                    dict_1[usr] = pswd, name1, gmail
                if (usr_2) in dict_1.keys():
                    window_5 = Toplevel()
                    window_5.geometry('850x500')
                    Access_4 = Label(window_5,text='Username already exists')
                    Access_4.config(font = ('Arial', 20))
                    Access_4.place(x=300,y=200)
                else:
                    with open('saving_ps.txt', 'a') as w:
                        w.write('\n')
                        w.write(usr_2)
                        w.write(':')
                        w.write(passwd_12)
                        w.write(':')
                        w.write(name_2)
                        w.write(':')
                        w.write(eml)
                        w.close()
                    window_4 = Toplevel()
                    window_4.geometry('850x500')
                    Access_3 = Label(window_4,text='You have successfully created an account')
                    Access_3.config(font = ('Arial', 20))
                    Access_3.place(x=300,y=200)
            window_1.destroy()
            return
def login():
    global window,usrname_entry,passwd_entry
    window = Toplevel()
    window.geometry('850x500')
    usrnmae = Label(window,text='Username: ')
    usrnmae.config(font = ('Arial', 20))
    usrnmae.place(x=300,y=200)
    usrname_entry = Entry(window, width=20, borderwidth=3,)
    usrname_entry.place(x=400, y=200)
    passwd = Label(window,text='Password : ')
    passwd.config(font = ('Arial', 20))
    passwd.place(x=300,y=230)
    passwd_entry = Entry(window, show='*', width=20, borderwidth=3,)
    passwd_entry.place(x=400, y=230)
    subission = Button(window, text='Submit', command=submit_login).place(x=390,y=260)
    forgot_pswrd = Button(window,text='forgot password',command=forgot_password).place(x=390,y=290)
    return
def signup():
    global window_1,emaail_entry,name_entry,passwd1_entry,usrname1_entry
    window_1 = Toplevel()
    window_1.geometry('850x500')
    email = Label(window_1,text='Email Address : ')
    email.config(font = ('Arial', 20))
    email.place(x=255,y=170)
    emaail_entry = Entry(window_1, width=20, borderwidth=3,)
    emaail_entry.place(x=400, y=170)
    name = Label(window_1,text='Full Name : ')
    name.config(font = ('Arial', 20))
    name.place(x=292,y=200)
    name_entry = Entry(window_1, width=20, borderwidth=3,)
    name_entry.place(x=400, y=200)
    paswd = Label(window_1, text= 'Create Password : ')
    paswd.config(font = ('Arial', 20))
    paswd.place(x=230,y=230)
    passwd1_entry = Entry(window_1, show='*', width=20, borderwidth=3,)
    passwd1_entry.place(x=400, y=230)
    usrnmae_1 = Label(window_1,text='Create Username : ')
    usrnmae_1.config(font = ('Arial', 20))
    usrnmae_1.place(x=226,y=260)
    usrname1_entry = Entry(window_1, width=20, borderwidth=3,)
    usrname1_entry.place(x=400, y=260)
    subission_1 = Button(window_1, text='Submit', command=submit_signup).place(x=390,y=290)
    return
def forgot_password():
    global window_44,email_entry,usr2_entry
    window_44 = Toplevel()
    window_44.geometry('850x500')
    email = Label(window_44,text='Enter email address : ')
    email.config(font = ('Arial', 20))
    email.place(x=205,y=200)
    email_entry = Entry(window_44, width=20, borderwidth=3,)
    email_entry.place(x=400, y=200)
    usr_2 = Label(window_44,text='Enter Username : ')
    usr_2.config(font = ('Arial', 20))
    usr_2.place(x=236,y=230)
    usr2_entry = Entry(window_44, width=20, borderwidth=3,)
    usr2_entry.place(x=400, y=230)
    subission_4 = Button(window_44, text='Submit', command=forgot_pssword).place(x=390,y=290)
    window.destroy()
if __name__ == '__main__':
    root = Tk()
    root.geometry('850x500')
    title_1= root.title('Credentials')
    button_1 = Button(root, text = 'Login',padx=30,pady=20, command=login).place(x=308,y=210)
    button_2 = Button(root, text = 'Signup',padx=27,pady=20, command=signup).place(x=435,y=210)
    root.mainloop()