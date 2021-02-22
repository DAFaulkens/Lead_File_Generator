from tkinter import messagebox #For MessageBox
from tkinter import * #Importing Other Tkinter Modules
import tkinter as tk #Importing TK
from tkinter import ttk #This is basically for better UI
from tkinter.ttk import * #For Progress Bar (Added 15022021)
import datetime as dt # For the Dates Inputed
import os #For Opening the file
from csv import DictWriter #For Writing as headers and rows 
import time
import smtplib
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Setting up Plate & Size    
#creating Main window
win = tk.Tk()#mainwindow
win.title("Lead File Generator")#mainwindow

#Setting Window Size
win.geometry('360x230') #mainwindow
win.resizable(width=False,height=False) #mainwindow

##Tabbing Details 
tab_parent = ttk.Notebook(win)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2=ttk.Frame(tab_parent)
tab_parent.add(tab0,text = 'Information')
tab_parent.add(tab1,text = 'Leads Generated')
tab_parent.add(tab2,text = 'Loan Calculator')
tab_parent.grid()
#END of Details    

#GUI Image
win.iconbitmap('D:\GitHub.io\Lead_File_Generator\logo.ico')
#END of Details

#Labelling of the frames
#Date:Label
date_var=str(dt.date.today())
dt_label=ttk.Label(tab1,text= "Date at Time of Entry :").grid(row=1, column= 0, sticky = tk.W)
date_label=ttk.Label(tab1,text=dt.datetime.now()).grid(row=1, column= 1, sticky = tk.W)

#Name: Label
name_label = ttk.Label(tab1,text = "Enter Client's Name: ")
name_label.grid(row = 2, column = 0,sticky = tk.W)

#PhoneNumber: Label
num_label = ttk.Label(tab1,text = "Enter Client's Phone Number: ")
num_label.grid(row = 4, column = 0,sticky = tk.W)

#Email: Label
email_label = ttk.Label(tab1,text = "Enter Client's Email id: ")
email_label.grid(row = 6, column = 0, sticky = tk.W)

#Lead : Label
lead_label = ttk.Label(tab1,text = "Lead Type sourced under:")
lead_label.grid(row = 8, column = 0,sticky = tk.W)

#Select File type : Label
file_type_Label = ttk.Label(tab1,text = 'Select the type of lead: ')
file_type_Label.grid(row = 10,column = 0,sticky = tk.W)

#Select Date of Follow up : Label
followup_Label = ttk.Label(tab1,text = ' Date for Follow up: ')
followup_Label.grid(row = 14,column = 0,sticky = tk.W)

#END of Details

#Buttoning them Up--[DATA BOX]
#Button 01: Name
name_var=tk.StringVar()
name_entrybox = ttk.Entry(tab1,width = 23,textvariable =name_var)
name_entrybox.grid(row =2,column=1,sticky = tk.W)
name_entrybox.focus()

#Button 02: PhoneNumber
num_var = tk.IntVar(value=0)
num_entrybox = ttk.Entry(tab1,width = 23, textvariable =num_var)
num_entrybox.grid(row =4, column =1,sticky = tk.W)

#Button 03: Email
email_var = tk.StringVar()
email_entrybox = ttk.Entry(tab1,width = 23, textvariable = email_var)
email_entrybox.grid(row=6,column=1,sticky =tk.W)

#Combobutton :Lead Type
lead_var = tk.StringVar()
lead_entrybox = ttk.Combobox(tab1,width =20,textvariable = lead_var,state = 'readonly')
lead_entrybox['values'] = ('Sourcing Via','DSA','Reference','Self Sourced')
lead_entrybox.current(0)
lead_entrybox.grid(row = 8, column = 1,sticky = tk.W)

#Combo Button: File type save selection
file_type = tk.StringVar()
file_entrybox = ttk.Combobox(tab1,width = 20,textvariable = file_type,state = 'readonly')
file_entrybox['values'] = ('Select the file type','Home Loan','LAP','SME','Balance Transfer','Re-Finance','Plot','Self-Construction')
file_entrybox.current(0)
file_entrybox.grid(row = 10,column = 1,sticky = tk.W)

#Check button for subscription
checkbtn_var= tk.IntVar()
checkbtn =ttk.Checkbutton(tab1,text="Select if the customer wants to be followed up: ",var = checkbtn_var)
checkbtn.grid(row=12,columnspan=4,sticky = tk.W)

##Date button for follow up
date_btn_var = tk.StringVar()
date_btn = ttk.Entry(tab1,width = 23,textvariable = date_btn_var)
date_btn.grid(row = 14,column = 1,sticky = tk.W)
#END of Details

#Parseing Display Field for value
disp=len(str(num_var.get()))
disp_error = tk.Label(tab1,text=disp,width="2",bd="0",justify = "center",fg="white",bg='black').grid(row =4, column =2,sticky = tk.W)

def disp_val():
    try:
        disp=len(str(num_var.get()))
        disp_error = tk.Label(tab1,text=disp,width="2",bd="0",justify="center",fg="white",bg='black').grid(row =4,column =2,sticky = tk.W)
        tab1.after(100,disp_val)
    except:
        return tab1.after(100,disp_val)
