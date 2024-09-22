import customtkinter as ctk
import tkinter as tk
from PIL import Image
#from hms_gui import BookAppointment
from tkinter import messagebox

class ViewPage():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1200x1200")
        self.root.configure(fg_color = "#ffffff")
        self.root.title("Appointment details")

        self.top_frame = ctk.CTkFrame(self.root,height = 100,fg_color = "#B8B8B8")
        self.top_frame.pack(side = "top",fill = "x")
        
        self.back_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\admin\Academic Year 24-25\Data Strucutre\DataStructureProject\back.png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.top_frame,height = 20,text = "",image = self.back_image,width = 30,corner_radius = 15,fg_color = "#B8B8B8",hover_color = "#FFA2A3",command = self.back_command)
        self.back_button.pack(side = "left",padx = 30,pady = 20)

        self.schedule_label = ctk.CTkLabel(self.top_frame,text = "SCHEDULED APPOINTMENTS",text_color = "#000000",font = ctk.CTkFont(family = "Tahoma",size = 25,weight = "bold"))
        self.schedule_label.pack(side = "right",padx = (0,470),pady = 20)

        self.bottom_frame1 = ctk.CTkFrame(self.root,fg_color = "#B8B8B8")
        self.bottom_frame1.pack(fill = "both",expand = True)

        #self.side_frame = ctk.CTkFrame(self.bottom_frame1,width = 200,fg_color = "#B8B8B8")
        #self.side_frame.pack(side = "right",fill = "y")

        self.appointment_frame = ctk.CTkFrame(self.bottom_frame1,corner_radius = 10,border_width = 1,border_color = "gray",fg_color = "#ffffff")
        self.appointment_frame.pack(fill = "both",expand = True,padx = 30,pady = (0,20))

        self.show_appointment_label = ctk.CTkLabel(self.appointment_frame,text = "Appointments",text_color = "#000000",font = ctk.CTkFont(family = "Fantasy",size = 25,weight = "bold"))
        self.show_appointment_label.pack(anchor = "nw",padx = 10,pady = 10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.appointment_frame,corner_radius = 15,border_width = 1,border_color = "darkgray",fg_color = "#ffffff",scrollbar_button_color = "lightgray",scrollbar_button_hover_color = "darkgray",orientation = "vertical")
        self.scrollable_frame.pack(anchor = "nw",fill = "both",expand = True,padx = 30,pady = (5,30))

        self.queue_no_label = ctk.CTkLabel(self.scrollable_frame,text = "QUEUE NO",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.queue_no_label.grid(row = 0,column = 0,sticky = "nw",padx = 10,pady = 10)

        self.patient_name = ctk.CTkLabel(self.scrollable_frame,text = "PATIENT NAME",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.patient_name.grid(row = 0,column = 1,padx = 130,pady = 10)

        self.doctor_name = ctk.CTkLabel(self.scrollable_frame,text = "DOCTOR NAME",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.doctor_name.grid(row = 0,column = 2,padx = 100,pady = 10)

        self.status = ctk.CTkLabel(self.scrollable_frame,text = "STATUS",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.status.grid(row = 0,column = 3,padx = 100,pady = 10)

    def back_command(self):
        self.root.destroy()

    def createslots(self,queue_no,patient_nm,doctor_nm):
        self.label_slot = ctk.CTkLabel(self.scrollable_frame,height = 35,corner_radius = 15,fg_color = "lightgray")
        self.label_slot.grid(row = 0,column = 1,fill = "x",padx = 20,pady = 10)
        
viewpage_object = ViewPage()
viewpage_object.root.mainloop()