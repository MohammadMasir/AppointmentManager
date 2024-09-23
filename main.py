import customtkinter as ctk
import tkinter as tk
from tkinter.messagebox import showerror,showinfo,showwarning
from time import strftime
from PIL import Image


class AppointmentNode():
    def __init__(self, patientName, doctorName):
        self.pname = patientName
        self.dname = doctorName
        self.nextApt = None
        self.appointment = [f"Patient name : {self.pname}", f"Doctor name : {self.dname}"]

    def showAppointment(self):
        print(self.appointment, end=" -> ")

class ApptQueue():
    def __init__(self):
        self.firstAppt = None
        # self.appoinments = []

    def isEmpty(self):
        return self.firstAppt is None

    def appointment(self, patientName, doctorName):
        if self.isEmpty():
            self.firstAppt = AppointmentNode(patientName, doctorName)
        else:
            current = self.firstAppt
            while current.nextApt is not None and current != None:
                current = current.nextApt

            newApt = AppointmentNode(patientName, doctorName)
            current.nextApt = newApt

    def showQueue(self):
        if self.isEmpty():
            print("Queue is Empty...")
        else:
            pointer = self.firstAppt
            while pointer != None:
                self.appts = pointer.showAppointment()
                # self.appoinments.append(pointer.appoinment)
                pointer = pointer.nextApt


                #   ================ --------------------- ==================  #
          # ========================== Application Starts ==============================  #
                #   ================ --------------------- ==================  #


class AppoinmentManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("Appointment Manager")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.initialScreen()

    def toggle_fullscreen(self, event=None):
        # Set the application to fullscreen mode
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # Exit fullscreen mode
        self.attributes('-fullscreen', False)
        # self.resizable(width=True, height=True)
        self.geometry(f'{width - 100}x{height-100}')
        self.maxsize(width,height)

    def time1(self):
        self.datePattern = strftime("%H-%M-%S %p")
        self.time_label.configure(text = self.datePattern)
        self.time_label.after(1000,self.time1)

    def initialScreen(self):
        self.toggle_fullscreen()
        self.bind("<F11>", self.toggle_fullscreen)

        self.top_frame = ctk.CTkFrame(self,height = 100,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.top_frame.pack(side = "top",padx = 20,pady = 20,fill = "x")

        self.title_label = ctk.CTkLabel(self.top_frame,text = "PATIENT  APPOINTMENT  BOOKING",height = 20,width = 80,fg_color = "#B8B8B8",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 30))
        self.title_label.place(x = 400,y = 40)

        self.bottom_frame = ctk.CTkFrame(self,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.bottom_frame.pack(side = "top",padx = 20,pady = 20,fill = "both",expand = True)

        self.name_label = ctk.CTkLabel(self.bottom_frame,text = "NAME",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.name_label.pack(anchor = "nw",padx = 30,pady = (30,8))
        
        self.name_variable = tk.StringVar() #TODO... NAME ---------------
        self.name_entry = ctk.CTkEntry(self.bottom_frame,height = 50,textvariable = self.name_variable,width = 600,corner_radius = 15,fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont("normal",15),placeholder_text = "Enter Patient's Name:",placeholder_text_color = "#000000")
        self.name_entry.pack(anchor = "nw",padx = 30)

        self.doctor_and_time_frame = ctk.CTkFrame(self.bottom_frame,height = 50,fg_color = "#B8B8B8")
        self.doctor_and_time_frame.pack(anchor = "nw",padx = 30,pady = (50,8),fill = "x")

        self.doctor_label = ctk.CTkLabel(self.doctor_and_time_frame,text = "CONSULTED  DOCTOR",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.doctor_label.pack(side = "left")

        self.entry_frame = ctk.CTkFrame(self.bottom_frame,height = 50,fg_color = "#B8B8B8")
        self.entry_frame.pack(anchor = "nw",padx = 30,fill = "x")

        self.consulted_doctor_variable = tk.StringVar()
        self.consulted_doctor_variable.set("Select Doctor") #TODO... DOCTOR NAME ---------------
        self.select_dropdown = ctk.CTkOptionMenu(self.entry_frame,height = 50,width = 160,corner_radius = 15,fg_color = "#ffffff",variable = self.consulted_doctor_variable,button_color = "lightgray",button_hover_color = "gray",dropdown_hover_color = "lightblue",text_color = "#000000",font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dropdown_font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dynamic_resizing = True,values = ["Cardiologist : Dr.Satish Gupta","Neurologist : Dr.Raj Sharma","Anesthesiologist : Dr.Vinod Thakur","Pediatrician : Dr.Ankush Mehta","Dermatologist : Dr.Krishna Sen"])
        self.select_dropdown.pack(side = "left")

        self.time_label = ctk.CTkLabel(self.doctor_and_time_frame,text = "TIMING",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.time_label.pack(side = "right",padx = (0,650))

        self.time_variable = tk.StringVar()
        self.time_variable.set("Choose Timing") #TODO... TIMING ---------------
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
    
    def add_appointment(self):
        if self.name_variable.get() == "":
            showerror(title = "Name Error",message = "Please input name:")
        if self.consulted_doctor_variable.get() == "Select Doctor":
            showerror(title = "Error",message = "Choose Appointment Doctor:")
        if self.time_variable.get() == "Choose Timing":
            showerror(title = "Error",message = "Choose timing:")
        else:
            self.appointmentQueue = ApptQueue()
            self.appointmentQueue.appointment(self.name_variable.get(), self.consulted_doctor_variable.get())
            self.appointmentQueue.showQueue()
            # name_data = self.name_variable.get()
            # called_viewpage_object = ViewPage()
            # called_viewpage_object.createslots(name_data)
            # showinfo(title = "Success",message = "Your Appointment Booked Successfully..!!")
        

    def view_appointment(self):
        pass
        self.top_frame.pack_forget()
        self.bottom_frame.pack_forget()
        self.appointmentQueue.showQueue()

        self.top_frame2 = ctk.CTkFrame(self,height = 100,fg_color = "#B8B8B8")
        self.top_frame2.pack(side = "top",fill = "x")
        
        self.back_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\user\SY Masir\Practical\Data Structure\pract\AppointmentManager\back.png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.top_frame,height = 20,text = "",image = self.back_image,width = 30,corner_radius = 15,fg_color = "#B8B8B8",hover_color = "#FFA2A3",command = self.back_command)
        self.back_button.pack(side = "left",padx = 30,pady = 20)

        self.schedule_label = ctk.CTkLabel(self.top_frame2,text = "SCHEDULED APPOINTMENTS",text_color = "#000000",font = ctk.CTkFont(family = "Tahoma",size = 25,weight = "bold"))
        self.schedule_label.pack(side = "right",padx = (0,470),pady = 20)

        self.bottom_frame1 = ctk.CTkFrame(self,fg_color = "#B8B8B8")
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

        # labelinfo = ctk.CTkLabel(self.scrollable_frame, text=self.appointmentQueue.appts, text_color="black", font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        # labelinfo.grid(row = 1,column = 0,padx = 100,pady = 10)

    def back_command(self):
        pass

    def createslots(self,queue_no,patient_nm,doctor_nm):
        self.label_slot = ctk.CTkLabel(self.scrollable_frame,height = 35,corner_radius = 15,fg_color = "lightgray")
        self.label_slot.grid(row = 0,column = 1,fill = "x",padx = 20,pady = 10)


if __name__ == "__main__":
    app = AppoinmentManager()
    app.mainloop()