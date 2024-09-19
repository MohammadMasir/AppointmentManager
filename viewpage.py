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
        
        self.back_image = ctk.CTkImage(dark_image = Image.open("C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\PYTHON OOPS\\back.png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.top_frame,height = 20,text = "",image = self.back_image,width = 30,corner_radius = 15,fg_color = "#B8B8B8",hover_color = "#FFA2A3",command = self.back_command)
        self.back_button.pack(side = "left",padx = 30,pady = 20)

        self.schedule_label = ctk.CTkLabel(self.top_frame,text = "SCHEDULED APPOINTMENTS",text_color = "#000000",font = ctk.CTkFont(family = "Tahoma",size = 25,weight = "bold"))
        self.schedule_label.pack(side = "right",padx = (0,470),pady = 20)

        self.bottom_frame1 = ctk.CTkFrame(self.root,fg_color = "#B8B8B8")
        self.bottom_frame1.pack(fill = "both",expand = True)

        self.side_frame = ctk.CTkFrame(self.bottom_frame1,width = 200,fg_color = "#B8B8B8")
        self.side_frame.pack(side = "right",fill = "y")

        self.scrollable_frame = ctk.CTkScrollableFrame(self.bottom_frame1,corner_radius = 10,border_width = 1,border_color = "gray",fg_color = "#ffffff",scrollbar_button_color = "lightgray",scrollbar_button_hover_color = "darkgray",orientation = "vertical")
        self.scrollable_frame.pack(side = "left",fill = "both",expand = True)

    def back_command(self):
        self.root.destroy()

    def createslots(self,data):
        self.appointment_label = ctk.CTkLabel(self.scrollable_frame,height = 100,text = data,corner_radius = 15,fg_color = "#C8C8C8",text_color = "#000000",font = ctk.CTkFont(family = "Menlo",size = 20,weight = "bold"))
        self.appointment_label.pack(side = "top",fill = "x",padx = 10,pady = 10)

        
viewpage_object = ViewPage()
viewpage_object.root.mainloop()