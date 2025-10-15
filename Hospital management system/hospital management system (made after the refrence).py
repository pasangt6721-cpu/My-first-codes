import tkinter as tk
from tkinter import messagebox , ttk

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

        # Title
        tk.Label(
            self.root,
            text="Hospital Management System",
            font=("Helvetica", 28, "bold"),
            fg="#2C3E50"
        ).pack(pady=40)

        # Frame for inputs
        login_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=40, pady=30)
        login_frame.pack(pady=20)

        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)

        # Username
        tk.Label(login_frame, text="Username:", font=label_font, bg="#F8F9FA").grid(row=0, column=0, sticky="w", pady=10)
        self.username_entry = tk.Entry(login_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.username_entry.grid(row=0, column=1, pady=10)

        # Password
        tk.Label(login_frame, text="Password:", font=label_font, bg="#F8F9FA").grid(row=1, column=0, sticky="w", pady=10)
        self.password_entry = tk.Entry(login_frame, show="*", font=entry_font, width=30, bd=2, relief="solid")
        self.password_entry.grid(row=1, column=1, pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#FFFFFF")
        btn_frame.pack(pady=30)

        login_btn = tk.Button(
            btn_frame,
            text="Login",
            command=self.check_login,
            bg="#2980B9",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            bd=0,
            pady=8
        )
        login_btn.grid(row=0, column=0, padx=20)

        exit_btn = tk.Button(
            btn_frame,
            text="Exit",
            command=self.root.destroy,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            bd=0,
            pady=8
        )
        exit_btn.grid(row=0, column=1, padx=20)

    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_login(self):
        # Checking the password and username
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome to the system!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")


    # ----------------- MAIN MENU -----------------
    def show_main_menu(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text="Hospital Management System",
            font=("Helvetica", 28, "bold"),
            fg="#2C3E50"
        ).pack(pady=40)

        # Menu frame
        menu_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=50, pady=40)
        menu_frame.pack(pady=20)

        btn_font = ("Arial", 12, "bold")

        # Doctor Management Button
        tk.Button(
            menu_frame,
            text="Doctor Management",
            width=25,
            command=self.doctor_menu,
            bg="#3498DB",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Patient Management Button
        tk.Button(
            menu_frame,
            text="Patient Management",
            width=25,
            command=self.patient_menu,
            bg="#2ECC71",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Logout Button
        tk.Button(
            menu_frame,
            text="Logout",
            width=25,
            command=self.show_login_screen,
            bg="#E74C3C",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)


    #--------------All of the Doctor part ----------
    def doctor_menu(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text="Doctor Management",
            font=("Helvetica", 24, "bold"),
            fg="#2C3E50"
        ).pack(pady=40)

        # Menu frame
        menu_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=50, pady=40)
        menu_frame.pack(pady=20)

        btn_font = ("Arial", 12, "bold")

        # Register Doctor
        tk.Button(
            menu_frame,
            text="Register Doctor",
            width=25,
            command=self.register_doctor,
            bg="#3498DB",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # View Doctors
        tk.Button(
            menu_frame,
            text="View Doctors",
            width=25,
            command=self.view_doctors,
            bg="#2ECC71",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Delete Doctor
        tk.Button(
            menu_frame,
            text="Delete Doctor",
            width=25,
            command=self.delete_doctor,
            bg="#E74C3C",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Back to Main Menu
        tk.Button(
            menu_frame,
            text="⬅ Back",
            width=25,
            command=self.show_main_menu,
            bg="#7F8C8D",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)


    def register_doctor(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text="Register Doctor",
            font=("Helvetica", 24, "bold"),
            fg="#2C3E50"
        ).pack(pady=30)

        # Frame for inputs
        form_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=40, pady=30)
        form_frame.pack(pady=10)

        # Styling helper
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)

        # Row 1 - Doctor ID
        tk.Label(form_frame, text="Doctor ID:", font=label_font, bg="#F8F9FA").grid(row=0, column=0, sticky="w", pady=8)
        self.doc_id = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.doc_id.grid(row=0, column=1, pady=8)

        # Row 2 - Name
        tk.Label(form_frame, text="Name:", font=label_font, bg="#F8F9FA").grid(row=1, column=0, sticky="w", pady=8)
        self.doc_name = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.doc_name.grid(row=1, column=1, pady=8)

        # Row 3 - Age
        tk.Label(form_frame, text="Age:", font=label_font, bg="#F8F9FA").grid(row=2, column=0, sticky="w", pady=8)
        self.doc_age = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.doc_age.grid(row=2, column=1, pady=8)

        # Row 4 - Specialization
        tk.Label(form_frame, text="Specialization:", font=label_font, bg="#F8F9FA").grid(row=3, column=0, sticky="w", pady=8)
        self.doc_spec = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.doc_spec.grid(row=3, column=1, pady=8)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#FFFFFF")
        btn_frame.pack(pady=30)

        save_btn = tk.Button(
            btn_frame, text="Save Doctor",
            command=self.save_doctor,
            bg="#27AE60", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        )
        save_btn.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(
            btn_frame, text="⬅ Back",
            command=self.doctor_menu,
            bg="#E74C3C", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        )
        back_btn.grid(row=0, column=1, padx=20)


    def save_doctor(self):
        # Get and clean user input
        doc_id = self.doc_id.get().strip()
        name = self.doc_name.get().strip()
        age = self.doc_age.get().strip()
        spec = self.doc_spec.get().strip()

        # Validate empty fields
        if not all([doc_id, name, age, spec]):
            messagebox.showwarning("Missing Information", "⚠ Please fill in all fields.")
            return

        # Validate numeric age
        if not age.isdigit():
            messagebox.showerror("Invalid Age", " Age must be a number.")
            return

        # Check for duplicate ID
        if doc_id in self.doctors:
            messagebox.showerror("Duplicate ID", f" Doctor ID '{doc_id}' already exists.")
            return

        # Confirm save
        confirm = messagebox.askyesno("Confirm Save", f"Save doctor '{name}' with ID {doc_id}?")
        if not confirm:
            return

        # Save to dictionary
        self.doctors[doc_id] = {
            "Name": name,
            "Age": age,
            "Specialization": spec
        }

        # Success message
        messagebox.showinfo("Success", f" Doctor '{name}' registered successfully!")

        # Go back to doctor menu
        self.doctor_menu()

    def view_doctors(self):
        self.clear_screen()

        # Title
        tk.Label(self.root, text=" Registered Doctors", font=("Helvetica", 22, "bold"), fg="#2C3E50").pack(pady=20)

        if not self.doctors:
            tk.Label(self.root, text="No doctors registered", font=("Arial", 14)).pack(pady=10)
        else:
            # Table
            columns = ("ID", "Name", "Age", "Specialization")
            tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
            tree.pack(pady=10, padx=20)

            # Define headings
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", width=150)

            # Insert data
            for doc_id, info in self.doctors.items():
                tree.insert("", tk.END, values=(doc_id, info["Name"], info["Age"], info["Specialization"]))

        # Back button
        tk.Button(self.root, text="⬅ Back", command=self.doctor_menu, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"), width=15).pack(pady=20)


    def delete_doctor(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text=" Delete Doctor",
            font=("Helvetica", 22, "bold"),
            fg="#C0392B"
        ).pack(pady=30)

        # Instruction
        tk.Label(
            self.root,
            text="Enter the Doctor ID you want to delete:",
            font=("Arial", 14)
        ).pack(pady=10)

        # Input box
        self.del_doc_id = tk.Entry(self.root, font=("Arial", 12), width=30, bd=2, relief="solid")
        self.del_doc_id.pack(pady=10)

        # Button frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        # Delete button
        tk.Button(
            btn_frame,
            text=" Delete",
            command=self.confirm_delete_doctor,
            bg="#C0392B", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        ).grid(row=0, column=0, padx=20)

        # Back button
        tk.Button(
            btn_frame,
            text=" Back",
            command=self.doctor_menu,
            bg="#7F8C8D", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        ).grid(row=0, column=1, padx=20)


    def confirm_delete_doctor(self):
        doc_id = self.del_doc_id.get().strip()  # remove extra spaces

        if not doc_id:
            messagebox.showwarning("Input Needed", "⚠ Please enter a Doctor ID.")
            return

        if doc_id not in self.doctors:
            messagebox.showerror("Error", f" Doctor ID '{doc_id}' not found.")
            return

        # Ask for confirmation
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete Doctor '{self.doctors[doc_id]['Name']}' (ID: {doc_id})?"
        )
        if not confirm:
            return

        # Delete doctor
        del self.doctors[doc_id]

        # Remove doctor from any patient assignment
        for pat in self.patients.values():
            if pat["Doctor"] == doc_id:
                pat["Doctor"] = None

        # Show success
        messagebox.showinfo("Deleted", f" Doctor '{doc_id}' has been deleted successfully!")
        self.doctor_menu()


    #-----------patient part----------------
    def patient_menu(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text=" Patient Management",
            font=("Helvetica", 24, "bold"),
            fg="#2C3E50"
        ).pack(pady=40)

        # Menu frame
        menu_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=50, pady=40)
        menu_frame.pack(pady=20)

        btn_font = ("Arial", 12, "bold")

        # Register Patient
        tk.Button(
            menu_frame,
            text="Register Patient",
            width=30,
            command=self.register_patient,
            bg="#3498DB",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # View Patients
        tk.Button(
            menu_frame,
            text=" View Patients",
            width=30,
            command=self.view_patients,
            bg="#2ECC71",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Delete Patient
        tk.Button(
            menu_frame,
            text="Delete Patient",
            width=30,
            command=self.delete_patient,
            bg="#E74C3C",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Assign Doctor to Patient
        tk.Button(
            menu_frame,
            text="Assign Doctor to Patient",
            width=30,
            command=self.assign_doctor_to_patient,
            bg="#9B59B6",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

        # Back to Main Menu
        tk.Button(
            menu_frame,
            text="⬅ Back",
            width=30,
            command=self.show_main_menu,
            bg="#7F8C8D",
            fg="white",
            font=btn_font,
            bd=0,
            pady=10
        ).pack(pady=15)

    

    def register_patient(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text=" Register Patient",
            font=("Helvetica", 24, "bold"),
            fg="#2C3E50"
        ).pack(pady=30)

        # Frame for inputs
        form_frame = tk.Frame(self.root, bg="#F8F9FA", bd=2, relief="ridge", padx=40, pady=30)
        form_frame.pack(pady=10)

        # Fonts
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)

        # Patient ID
        tk.Label(form_frame, text="Patient ID:", font=label_font, bg="#F8F9FA").grid(row=0, column=0, sticky="w", pady=8)
        self.pat_id = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.pat_id.grid(row=0, column=1, pady=8)

        # Name
        tk.Label(form_frame, text="Name:", font=label_font, bg="#F8F9FA").grid(row=1, column=0, sticky="w", pady=8)
        self.pat_name = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.pat_name.grid(row=1, column=1, pady=8)

        # Age
        tk.Label(form_frame, text="Age:", font=label_font, bg="#F8F9FA").grid(row=2, column=0, sticky="w", pady=8)
        self.pat_age = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.pat_age.grid(row=2, column=1, pady=8)

        # Blood Group (Dropdown)
        tk.Label(form_frame, text="Blood Group:", font=label_font, bg="#F8F9FA").grid(row=3, column=0, sticky="w", pady=8)
        blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.pat_bg = ttk.Combobox(form_frame, values=blood_groups, font=entry_font, state="readonly", width=28)
        self.pat_bg.grid(row=3, column=1, pady=8)
        self.pat_bg.set("Select Blood Group")  # default placeholder

        # Disease
        tk.Label(form_frame, text="Disease:", font=label_font, bg="#F8F9FA").grid(row=4, column=0, sticky="w", pady=8)
        self.pat_dis = tk.Entry(form_frame, font=entry_font, width=30, bd=2, relief="solid")
        self.pat_dis.grid(row=4, column=1, pady=8)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#FFFFFF")
        btn_frame.pack(pady=30)

        save_btn = tk.Button(
            btn_frame, text=" Save Patient",
            command=self.save_patient,
            bg="#27AE60", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        )
        save_btn.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(
            btn_frame, text=" Back",
            command=self.patient_menu,
            bg="#E74C3C", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        )
        back_btn.grid(row=0, column=1, padx=20)

    def save_patient(self):
        pat_id = self.pat_id.get().strip()
        name = self.pat_name.get().strip()
        age = self.pat_age.get().strip()
        blood_group = self.pat_bg.get().strip()
        disease = self.pat_dis.get().strip()

        # Check if any field is empty
        if not all([pat_id, name, age, blood_group, disease]):
            messagebox.showerror("Error", "⚠ All fields are required!")
            return

        # Validate Blood Group selection
        valid_blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        if blood_group not in valid_blood_groups:
            messagebox.showerror("Error", "⚠ Please select a valid Blood Group!")
            return

        # Check if patient ID already exists
        if pat_id in self.patients:
            messagebox.showerror("Error", f" Patient ID '{pat_id}' already exists!")
            return

        # Optional: Validate age as a positive number
        if not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Error", "⚠ Age must be a positive number!")
            return

        # Save patient
        self.patients[pat_id] = {
            "Name": name,
            "Age": age,
            "Blood Group": blood_group,
            "Disease": disease,
            "Doctor": None
        }

        # Success message
        messagebox.showinfo("Success", f"Patient '{name}' (ID: {pat_id}) registered successfully!")

        # Return to Patient Menu
        self.patient_menu()


    def view_patients(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text="Registered Patients",
            font=("Helvetica", 22, "bold"),
            fg="#2C3E50"
        ).pack(pady=20)

        if not self.patients:
            tk.Label(
                self.root,
                text="No patients registered",
                font=("Arial", 14)
            ).pack(pady=10)
        else:
            # Define columns
            columns = ("ID", "Name", "Age", "Blood Group", "Disease", "Doctor")
            tree = ttk.Treeview(self.root, columns=columns, show="headings", height=12)
            tree.pack(pady=10, padx=20)

            # Define headings
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", width=120)

            # Insert patient data
            for pat_id, info in self.patients.items():
                doctor = info["Doctor"] if info["Doctor"] else "None"
                tree.insert("", tk.END, values=(
                    pat_id,
                    info["Name"],
                    info["Age"],
                    info["Blood Group"],
                    info["Disease"],
                    doctor
                ))

        # Back button
        tk.Button(
            self.root,
            text="⬅ Back",
            command=self.patient_menu,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15
        ).pack(pady=20)

    def delete_patient(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text=" Delete Patient",
            font=("Helvetica", 22, "bold"),
            fg="#C0392B"
        ).pack(pady=30)

        # Instruction
        tk.Label(
            self.root,
            text="Enter the Patient ID to delete:",
            font=("Arial", 14)
        ).pack(pady=10)

        # Input box
        self.del_pat_id = tk.Entry(self.root, font=("Arial", 12), width=30, bd=2, relief="solid")
        self.del_pat_id.pack(pady=10)

        # Button frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        # Delete button
        tk.Button(
            btn_frame,
            text=" Delete",
            command=self.confirm_delete_patient,
            bg="#C0392B", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        ).grid(row=0, column=0, padx=20)

        # Back button
        tk.Button(
            btn_frame,
            text="⬅ Back",
            command=self.patient_menu,
            bg="#7F8C8D", fg="white",
            font=("Arial", 12, "bold"),
            width=15, bd=0, pady=8
        ).grid(row=0, column=1, padx=20)
    
    def confirm_delete_patient(self):
        pat_id = self.del_pat_id.get().strip()  # Remove spaces

        if not pat_id:
            messagebox.showwarning("Input Required", "⚠ Please enter a Patient ID.")
            return

        if pat_id not in self.patients:
            messagebox.showerror("Not Found", f" Patient ID '{pat_id}' does not exist.")
            return

        # Confirm deletion
        patient_name = self.patients[pat_id]['Name']
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete Patient '{patient_name}' (ID: {pat_id})?"
        )
        if not confirm:
            return

        # Delete patient
        del self.patients[pat_id]

        # Success message
        messagebox.showinfo("Deleted", f" Patient '{patient_name}' has been deleted successfully!")
        self.patient_menu()

    def assign_doctor_to_patient(self):
        self.clear_screen()

        # Title
        tk.Label(
            self.root,
            text=" Assign Doctor to Patient",
            font=("Helvetica", 22, "bold"),
            fg="#2C3E50"
        ).pack(pady=20)

        if not self.patients:
            tk.Label(self.root, text="No patients registered.", font=("Arial", 14)).pack(pady=10)
            tk.Button(self.root, text="⬅ Back", command=self.patient_menu, bg="#7F8C8D", fg="white",
                    font=("Arial", 12, "bold"), width=15).pack(pady=20)
            return

        if not self.doctors:
            tk.Label(self.root, text="No doctors registered.", font=("Arial", 14)).pack(pady=10)
            tk.Button(self.root, text="⬅ Back", command=self.patient_menu, bg="#7F8C8D", fg="white",
                    font=("Arial", 12, "bold"), width=15).pack(pady=20)
            return

        # Frame for selection
        frame = tk.Frame(self.root, pady=20)
        frame.pack()

        # Patient selection
        tk.Label(frame, text="Select Patient:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.patient_combo = ttk.Combobox(frame, values=list(self.patients.keys()), font=("Arial", 12), state="readonly")
        self.patient_combo.grid(row=0, column=1, pady=10)

        # Doctor selection
        tk.Label(frame, text="Select Doctor:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.doctor_combo = ttk.Combobox(frame, values=list(self.doctors.keys()), font=("Arial", 12), state="readonly")
        self.doctor_combo.grid(row=1, column=1, pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text=" Assign", command=self.confirm_assign, bg="#27AE60", fg="white",
                font=("Arial", 12, "bold"), width=15, bd=0, pady=8).grid(row=0, column=0, padx=20)
        tk.Button(btn_frame, text="⬅ Back", command=self.patient_menu, bg="#E74C3C", fg="white",
                font=("Arial", 12, "bold"), width=15, bd=0, pady=8).grid(row=0, column=1, padx=20)
    def confirm_assign(self):
        pat_id = self.patient_combo.get()
        doc_id = self.doctor_combo.get()

        if not pat_id or not doc_id:
            messagebox.showwarning("Input Required", "⚠ Please select both Patient and Doctor.")
            return

        self.patients[pat_id]["Doctor"] = doc_id
        messagebox.showinfo("Success", f" Doctor '{doc_id}' assigned to Patient '{pat_id}'.")
        self.patient_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
