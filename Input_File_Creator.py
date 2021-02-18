from tkinter import messagebox #For MessageBox
from tkinter import * #Importing Other Tkinter Modules
import tkinter as tk #Importing TK
from tkinter import ttk #This is basically for better UI
from tkinter.ttk import * #For Progress Bar (Added 15022021)
import datetime as dt # For the Dates Inputed
import os #For Opening the file
from csv import DictWriter #For Writing as headers and rows 
import time


#Setting up Plate & Size
#creating Main window
win = tk.Tk()#mainwindow
win.title("Lead File Generator")#mainwindow
#Setting Window Size
win.geometry('480x200') #mainwindow
win.resizable(width=False,height=False) #mainwindow
#END of Details    
#GUI Image
win.iconbitmap('D:\GitHub.io\Lead_File_Generator\logo.ico')
#END of Details




#Labelling of the frames
#Date:Label
date_var=str(dt.date.today())
dt_label=ttk.Label(win,text= "Date at Time of Entry :").grid(row=1, column= 0, sticky = tk.W)
date_label=ttk.Label(win,text=dt.datetime.now()).grid(row=1, column= 1, sticky = tk.W)

#Name: Label
name_label = ttk.Label(win,text = "Enter Client's Name: ")
name_label.grid(row = 2, column = 0,sticky = tk.W)

#PhoneNumber: Label
num_label = ttk.Label(win,text = "Enter Client's Phone Number: ")
num_label.grid(row = 4, column = 0,sticky = tk.W)

#Email: Label
email_label = ttk.Label(win,text = "Enter Client's Email id: ")
email_label.grid(row = 6, column = 0, sticky = tk.W)

#Lead : Label
lead_label = ttk.Label(win,text = "Lead Type sourced under:")
lead_label.grid(row = 8, column = 0,sticky = tk.W)

#Select File type : Label
file_type_Label = ttk.Label(win,text = 'Select the type of lead: ')
file_type_Label.grid(row = 10,column = 0,sticky = tk.W)

#Select Date of Follow up : Label
followup_Label = ttk.Label(win,text = ' Date for Follow up: ')
followup_Label.grid(row = 14,column = 0,sticky = tk.W)

#END of Details

#Buttoning them Up--[DATA BOX]
#Button 01: Name
name_var=tk.StringVar()
name_entrybox = ttk.Entry(win,width = 23,textvariable =name_var)
name_entrybox.grid(row =2,column=1,sticky = tk.W)
name_entrybox.focus()

#Button 02: PhoneNumber
num_var = tk.IntVar()
num_entrybox = ttk.Entry(win,width = 23, textvariable =num_var)
num_entrybox.grid(row =4, column =1,sticky = tk.W)

#Button 03: Email
email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width = 23, textvariable = email_var)
email_entrybox.grid(row=6,column=1,sticky =tk.W)

#Combobutton :Lead Type
lead_var = tk.StringVar()
lead_entrybox = ttk.Combobox(win,width =20,textvariable = lead_var,state = 'readonly')
lead_entrybox['values'] = ('Sourcing Via','DSA','Reference','Self Sourced')
lead_entrybox.current(0)
lead_entrybox.grid(row = 8, column = 1,sticky = tk.W)

#Combo Button: File type save selection
file_type = tk.StringVar()
file_entrybox = ttk.Combobox(win,width = 20,textvariable = file_type,state = 'readonly')
file_entrybox['values'] = ('Select the file type','Home Loan','LAP','SME','Balance Transfer','Re-Finance','Plot','Self-Construction')
file_entrybox.current(0)
file_entrybox.grid(row = 10,column = 1,sticky = tk.W)

#Check button for subscription
checkbtn_var= tk.IntVar()
checkbtn =ttk.Checkbutton(win,text="Select if the customer wants to be followed up: ",var = checkbtn_var)
checkbtn.grid(row=12,columnspan=4,sticky = tk.W)

##Date button for follow up
date_btn_var = tk.StringVar()
date_btn = ttk.Entry(win,width = 23,textvariable = date_btn_var)
date_btn.grid(row = 14,column = 1,sticky = tk.W)
#END of Details

#Parseing Display Field for value
disp=len(str(num_var.get()))
disp_error = tk.Label(win,text=disp,width="2",bd="0",justify = "center",fg="white",bg='black').grid(row =4, column =2,sticky = tk.W)

def disp_val():
    try:
        disp=len(str(num_var.get()))
        disp_error = tk.Label(win,text=disp,width="2",bd="0",justify="center",fg="white",bg='black').grid(row =4,column =2,sticky = tk.W)
    except:
        messagebox.showinfo("Input Error", " Number cannot be blank")
disp_error_btn = ttk.Button(win,width=22,text="Check Digits Entered:",command=disp_val).grid(row =16, column =1,sticky = tk.W)

#DEFINING THE ACTION ON PRESSING SUBMIT 

#printing the file to terminal
def action():
    userName = name_var.get()   #Calling Name
    try:
        userNumber = num_var.get() #Ensuring Number is not Blank
    except:
        messagebox.showinfo("Input Error", " Number cannot Non number") #Message pop up
    userEmail = email_var.get() #Retriving Email ID
    userLead = lead_var.get()#Retriving Lead sourced from
    userFile = file_type.get()#Retriving File Type
    userDate = date_btn_var.get() #Retriving Follow up date
    if checkbtn_var.get()==1: #Checkbox 
        followup = 'Yes'
    else:
        followup = 'No'
    try:
        print(userName,userNumber,userEmail,userLead,userFile,followup,userDate)
    except:
        return action           
  
   #printing to file
    with open(date_var+"__Lead Generated"+" .csv",'a',newline='') as f:
            #Writing Headers         
            headers = ['Date Log','Client Name','Client Number','Client Email','File Type','Sourced Via','Follow Up','callback on']
            writer = DictWriter (f,fieldnames=headers)
            if os.stat(date_var+"__Lead Generated"+" .csv").st_size==0:
                    writer.writeheader()
            #Writing Rows
            writer.writerow({'Date Log':date_var,"Client Name":userName,"Client Number":userNumber,"Client Email":userEmail,"File Type":userFile,"Sourced Via":userLead,"Follow Up":followup,"callback on":userDate })
        
 
        #def delete():
            name_entrybox.delete(0,tk.END)
            num_entrybox.delete(0,tk.END)
            email_entrybox.delete(0,tk.END)
            date_btn.delete(0,tk.END)
            #END of Details

#Finally
#SUBMIT BUTTON & CLEAR BUTTON
submit = ttk.Button(win,text="Submit",command = action)
submit.grid(row=16,column=0,sticky = tk.W)

#Extrasss
def information():
     #Setting up Introduction
    #Creating Author's Informations
    messagebox.showinfo("Author's Info","""Author's Name:Gautam Walve \nFile Name: Lead File Generator \nPublising Month: February 2021 \nVersion:1.3 \nUpdate Logs: 
>>Added Publishing Information  \n>>Moved 'Check Digits Entered' Button  to Bottom of the screen  \n Minor Error Fixed """)
   # root = tk.Tk()
    #root.overrideredirect(True)
    #info = ttk.Label(win,text="hiee" )
    #info.grid(row=1,column=0)
    #root.after(3000,root.destroy)

info = ttk.Button(win,text = "Updates",command = information)
info.grid(row =1,column = 2)





#END of Details
win.mainloop()