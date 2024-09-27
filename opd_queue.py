import customtkinter as ctk
from tkinter.messagebox import showinfo,showerror,showwarning

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
                pointer.showAppointment()
                pointer = pointer.nextApt

totalAppt = int(input("Enter number of Appointments in a day : "))
appointmentQueue = ApptQueue()
i = 1
while i <= totalAppt :
    patient_name = input("Enter patient name : ")
    doctor_name = input("Enter doctor name : ")
    appointmentQueue.appointment(patient_name, doctor_name)
    print("Appointment is scheduled successfully..")
    if i <= (totalAppt-1):
        nextOption = input("Want another Appointment, If Yes then press `Y` if not then press `N` :\n")
        if nextOption.upper() == "Y":
            i += 1
        elif nextOption.upper() == "N":
            i = totalAppt + 1
        else:
            i = totalAppt + 1
            print("Process Terminated.. invalid option is pressed.")
    else:
        i = totalAppt + 1
appointmentQueue.showQueue()
