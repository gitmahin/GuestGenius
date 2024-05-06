from tkinter import *
import pandas as pd
import os

root = Tk()
root.geometry("700x650")
root.maxsize(2200, 1500)
root.minsize(700, 650)
root.title("GuestGenius")

main_frame = Frame(root)
main_frame.pack(expand=1, fill=BOTH)

Label(main_frame, text="Hotel guest data manager - GuestGenius", font="Roboto, 15 bold", fg="#6c5ce7").pack(anchor=CENTER, side=TOP, pady=10)

form_frame = Frame(main_frame, pady=20)
form_frame.pack(anchor=CENTER, side=TOP)



def resetForm():
    [widget.delete(0, END) for widget in form_frame.winfo_children() if isinstance(widget, Entry)]
    smokeVal.set("")
    familyVal.set("")
    privateBalconyVal.set("")
    personaVal.set("")
    loungeVal.set("")
    typeOfTravVal.set("Solo")
    menuVal.set("Select your travel purpose")
    genderVal.set(0)

def cancleForm():
    resetForm()
    caption.configure(text="Cancled", fg="red")


def saveGuestData():
    data = {"Name": [], "Email": [], "Phone": [], "Gender": [], "Profession": [], "Special requests": [], "Travel purpose": [], "Type of traveler": [], "Duration of stay": [] }

    data["Name"].append(nameVal.get())
    data["Email"].append(emailVal.get())
    data["Phone"].append(phoneVal.get())
    data["Gender"].append(genderVal.get())
    data["Profession"].append(professionVal.get())
    data["Special requests"].append(f"{smokeVal.get(), familyVal.get(), privateBalconyVal.get(), personaVal.get(), loungeVal.get()}")
    data["Travel purpose"].append(menuVal.get())
    data["Type of traveler"].append(typeOfTravVal.get())
    data["Duration of stay"].append(f"{stayVal.get()} days")

    isFile = os.path.isfile("data.csv")
    try:
        dataFrame = pd.DataFrame.from_dict(data)
        if(isFile):
            dataFrame.to_csv("data.csv", mode="a", index=False, header=False)
            caption.configure(text="File updated", fg="#00b894")  
            resetForm()
        else:
            dataFrame.to_csv("data.csv", mode="a", index=False, header=True)
            caption.configure(text="File created & saved", fg="#00b894")
            resetForm()
    except Exception as e:
        caption.configure(text="Something went wrong", fg="red")


# labels
Label(form_frame, text="Name:", font="Roboto 11 bold").grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Email address:", font="Roboto 11 bold").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="phone number:", font="Roboto 11 bold").grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Gender:", font="Roboto 11 bold").grid(row=3, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Profession:", font="Roboto 11 bold").grid(row=6, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Any special requests?", font="Roboto 11 bold").grid(row=7, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Travel purpose:", font="Roboto 11 bold").grid(row=10, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Type of traveler:", font="Roboto 11 bold").grid(row=11, column=0, sticky=W, padx=10, pady=5)
Label(form_frame, text="Duration of stay [In days]", font="Roboto 11 bold").grid(row=12, column=0, sticky=W, padx=10, pady=5)

# tkinter Entries variables
nameVal = StringVar()
emailVal = StringVar()
phoneVal = StringVar()
professionVal = StringVar()
stayVal = StringVar()

# Checkboxes variables
smokeVal = StringVar()
familyVal = StringVar()
privateBalconyVal = StringVar()
personaVal = StringVar()
loungeVal = StringVar()

# Options varibales
typeOfTravVal = StringVar()
typeOfTravVal.set("Solo")
menuVal = StringVar()
menuVal.set("Select your travel purpose")

# radio buttons var
genderVal = StringVar()
genderVal.set(0)

# user entries
Entry(form_frame, textvariable=nameVal, font="Roboto 11", width=30).grid(row=0, column=1, sticky=W)
Entry(form_frame, textvariable=emailVal, font="Roboto 11", width=30).grid(row=1, column=1, sticky=W)
Entry(form_frame, textvariable=phoneVal, font="Roboto 11", width=30).grid(row=2, column=1, sticky=W)
radio = Radiobutton(form_frame, text="Male", variable=genderVal, value="Male", font="Roboto 11").grid(row=3, column=1, sticky=W)
radio = Radiobutton(form_frame, text="Female", variable=genderVal, value="Female", font="Roboto 11").grid(row=4, column=1, sticky=W)
radio = Radiobutton(form_frame, text="Other", variable=genderVal, value="Other", font="Roboto 11").grid(row=5, column=1, sticky=W)
Entry(form_frame, textvariable=professionVal, font="Roboto 11", width=30).grid(row=6, column=1, sticky=W)

# Checkboxes
Checkbutton(form_frame, text= "Smoking room", activebackground="#74b9ff", font="Roboto 10", variable=smokeVal, onvalue="Smoking room", offvalue="", foreground="#0984e3").grid(row=7, column=1, sticky=W)

Checkbutton(form_frame, text="Family Suite", activebackground="#74b9ff", font="Roboto 10", variable=familyVal, onvalue="Family Suite", offvalue="", foreground="#0984e3").grid(row=7, column=2, sticky=W)

Checkbutton(form_frame, text="Private Balcony or Terrace", activebackground="#74b9ff", font="Roboto 10", variable=privateBalconyVal, onvalue="Private Balcony or Terrace", offvalue="", foreground="#0984e3").grid(row=8, column=1, sticky=W)

Checkbutton(form_frame, text="Personalized Welcome Amenities", activebackground="#74b9ff", font="Roboto 10", variable=personaVal, onvalue="Personalized Welcome Amenities", offvalue="", foreground="#0984e3").grid(row=8, column=2, sticky=W)

Checkbutton(form_frame, text="Executive Lounge Access", activebackground="#74b9ff", font="Roboto 10", variable=loungeVal, onvalue="Executive Lounge Access", offvalue="", foreground="#0984e3").grid(row=9, column=1, sticky=W)

# options
OptionMenu(form_frame, menuVal, "Business Traveler", "Leisure Traveler", "Family Vacationers", "Group Travelers", "Luxury Travelers", "Adventure Travelers", "Couples Retreat", "Wellness Travelers", "Pet-Friendly Travelers", "Extended Stay Travelers").grid(row=10, column=1, sticky=W, pady=5)

OptionMenu(form_frame, typeOfTravVal, "Solo", "group", "corporate").grid(row=11, column=1, sticky=W)

# Entry
Entry(form_frame, textvariable=stayVal, width=30).grid(row=12, column=1, sticky=W)

# submit data
Button(form_frame, text="Save", padx=30, bg="#089767", fg="black", cursor="hand2", font="Roboto 10 bold", command=saveGuestData).grid(row=13, column=2, sticky=E, pady=20)
Button(form_frame, text="Cancel", padx=30, bg="red", fg="white", cursor="hand2", font="Roboto 10", command=cancleForm).grid(row=13, column=0, sticky=W, pady=20)

# system caption
caption = Label(main_frame, pady=30, font="Roboto 10 bold")
caption.pack(side=BOTTOM, anchor=CENTER)

root.mainloop()