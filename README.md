# Hospital Management System - Appointment Manager

## Overview
This project is a **Hospital Management System (HMS) Appointment Manager** built using **CustomTkinter** (a modern tkinter framework) and **PIL** (Python Imaging Library). It enables hospitals or clinics to manage patient appointments effectively, allowing users to book, view, and manage appointments. The program also checks for appointment availability for doctors and specific time slots.

## Features
- **Appointment Queue Management:** The system maintains a queue of patient appointments, ensuring that no doctor has more than a set number of appointments in a given time slot
- **GUI using CustomTkinter:** The application has an easy-to-use graphical user interface, with features like:
  - Full-screen mode
  - Back navigation
  - Interactive buttons
- **Appointment Booking:** Patients can book appointments by selecting the doctor, time slot, and providing their name
- **View Scheduled Appointments:** Users can view all scheduled appointments in a scrollable list
- **Appointment Removal:** Appointments can be removed from the queue

## Prerequisites
- **Python 3.x:** Make sure Python 3.x is installed on your system
- **Required Libraries:**
  - customtkinter
  - tkinter
  - PIL (Python Imaging Library)

You can install the required libraries via pip:
```bash
pip install customtkinter pillow
```

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/MohammadMasir/AppointmentManager.git
cd appointment-manager
```

2. Run the Python script:
```bash
python appointment_manager.py
```

## File Structure
- `appointment_manager.py`: The main file containing the code for managing the appointment system using a doubly linked list structure and handling the GUI elements
- `back.png`: Image used for the "back" button in the GUI

## Code Overview

### Appointment Queue
- **AppointmentNode:** Represents an individual appointment with attributes like:
  - Patient name
  - Doctor name
  - Allotted time
  - Pointers to next and previous appointments

- **ApptQueue:** Manages the appointment queue. It supports functions like:
  - Adding appointments
  - Removing appointments
  - Displaying appointments
  - Checking availability

### GUI with CustomTkinter
- **AppoinmentManager:** Inherits from `ctk.CTk` and manages the application's windows and frames
  - `startScreen()`: Displays the start screen with options to view or book appointments
  - `newScreen()`: Provides a form to input details for a new appointment
  - `view_appointment()`: Displays a scrollable list of all scheduled appointments
- **Full-Screen Toggle:** The application can toggle between full-screen and windowed mode using the F11 key

## Future Enhancements
- **Database Integration:** Store appointments in a database for persistence
- **Enhanced Appointment Handling:** Add features for rescheduling and modifying appointments
- **Multi-User Support:** Allow different users (doctors, patients) to log in and manage their appointments

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