disp_val()
#disp_error_btn = ttk.Button(tab1,width=22,text="Check Digits Entered:",command=disp_val).grid(row =16, column =1,sticky = tk.W)

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
submit = ttk.Button(tab1,text="Submit",command = action)
submit.grid(row=16,column=0,sticky = tk.W)


#Extrasss
#Authors information
#def information():
#     #Setting up Introduction
#    #Creating Author's Informations
info = ttk.Label(tab0,text = """Author's Name:Gautam Walve \nFile Name: Lead File Generator \nPublising Month: February 2021 \nVersion:1.4 \nUpdate Logs: 
>> Tabs Added for extra Functionalities
>> Tab Added to calculate Loan Eligibility
>> Added auto Update of Digits entered for Numbers
>> Removed Updater for DIgits Entered
>> Message Box Information now displayed in Tab""")

info.grid(row =1,column = 2)




#LTV Calculator
import math
#loan Required & LTV just to Show
#LTV
loan_req = IntVar()
    #Label
loan_req_lbl = ttk.Label(tab2,text= "Loan Required: ")
loan_req_lbl.grid(row=1, column =0,sticky=tk.W)
    #Entrybox
loan_req_entry=ttk.Entry(tab2,width=23,textvariable = loan_req)
loan_req_entry.grid(row=1,column=1,sticky=tk.W)

#LTV
ltv_req = IntVar()
    #Label
ltv_req_lbl = ttk.Label(tab2,text= "Maximum LTV: (%)")
ltv_req_lbl.grid(row=2, column =0,sticky=tk.W)
    #Entrybox
ltv_req_entry=ttk.Entry(tab2,width=10,textvariable = ltv_req)
ltv_req_entry.grid(row=2,column=1,sticky=tk.W)
    
    #Loan Eligible 
    #Label
ltv_req_lbl = ttk.Label(tab2,text= "Maximum Loan: (Amount)")
ltv_req_lbl.grid(row=3, column =0,sticky=tk.W)

def ltv():
    try:
        loan_ltv_entry=ttk.Label(tab2,width=20,text=int((ltv_req.get()/100)*loan_req.get()))
        loan_ltv_entry.grid(row=3,column=1,sticky=tk.W)
        tab2.after(100,ltv)
        
    except:
        tab2.after(100,ltv)
ltv()

Loaned = IntVar()
    #Label
loan_req_lbl = ttk.Label(tab2,text= "Net Monthly Income: ")
loan_req_lbl.grid(row=4, column =0,sticky=tk.W)
    #Entrybox
loan_req_entry=ttk.Entry(tab2,width=23,textvariable = Loaned)
loan_req_entry.grid(row=4,column=1,sticky=tk.W)

#Rate of Interest
roi = IntVar()
    #Label
roi_lbl = ttk.Label(tab2,text= "Proposed ROI: (%) ")
roi_lbl.grid(row=5, column =0,sticky=tk.W)
    #Entrybox
roi_entry=ttk.Entry(tab2,width=23,textvariable = roi)
roi_entry.grid(row=5,column=1,sticky=tk.W)

#Tenure
tenure = IntVar()
    #Label
tenure_lbl = ttk.Label(tab2,text= "Tenure Proposed(in years): ")
tenure_lbl.grid(row=6, column =0,sticky=tk.W)
    #Entrybox
tenure_entry=ttk.Entry(tab2,width=10,textvariable = tenure)
tenure_entry.grid(row=6,column=1,sticky=tk.W)
    #Label
def mon():
    try:
        tenure_lbl2 = ttk.Label(tab2,text= (f'{(tenure.get()*12)}:months' ),width='11')
        tenure_lbl2.grid(row=6, column =1,sticky=tk.E)
        tab2.after(100,mon)
    except:
         return tab2.after(100,mon)
mon()

#Liability
deductions = IntVar()
    #Label
liability_lbl = ttk.Label(tab2,text= "Recurring Liabilities/outflow:(Amount) ")
liability_lbl.grid(row=7, column =0,sticky=tk.W)
    #Entrybox
liability_entry=ttk.Entry(tab2,width=23,textvariable = deductions)
liability_entry.grid(row=7,column=1,sticky=tk.W)

#Eligibility
eli = IntVar()
    #Label
eli_lbl = ttk.Label(tab2,text= "Loan Eligibility: ")
eli_lbl.grid(row=8, column =0,sticky=tk.W)

    #Entrybox
userIncome = Loaned.get()
userRoi = (roi.get()/100)
userTenure = (tenure.get()*12)
userLiability = deductions.get()
formula = ((userIncome*userRoi*userTenure)-userLiability)

def formulae():
    try:
        eli_txt2 = ttk.Label(tab2,text=int((Loaned.get())*((roi.get()/100))*((tenure.get()*12)) - deductions.get()),width='10' )
        eli_txt2.grid(row=8, column =1,sticky=tk.W)
        tab2.after(100,formulae)
    except:
        tab2.after(100,formulae)
formulae()

#END of Details
win.mainloop()