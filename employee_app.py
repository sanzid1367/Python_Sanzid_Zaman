import tkinter as tk
from tkinter import messagebox

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Main Menu")
        self.root.geometry("300x300")

        title_label = tk.Label(root, text="Employee Main Menu", font=("Arial", 12, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_button(root, "Add Employee", 15, 2, 0, 2, 10, 5, self.add_employee)
        self.create_button(root, "Edit Employee", 15, 3, 0, 2, 10, 5, self.search_employee)
        self.create_button(root, "Exit", 15, 5, 0, 2, 10, 5, root.quit)

        root.grid_columnconfigure(0, weight=1)

    def create_label_entry(self, parent, text, r, c):
        label = tk.Label(parent, text=text)
        label.grid(row=r, column=0, padx=10, pady=5)
        entry = tk.Entry(parent)
        entry.grid(row=r, column=1, padx=10, pady=5)
        return entry 

    def create_button(self, parent, text, width, r, c, span, px, py, command):
        button = tk.Button(parent, text=text, width=width, command=command)
        button.grid(row=r, column=c, columnspan=span, padx=px, pady=py)
        return button

    def add_employee(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")

        self.name_entry = self.create_label_entry(add_window, "Name:", 0, 0)
        self.age_entry = self.create_label_entry(add_window, "Age:", 1, 0)
        self.position_entry = self.create_label_entry(add_window, "Position:", 2, 0)
        self.salary_entry = self.create_label_entry(add_window, "Salary:", 3, 0)

        self.create_button(add_window, "Save", 15, 4, 0, 2, 10, 10, self.save_employee)

    def save_employee(self):

        name = self.name_entry.get()
        age = self.age_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        if not name or not age or not position or not salary:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        with open("employee_details.txt", "a") as file:
            file.write(f"{name}, {age}, {position}, {salary}\n")

        self.display_employee_details(name, age, position, salary)

    def display_employee_details(self, name, age, position, salary):
        details_window = tk.Toplevel(self.root)
        details_window.title("Employee Details")
        
        text_info = f"Name: {name}\nAge: {age}\nPosition: {position}\nSalary: {salary}"
        tk.Label(details_window, text="Saved Successfully!", font=("Arial", 10, "bold")).pack()
        tk.Label(details_window, text=text_info).pack(padx=20, pady=20)

    def search_employee(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Employee")

        tk.Label(search_window, text="Search Name:").grid(row=0, column=0, padx=10)
        search_entry = tk.Entry(search_window)
        search_entry.grid(row=0, column=1, padx=10)

        cmd = lambda: self.perform_search(search_entry.get())
        tk.Button(search_window, text="Search", command=cmd).grid(row=1, column=0, columnspan=2, pady=10)

    def perform_search(self, criteria):
        found_employees = []
        try:
            with open("employee_details.txt", "r") as file:
                for line in file:
                    data = line.strip().split(", ")

                    if len(data) >= 4 and criteria.lower() in line.lower():
                        found_employees.append(data)
                        break 
            
            if found_employees:
                self.edit_employee(found_employees[0])
            else:
                messagebox.showinfo("Result", "No employee found.")
        except FileNotFoundError:
             messagebox.showerror("Error", "No database found. Add an employee first.")

    def edit_employee(self, data):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Employee")

        self.name_entry = self.create_label_entry(edit_window, "Name:", 0, 0)
        self.age_entry = self.create_label_entry(edit_window, "Age:", 1, 0)
        self.position_entry = self.create_label_entry(edit_window, "Position:", 2, 0)
        self.salary_entry = self.create_label_entry(edit_window, "Salary:", 3, 0)

        self.name_entry.insert(0, data[0])
        self.age_entry.insert(0, data[1])
        self.position_entry.insert(0, data[2])
        self.salary_entry.insert(0, data[3])

        self.create_button(edit_window, "Save New Version", 15, 4, 0, 2, 10, 10, self.save_employee)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()