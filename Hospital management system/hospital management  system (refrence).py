import tkinter as tk
from tkinter import messagebox, ttk

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        # Data storage
        self.doctors = {}  # {doc_id: {"Name":..., "Age":..., "Specialization":...}}
        self.patients = {}  # {pat_id: {"Name":..., "Age":..., "Blood Group":..., "Disease":..., "Doctor":...}}

        self.show_login_screen()

    # ----------------- LOGIN -----------------
    def show_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 22, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=20)

    def check_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "1234":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # ----------------- MAIN MENU -----------------
    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Hospital Management System", font=("Arial", 22, "bold")).pack(pady=20)

        tk.Button(self.root, text="Doctor Management", width=20, command=self.doctor_menu).pack(pady=10)
        tk.Button(self.root, text="Patient Management", width=20, command=self.patient_menu).pack(pady=10)
        tk.Button(self.root, text="Logout", width=20, command=self.show_login_screen).pack(pady=10)

    # ----------------- DOCTOR MANAGEMENT -----------------
    def doctor_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Doctor Management", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Button(self.root, text="Register Doctor", width=20, command=self.register_doctor).pack(pady=10)
        tk.Button(self.root, text="View Doctors", width=20, command=self.view_doctors).pack(pady=10)
        tk.Button(self.root, text="Delete Doctor", width=20, command=self.delete_doctor).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, command=self.show_main_menu).pack(pady=10)

    def register_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Register Doctor", font=("Arial", 20, "bold")).pack(pady=20)
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Doctor ID").grid(row=0, column=0, padx=10, pady=5)
        self.doc_id = tk.Entry(frame)
        self.doc_id.grid(row=0, column=1, pady=5)
        tk.Label(frame, text="Name").grid(row=1, column=0, padx=10, pady=5)
        self.doc_name = tk.Entry(frame)
        self.doc_name.grid(row=1, column=1, pady=5)
        tk.Label(frame, text="Age").grid(row=2, column=0, padx=10, pady=5)
        self.doc_age = tk.Entry(frame)
        self.doc_age.grid(row=2, column=1, pady=5)
        tk.Label(frame, text="Specialization").grid(row=3, column=0, padx=10, pady=5)
        self.doc_spec = tk.Entry(frame)
        self.doc_spec.grid(row=3, column=1, pady=5)

        tk.Button(self.root, text="Save Doctor", command=self.save_doctor).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.doctor_menu).pack()

    def save_doctor(self):
        doc_id = self.doc_id.get()
        if not all([doc_id, self.doc_name.get(), self.doc_age.get(), self.doc_spec.get()]):
            messagebox.showerror("Error", "All fields are required")
            return
        if doc_id in self.doctors:
            messagebox.showerror("Error", "Doctor ID exists")
            return
        self.doctors[doc_id] = {"Name": self.doc_name.get(),
                                "Age": self.doc_age.get(),
                                "Specialization": self.doc_spec.get()}
        messagebox.showinfo("Success", "Doctor registered successfully")
        self.doctor_menu()

    def view_doctors(self):
        self.clear_screen()
        tk.Label(self.root, text="Registered Doctors", font=("Arial", 20, "bold")).pack(pady=20)
        if not self.doctors:
            tk.Label(self.root, text="No doctors registered").pack()
        else:
            for doc_id, info in self.doctors.items():
                tk.Label(self.root, text=f"ID:{doc_id} Name:{info['Name']} Age:{info['Age']} Spec:{info['Specialization']}").pack()
        tk.Button(self.root, text="Back", command=self.doctor_menu).pack(pady=20)

    def delete_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Doctor", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Enter Doctor ID to delete").pack(pady=10)
        self.del_doc_id = tk.Entry(self.root)
        self.del_doc_id.pack(pady=5)
        tk.Button(self.root, text="Delete", command=self.confirm_delete_doctor).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.doctor_menu).pack(pady=10)

    def confirm_delete_doctor(self):
        doc_id = self.del_doc_id.get()
        if doc_id in self.doctors:
            del self.doctors[doc_id]
            # remove from any patient assignment
            for pat in self.patients.values():
                if pat["Doctor"] == doc_id:
                    pat["Doctor"] = None
            messagebox.showinfo("Deleted", "Doctor deleted")
            self.doctor_menu()
        else:
            messagebox.showerror("Error", "Doctor ID not found")

    # ----------------- PATIENT MANAGEMENT -----------------
    def patient_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Patient Management", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Button(self.root, text="Register Patient", width=20, command=self.register_patient).pack(pady=10)
        tk.Button(self.root, text="View Patients", width=20, command=self.view_patients).pack(pady=10)
        tk.Button(self.root, text="Delete Patient", width=20, command=self.delete_patient).pack(pady=10)
        tk.Button(self.root, text="Assign Doctor to Patient", width=25, command=self.assign_doctor_to_patient).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, command=self.show_main_menu).pack(pady=10)

    def register_patient(self):
        self.clear_screen()
        tk.Label(self.root, text="Register Patient", font=("Arial", 20, "bold")).pack(pady=20)
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Patient ID").grid(row=0, column=0, padx=10, pady=5)
        self.pat_id = tk.Entry(frame)
        self.pat_id.grid(row=0, column=1, pady=5)
        tk.Label(frame, text="Name").grid(row=1, column=0, padx=10, pady=5)
        self.pat_name = tk.Entry(frame)
        self.pat_name.grid(row=1, column=1, pady=5)
        tk.Label(frame, text="Age").grid(row=2, column=0, padx=10, pady=5)
        self.pat_age = tk.Entry(frame)
        self.pat_age.grid(row=2, column=1, pady=5)
        tk.Label(frame, text="Blood Group").grid(row=3, column=0, padx=10, pady=5)
        self.pat_bg = tk.Entry(frame)
        self.pat_bg.grid(row=3, column=1, pady=5)
        tk.Label(frame, text="Disease").grid(row=4, column=0, padx=10, pady=5)
        self.pat_dis = tk.Entry(frame)
        self.pat_dis.grid(row=4, column=1, pady=5)

        tk.Button(self.root, text="Save Patient", command=self.save_patient).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.patient_menu).pack()

    def save_patient(self):
        pat_id = self.pat_id.get()
        if not all([pat_id, self.pat_name.get(), self.pat_age.get(), self.pat_bg.get(), self.pat_dis.get()]):
            messagebox.showerror("Error", "All fields are required")
            return
        if pat_id in self.patients:
            messagebox.showerror("Error", "Patient ID exists")
            return
        self.patients[pat_id] = {
            "Name": self.pat_name.get(),
            "Age": self.pat_age.get(),
            "Blood Group": self.pat_bg.get(),
            "Disease": self.pat_dis.get(),
            "Doctor": None
        }
        messagebox.showinfo("Success", "Patient registered successfully")
        self.patient_menu()

    def view_patients(self):
        self.clear_screen()
        tk.Label(self.root, text="Registered Patients", font=("Arial", 20, "bold")).pack(pady=20)
        if not self.patients:
            tk.Label(self.root, text="No patients registered").pack()
        else:
            for pat_id, info in self.patients.items():
                doc = info["Doctor"] if info["Doctor"] else "None"
                tk.Label(self.root, text=f"ID:{pat_id} Name:{info['Name']} Age:{info['Age']} BG:{info['Blood Group']} Disease:{info['Disease']} Doctor:{doc}").pack()
        tk.Button(self.root, text="Back", command=self.patient_menu).pack(pady=20)

    def delete_patient(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Patient", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Enter Patient ID to delete").pack(pady=10)
        self.del_pat_id = tk.Entry(self.root)
        self.del_pat_id.pack(pady=5)
        tk.Button(self.root, text="Delete", command=self.confirm_delete_patient).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.patient_menu).pack(pady=10)

    def confirm_delete_patient(self):
        pat_id = self.del_pat_id.get()
        if pat_id in self.patients:
            del self.patients[pat_id]
            messagebox.showinfo("Deleted", "Patient deleted")
            self.patient_menu()
        else:
            messagebox.showerror("Error", "Patient ID not found")

    def assign_doctor_to_patient(self):
        self.clear_screen()
        tk.Label(self.root, text="Assign Doctor to Patient", font=("Arial", 20, "bold")).pack(pady=20)
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Patient ID").grid(row=0, column=0, padx=10, pady=5)
        self.assign_pat_id = tk.Entry(frame)
        self.assign_pat_id.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Doctor ID").grid(row=1, column=0, padx=10, pady=5)
        self.assign_doc_id = tk.Entry(frame)
        self.assign_doc_id.grid(row=1, column=1, pady=5)

        tk.Button(self.root, text="Assign", command=self.confirm_assign).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.patient_menu).pack()

    def confirm_assign(self):
        pat_id = self.assign_pat_id.get()
        doc_id = self.assign_doc_id.get()
        if pat_id not in self.patients:
            messagebox.showerror("Error", "Patient ID not found")
            return
        if doc_id not in self.doctors:
            messagebox.showerror("Error", "Doctor ID not found")
            return
        self.patients[pat_id]["Doctor"] = doc_id
        messagebox.showinfo("Success", f"Doctor {doc_id} assigned to Patient {pat_id}")
        self.patient_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
