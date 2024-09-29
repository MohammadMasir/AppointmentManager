import customtkinter as ctk
import tkinter as tk
from tkinter.messagebox import showerror,showinfo,showwarning
from time import strftime
from PIL import Image
def checkout(self,appntNumber):
        print(appntNumber)
        print("THIS IS THE BUTTON TO SEE APPOINTMENT")
        appointmentNumber = appntNumber
        if self.appointmentQueue.isEmpty():
            showinfo("Empty Queue", "No appointments to delete.")
        else:
            pointer = self.appointmentQueue.firstAppt
            appointment_deleted = False  # Flag to track if the appointment was deleted

            while pointer is not None:
                if pointer.appntNumber == appointmentNumber:
                    if pointer == self.appointmentQueue.firstAppt:  # If it's the first appointment
                        self.appointmentQueue.firstAppt = pointer.nextApt
                        if self.appointmentQueue.firstAppt is not None:
                            self.appointmentQueue.firstAppt.prevApt = None
                        appointment_deleted = True  # Mark as deleted
                        break

                    elif pointer == self.appointmentQueue.lastAppt:  # If it's the last appointment
                        self.appointmentQueue.lastAppt = pointer.prevApt
                        if self.appointmentQueue.lastAppt is not None:
                            self.appointmentQueue.lastAppt.nextApt = None
                        appointment_deleted = True  # Mark as deleted
                        break

                    else:  # If it's in the middle
                        pointer.prevApt.nextApt = pointer.nextApt
                        pointer.nextApt.prevApt = pointer.prevApt
                        appointment_deleted = True  # Mark as deleted
                break

                pointer = pointer.nextApt

    # Show deletion success message only if the appointment was deleted
            if appointment_deleted:
                showinfo("Deleted", f"Appointment {appointmentNumber} has been deleted.")
            else:
        # If no appointment was deleted, show the "Not Found" error
                showerror("Not Found", f"Appointment number {appointmentNumber} not found.")
