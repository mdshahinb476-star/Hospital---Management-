
class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

class Doctor:
    def __init__(self, doctor_id, name, department, experience):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department
        self.experience = experience

    def display(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Dept: {self.department}, Exp: {self.experience} years")

class Appointment:
    def __init__(self, appointment_id, patient, doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor

    def display(self):
        print(f"Appointment ID: {self.appointment_id}")
        self.patient.display()
        self.doctor.display()

class HospitalManager:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def make_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_patients(self):
        for p in self.patients:
            p.display()

    def show_doctors(self):
        for d in self.doctors:
            d.display()

    def show_appointments(self):
        for a in self.appointments:
            a.display()

# Sample Demo
if __name__ == "__main__":
    manager = HospitalManager()
    while True:
        print("\n--- CareTrack Hospital Management ---")
        print("1. Add Patient\n2. Add Doctor\n3. Make Appointment")
        print("4. Show Patients\n5. Show Doctors\n6. Show Appointments\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            manager.add_patient(Patient(pid, name, age, disease))
        elif choice == '2':
            did = input("Enter Doctor ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            exp = input("Enter Years of Experience: ")
            manager.add_doctor(Doctor(did, name, dept, exp))
        elif choice == '3':
            aid = input("Enter Appointment ID: ")
            pid = input("Enter Patient ID: ")
            did = input("Enter Doctor ID: ")
            patient = next((p for p in manager.patients if p.patient_id == pid), None)
            doctor = next((d for d in manager.doctors if d.doctor_id == did), None)
            if patient and doctor:
                manager.make_appointment(Appointment(aid, patient, doctor))
            else:
                print("Invalid patient or doctor ID.")
        elif choice == '4':
            manager.show_patients()
        elif choice == '5':
            manager.show_doctors()
        elif choice == '6':
            manager.show_appointments()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")
