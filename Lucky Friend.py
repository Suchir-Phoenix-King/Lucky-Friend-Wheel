# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:10:19 2022

@author: PC_RC
"""

from tkinter import * 
import random

root=Tk()

root.title("Lucky Friend Wheel")
root.geometry("500x500")
root.configure(background="lightgreen")



list1 = ["Ishaan Patil", "Vasuki", "Darshith", "Samanyu", "Pranav AV", "Deeno"]
friend = Label(root)
print(list1)


def random_number():
    random_no = random.randint(0, 5)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your Lucky Friend Is" + random_lucky_friend)
    friend["text"] = random_lucky_friend
    
    
btn1 = Button(root)
btn1 = Button(root, text=" Who is your lucky friend? ", command = random_number)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
friend.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()