import customtkinter as ctk
import tkinter as tk
from tkinter.messagebox import showerror,showinfo,showwarning

class initial_screen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Start Screen")
        self.geometry("800x800")
        #self.attributes("-fullscreen",True)

        self.start_screen()

    def start_screen(self):
        self.configure(fg_color = "#ffffff")

        self.top_label = ctk.CTkLabel(self,height = 100,text = "HMS APPOINTMENT BOOKING",fg_color = "#B8B8B8",text_color = "#000000",font = ctk.CTkFont(family = "Helvetica",size = 30,weight = "bold"))
        self.top_label.pack(side = "top",fill = "x")

        self.buttons_frame = ctk.CTkFrame(self,height = 500,fg_color = "#ffffff")
        self.buttons_frame.pack(fill = "x",pady = 100)

        self.appointments_button = ctk.CTkButton(self.buttons_frame,text = "Appointments",text_color = "#000000",fg_color = "#2aa1c9",hover_color = "#a5e0e6",height = 100,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"))
        self.appointments_button.pack(side = "left",padx = 300)

        self.new_button = ctk.CTkButton(self.buttons_frame,text = "New",text_color = "#000000",fg_color = "#2aa1c9",hover_color = "#a5e0e6",height = 100,width = 200,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"))
        self.new_button.pack(side = "right",padx = (80,400))
        

if __name__ == "__main__":
    app1 = initial_screen()
    app1.mainloop()