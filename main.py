import customtkinter as ctk
import tkinter as tk
from tkinter.messagebox import showerror,showinfo,showwarning
from time import strftime
from PIL import Image

class AppointmentNode():
    def __init__(self, appointmentNumber, patientName, doctorName, allottedTime):
        self.appntNumber = appointmentNumber
        self.pname = patientName
        self.dname = doctorName
        self.time = allottedTime
        self.nextApt = None
        self.prevApt = None

    def showAppointment(self):
        print(f"Appt_id : {self.appntNumber}, Patient_name : {self.pname}, Doctor_name : {self.dname}, Allotted time : {self.time}", end=" -> ")

class ApptQueue():
    def __init__(self):
        self.firstAppt = None
        self.lastAppt = None
        self.appointmentNumber = 0

    def isEmpty(self):
        return self.firstAppt is None

    def appointment(self, patientName, doctorName, allottedTime):
        self.appointmentNumber += 1
        if self.isEmpty():
            newApt = AppointmentNode(self.appointmentNumber, patientName, doctorName, allottedTime)
            self.firstAppt = newApt
            self.lastAppt = newApt
        else:
            newApt = AppointmentNode(self.appointmentNumber, patientName, doctorName, allottedTime)
            newApt.prevApt = self.lastAppt
            self.lastAppt.nextApt = newApt
            self.lastAppt = newApt

    def showQueue(self):
        if self.isEmpty():
            print("Queue is Empty...")
        else:
            pointer = self.firstAppt
            while pointer is not None:
                pointer.showAppointment()
                pointer = pointer.nextApt

    def checkTimings(self, docName, timing):
        if self.isEmpty():
            showinfo("Empty Queue", "Adding the First Appointment.")
            return True   # `True` means `Timing Available`..
        else:
            pointer = self.firstAppt
            counter = 0
            while pointer is not None:
                if pointer.dname == docName and pointer.time == timing:
                    counter +=1
                    if counter == 5:
                        showinfo("Timing not available!",f"Doctor : {docName} is not available between {timing}.")
                        return False
                pointer = pointer.nextApt
            return True
        
    def removeAppt(self, apptNumber):
        pointer = self.firstAppt
        
        while pointer is not None:
            if pointer.appntNumber == apptNumber:
                break
            pointer = pointer.nextApt
        if pointer.nextApt == None and pointer.prevApt == None:
            pointer = None
        elif pointer.prevApt == None:
            pointer.nextApt.prevApt = None
            self.firstAppt = pointer.nextApt
        elif pointer.nextApt == None:
            pointer.prevApt.nextApt = None
            self.lastAppt = pointer.prevApt
        else:
            pointer.prevApt.nextApt = pointer.nextApt
            pointer.nextApt.prevApt = pointer.prevApt
        # self.showQueue() # Uncomment To Debug/Print...
        
    

                        #   ================ --------------------- ==================  #
                  # ========================== Application Starts ==============================  #
                        #   ================ --------------------- ==================  # 



class AppoinmentManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-8,-5))
        self.title("Appointment Manager")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.appointmentQueue = ApptQueue()

        self.screen_stack = []
        self.current_screen = None
        self.appointment_slots = {}

        self.startScreen()


    def time1(self):
        self.datePattern = strftime("%H-%M-%S %p")
        self.time_label.configure(text = self.datePattern)
        self.time_label.after(1000,self.time1)

    def toggle_fullscreen(self, event=None):
        # Set the application to fullscreen mode
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        # Exit fullscreen mode
        self.attributes('-fullscreen', False)
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-8,-5))
        self.resizable(True,True)

    def switch_screen(self, new_screen):
        # Save the current screen to the stack
        if self.current_screen:
            self.screen_stack.append(self.current_screen)
        # Clear the current screen
        for widget in self.winfo_children():
            widget.pack_forget()
        # Display the new screen
        self.current_screen = new_screen
        new_screen()

    def back(self):
        if self.screen_stack:
            # Clear the current screen
            for widget in self.winfo_children():
                widget.pack_forget()
            # Restore the previous screen from the stack
            self.current_screen = self.screen_stack.pop()
            self.current_screen()

    def add_appointment(self):
        if self.name_variable.get() == "":
            showerror(title = "Name Error",message = "Please input name:")
        if self.consulted_doctor_variable.get() == "Select Doctor":
            showerror(title = "Error",message = "Choose Appointment Doctor:")
        if self.time_variable.get() == "Choose Timing":
            showerror(title = "Error",message = "Choose timing:")
        else:
            checkTime = self.appointmentQueue.checkTimings(self.consulted_doctor_variable.get(),self.time_variable.get())
            if checkTime:
                self.appointmentQueue.appointment(self.name_variable.get(), self.consulted_doctor_variable.get(), self.time_variable.get())
                showinfo(title = "Success",message = "Your Appointment Booked Successfully..!!")

    def startScreen(self):
        self.switch_screen(self._startScreen)

    def _startScreen(self):
        self.configure(fg_color = "#ffffff")
        self.bind("<F11>", self.toggle_fullscreen)

        self.top_frame0 = ctk.CTkFrame(self,height = 100,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.top_frame0.pack(side = "top",padx = 20,pady = 20,fill = "x")

        self.top_label0 = ctk.CTkLabel(self.top_frame0,height = 100,text = "HMS APPOINTMENT BOOKING",text_color = "#000000",font = ctk.CTkFont(family = "Helvetica",size = 30,weight = "bold"))
        self.top_label0.pack(side = "top",fill = "x")

        self.buttons_frame0 = ctk.CTkFrame(self,height = 500,fg_color = "#ffffff")
        self.buttons_frame0.pack(fill = "x",pady = 100)

        self.appointments_button = ctk.CTkButton(self.buttons_frame0,text = "Appointments",text_color = "#000000",fg_color = "#2aa1c9",hover_color = "#a5e0e6",height = 100,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"), command=self.view_appointment)
        self.appointments_button.pack(side = "left",padx = 200)

        self.new_button = ctk.CTkButton(self.buttons_frame0,text = "New",text_color = "#000000",fg_color = "#2aa1c9",hover_color = "#a5e0e6",height = 100,width = 200,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"), command=self.newScreen)
        self.new_button.pack(side = "right",padx = (50,200))

    def newScreen(self):
        self.switch_screen(self._newScreen)

    def _newScreen(self):
        self.top_frame = ctk.CTkFrame(self,height = 100,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
        self.top_frame.pack(side = "top",padx = 20,pady = 20,fill = "x")

        self.back_image0 = ctk.CTkImage(dark_image = Image.open(r"back.png"),size = (25,25))
        self.back_button0 = ctk.CTkButton(self.top_frame,height = 20,text = "",image = self.back_image0,width = 30,corner_radius = 15,fg_color = "#B8B8B8",hover_color = "#FFA2A3",command = self.back)
        self.back_button0.pack(side = "left",padx = 30,pady = 20)

        self.title_label = ctk.CTkLabel(self.top_frame,text = "PATIENT  APPOINTMENT  BOOKING",height = 20,width = 80,fg_color = "#B8B8B8",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 30))
        self.title_label.place(x = 300,y = 20)

        self.bottom_frame = ctk.CTkFrame(self,border_width = 1,border_color = 'gray',fg_color = "#B8B8B8")
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
        self.select_dropdown = ctk.CTkOptionMenu(self.entry_frame,height = 50,width = 160,corner_radius = 15,fg_color = "#ffffff",variable = self.consulted_doctor_variable,button_color = "lightgray",button_hover_color = "gray",dropdown_hover_color = "lightblue",text_color = "#000000",font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dropdown_font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dynamic_resizing = True,values = ["Dr. Satish Gupta","Dr. Ritik Sharma","Dr. Naveen Thakur","Dr. Ankush Mehta","Dr. Krishna Sen"])
        self.select_dropdown.pack(side = "left")

        self.time_label = ctk.CTkLabel(self.doctor_and_time_frame,text = "TIMING",text_color = "#000000",fg_color = "#B8B8B8",font = ctk.CTkFont(family = "Oswald",size = 25,weight = "bold"))
        self.time_label.pack(side = "right",padx = (0,650))

        self.time_variable = tk.StringVar()
        self.time_variable.set("Choose Timing")
        self.time_entry = ctk.CTkOptionMenu(self.entry_frame,height = 50,width = 160,corner_radius = 15,fg_color = "#ffffff",variable = self.time_variable,button_color = "lightgray",button_hover_color = "gray",dropdown_hover_color = "lightblue",text_color = "#000000",font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dropdown_font = ctk.CTkFont(family = "Courier New",size = 15,weight = "normal"),dynamic_resizing = True,values = ["11:00 am - 12:00 pm", "12:00 pm - 1:00 pm", "1:00 pm - 2:00 pm","2:00 pm - 3:00 pm", "3:00 pm - 4:00 pm", "4:00 pm - 5:00 pm"])
        self.time_entry.pack(side = "right",padx = (0,600))

        self.buttons_frame = ctk.CTkFrame(self.bottom_frame,fg_color = "#B8B8B8")
        self.buttons_frame.pack(anchor = "nw",padx = 30,pady = 20,fill = "both",expand = True)

        self.book_button = ctk.CTkButton(self.buttons_frame,height = 70,width = 100,corner_radius = 15,border_width = 1,fg_color = "#2EA2D7",text_color = "#000000",text = "Book Appointment",font = ctk.CTkFont(family = "Garamond",size = 17,weight = "bold"),hover_color = "#0277BD",command = self.add_appointment)
        self.book_button.pack(side = "left",padx = 0,pady = (25,0))

        self.view_button = ctk.CTkButton(self.buttons_frame,height = 70,width = 100,corner_radius = 15,border_width = 1,fg_color = "#2EA2D7",text_color = "#000000",text = "View Appointment",font = ctk.CTkFont(family = "Garamond",size = 17,weight = "bold"),hover_color = "#0277BD",command = self.view_appointment)
        self.view_button.pack(side = "right",padx = (0,700),pady = (25,0))

        self.time_label = ctk.CTkLabel(self.top_frame,font = ('Trebuchet MS',26,'bold'),text_color = "#000000",fg_color = "#ffffff",height = 50,width = 90,padx = 10,corner_radius = 20)
        self.time_label.place(x = 1000,y = 10)
        self.time1()

    def view_appointment(self):
        self.switch_screen(self._view_appointment)

    def _view_appointment(self):
        self.top_frame2 = ctk.CTkFrame(self,height = 100,fg_color = "#B8B8B8")
        self.top_frame2.pack(side = "top",fill = "x")
        
        self.back_image = ctk.CTkImage(dark_image = Image.open(r"back.png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.top_frame2,height = 20,text = "",image = self.back_image,width = 30,corner_radius = 15,fg_color = "#B8B8B8",hover_color = "#FFA2A3",command = self.back)
        self.back_button.pack(side = "left",padx = 30,pady = 20)

        self.schedule_label = ctk.CTkLabel(self.top_frame2,text = "SCHEDULED APPOINTMENTS",text_color = "#000000",font = ctk.CTkFont(family = "Tahoma",size = 25,weight = "bold"))
        self.schedule_label.pack(side = "right",padx = (0,670),pady = 20)

        self.bottom_frame1 = ctk.CTkFrame(self,fg_color = "#B8B8B8")
        self.bottom_frame1.pack(fill = "both",expand = True)

        self.appointment_frame = ctk.CTkFrame(self.bottom_frame1,corner_radius = 10,border_width = 1,border_color = "gray",fg_color = "#ffffff")
        self.appointment_frame.pack(fill = "both",expand = True,padx = 30,pady = (0,20))

        self.show_appointment_label = ctk.CTkLabel(self.appointment_frame,text = "Appointments",text_color = "#000000",font = ctk.CTkFont(family = "Fantasy",size = 25,weight = "bold"))
        self.show_appointment_label.pack(anchor = "nw",padx = 10,pady = 10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.appointment_frame,corner_radius = 15,border_width = 1,border_color = "darkgray",fg_color = "#ffffff",scrollbar_button_color = "lightgray",scrollbar_button_hover_color = "darkgray",orientation = "vertical")
        self.scrollable_frame.pack(anchor = "nw",fill = "both",expand = True,padx = 30,pady = (5,30))

        self.top_frame3 = ctk.CTkFrame(self.scrollable_frame, height=35, corner_radius=15, fg_color="#ffffff")
        self.top_frame3.grid(row = 0,column = 0,sticky = "ew",columnspan = 4,padx = 10,pady = 5)

        self.queue_no_label = ctk.CTkLabel(self.top_frame3,text = "QUEUE NO",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.queue_no_label.grid(row = 0,column = 0,sticky = "nw",padx = 10,pady = 10)

        self.patient_name = ctk.CTkLabel(self.top_frame3,text = "PATIENT NAME",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.patient_name.grid(row = 0,column = 1,sticky = "nw",padx = (50,50),pady = 10)

        self.doctor_name = ctk.CTkLabel(self.top_frame3,text = "DOCTOR NAME",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.doctor_name.grid(row = 0,column = 2,sticky = "nw",padx = (50,30),pady = 10)

        self.timing = ctk.CTkLabel(self.top_frame3,text = "TIMING",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.timing.grid(row = 0,column = 3,sticky = "nw",padx = (110,200),pady = 10)

        self.status = ctk.CTkLabel(self.top_frame3,text = "STATUS",text_color = "#000000",font = ctk.CTkFont(family = "Luminari",size = 20,weight = "bold"))
        self.status.grid(row = 0,column = 4,padx = (0,30),pady = 10)

        pointer = self.appointmentQueue.firstAppt
        row_index = 1
        
        while pointer is not None:
            self.createslots(row_index, pointer.pname, pointer.dname, pointer.time)
            pointer = pointer.nextApt
            row_index += 1

    def createslots(self, queue_no, patient_nm, doctor_nm, timing):
        self.label_slot = ctk.CTkFrame(self.scrollable_frame, height=35, corner_radius=15, fg_color="#B8B8B8")
        self.label_slot.grid(row=queue_no, column = 0,padx = 10, pady = 10,sticky = "ew")

        self.queue_label = ctk.CTkLabel(self.label_slot, text=f"{queue_no}", text_color="#000000", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"))
        self.queue_label.grid(row=0, column=0,padx=(10,100), pady=10, sticky="w")

        self.patient_label = ctk.CTkLabel(self.label_slot, text=f"{patient_nm}", text_color="#000000", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"))
        self.patient_label.grid(row=0, column=1, padx=(100,70), pady=10,sticky = "w")

        self.doctor_label = ctk.CTkLabel(self.label_slot, text=f"{doctor_nm}", text_color="#000000",font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"))
        self.doctor_label.grid(row=0, column=2, padx = (100,50), pady=10, sticky="e")

        self.timing_label = ctk.CTkLabel(self.label_slot, text=f"{timing}", text_color="#000000",font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"))
        self.timing_label.grid(row=0, column=3, padx = (100,40), pady=10, sticky="e")

        self.checkout_button = ctk.CTkButton(self.label_slot,text=f"Checkout", text_color="#000000", fg_color="#DAF34D", corner_radius=15,hover_color = "lightgray", command= lambda que_no = queue_no : self.checkout(que_no))
        self.checkout_button.grid(row=0, column = 4,padx = (90,40), pady=10, sticky="e")

        self.appointment_slots[queue_no] = self.label_slot

    def checkout(self, appointmentNumber):
        removedApt = appointmentNumber
        self.appointmentQueue.removeAppt(int(removedApt)) # Removing the Appointment from the Queue.
        if appointmentNumber in self.appointment_slots:
            self.appointment_slots[appointmentNumber].destroy()  # Remove the frame from the GUI
            del self.appointment_slots[appointmentNumber]

if __name__ == "__main__":
    app = AppoinmentManager()
    app.mainloop()