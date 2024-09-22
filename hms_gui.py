import customtkinter as ctk 
import tkinter as tk
#from viewpage import ViewPage
from tkinter import messagebox
from time import strftime


class BookAppointment:
    def __init__(self):
        self.screen = ctk.CTk()
        self.screen.geometry("1000x1000")
        self.screen.resizable(True,True)
        self.screen.configure(fg_color = "#ffffff")

        self.top_frame = ctk.CTkFrame(self.screen,height = 100,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.top_frame.pack(side = "top",padx = 20,pady = 20,fill = "x")

        self.title_label = ctk.CTkLabel(self.top_frame,text = "PATIENT  APPOINTMENT  BOOKING",height = 20,width = 80,fg_color = "#B8B8B8",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 30))
        self.title_label.place(x = 400,y = 40)

        self.bottom_frame = ctk.CTkFrame(self.screen,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.bottom_frame.pack(side = "top",padx = 20,pady = 20,fill = "both",expand = True)

        self.name_label = ctk.CTkLabel(self.bottom_frame,text = "NAME",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.name_label.pack(anchor = "nw",padx = 30,pady = (30,8))
        
        self.name_variable = tk.StringVar()
        self.name_entry = ctk.CTkEntry(self.bottom_frame,height = 50,textvariable = self.name_variable,width = 600,corner_radius = 15,fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont("normal",15),placeholder_text = "Enter Patient's Name:",placeholder_text_color = "#000000")
        self.name_entry.pack(anchor = "nw",padx = 30)

        self.doctor_and_time_frame = ctk.CTkFrame(self.bottom_frame,height = 50,fg_color = "#B8B8B8")
        self.doctor_and_time_frame.pack(anchor = "nw",padx = 30,pady = (50,8),fill = "x")

        self.doctor_label = ctk.CTkLabel(self.doctor_and_time_frame,text = "CONSULTED  DOCTOR",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.doctor_label.pack(side = "left")

        self.entry_frame = ctk.CTkFrame(self.bottom_frame,height = 50,fg_color = "#B8B8B8")
        self.entry_frame.pack(anchor = "nw",padx = 30,fill = "x")

        self.consulted_doctor_variable = tk.StringVar()
        self.consulted_doctor_variable.set("Select Doctor")
        self.select_dropdown = ctk.CTkOptionMenu(self.entry_frame,height = 50,width = 160,corner_radius = 15,fg_color = "#ffffff",variable = self.consulted_doctor_variable,button_color = "lightgray",button_hover_color = "gray",dropdown_hover_color = "lightblue",text_color = "#000000",font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dropdown_font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dynamic_resizing = True,values = ["Cardiologist : Dr.Satish Gupta","Neurologist : Dr.Raj Sharma","Anesthesiologist : Dr.Vinod Thakur","Pediatrician : Dr.Ankush Mehta","Dermatologist : Dr.Krishna Sen"])
        self.select_dropdown.pack(side = "left")

        self.time_label = ctk.CTkLabel(self.doctor_and_time_frame,text = "TIMING",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.time_label.pack(side = "right",padx = (0,650))

        self.time_variable = tk.StringVar()
        self.time_variable.set("Choose Timing")
        self.time_entry = ctk.CTkOptionMenu(self.entry_frame,height = 50,width = 160,corner_radius = 15,fg_color = "#ffffff",variable = self.time_variable,button_color = "lightgray",button_hover_color = "gray",dropdown_hover_color = "lightblue",text_color = "#000000",font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dropdown_font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dynamic_resizing = False,values = ["12:00 pm","1:30 pm","3:30 pm","5:00 pm"])
        self.time_entry.pack(side = "right",padx = (0,600))

        self.buttons_frame = ctk.CTkFrame(self.bottom_frame,fg_color = "#B8B8B8")
        self.buttons_frame.pack(anchor = "nw",padx = 30,pady = 20,fill = "both",expand = True)

        self.book_button = ctk.CTkButton(self.buttons_frame,height = 70,width = 100,corner_radius = 15,border_width = 1,fg_color = "#2EA2D7",text_color = "#000000",text = "Book Appointment",font = ctk.CTkFont(family = "Garamond",size = 17,weight = "bold"),hover_color = "#0277BD",command = self.add_appointment)
        self.book_button.pack(side = "left",padx = 0,pady = (25,0))

        self.view_button = ctk.CTkButton(self.buttons_frame,height = 70,width = 100,corner_radius = 15,border_width = 1,fg_color = "#2EA2D7",text_color = "#000000",text = "View Appointment",font = ctk.CTkFont(family = "Garamond",size = 17,weight = "bold"),hover_color = "#0277BD",command = self.view_appointment)
        self.view_button.pack(side = "right",padx = (0,700),pady = (25,0))

        self.time_label = ctk.CTkLabel(self.top_frame,font = ('Trebuchet MS',26,'bold'),text_color = "#000000",fg_color = "#ffffff",height = 50,width = 90,padx = 10,corner_radius = 20)
        self.time_label.place(x = 1000,y = 30)
        self.time1()
       

    def time1(self):
        self.string = strftime("%H-%M-%S %p")
        self.time_label.configure(text = self.string)
        self.time_label.after(1000,self.time1)
          
    
    def add_appointment(self):
        if self.name_variable.get() == "":
            messagebox.showerror(title = "Name Error",message = "Please input name:")
        if self.consulted_doctor_variable.get() == "Select Doctor":
            messagebox.showerror(title = "Error",message = "Choose Appointment Doctor:")
        if self.time_variable.get() == "Choose Timing":
            messagebox.showerror(title = "Error",message = "Choose timing:")
        else:
            name_data = self.name_variable.get()
            called_viewpage_object = ViewPage()
            called_viewpage_object.createslots(name_data)
            messagebox.showinfo(title = "Success",message = "Your Appointment Booked Successfully..!!")
        

    def view_appointment(self):
        self.screen.destroy()
        another_called_viewpage_object = ViewPage()
        another_called_viewpage_object.root.mainloop()

appointment_object = BookAppointment()
appointment_object.screen.mainloop()
