import tkinter as tk
from tkinter import messagebox
import csv

def load_users_from_csv(csv_filename):
    users = {}
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                role = row['role']
                username = row['username']
                password = row['password']
                if role not in users:
                    users[role] = []
                users[role].append({'username': username, 'password': password})
    except FileNotFoundError:
        print(f"CSV file '{csv_filename}' not found.")
    return users

users = load_users_from_csv('users.csv')

root = tk.Tk()
root.title("Restaurant Login")
root.geometry("300x400")

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

roles = ['Pelanggan', 'Pelayan/Dapur', 'Kasir', 'Admin', 'Owner']

def select_role(role):
    # Hide main frame
    main_frame.pack_forget()
    show_login_screen(role)

for role in roles:
    role_button = tk.Button(main_frame, text=role, width=20, command=lambda r=role: select_role(r))
    role_button.pack(pady=5)

def show_login_screen(role):
    login_frame = tk.Frame(root)
    login_frame.pack(pady=20)
    
    def back_to_main():
        login_frame.pack_forget()
        main_frame.pack(pady=20)
    
    back_button = tk.Button(login_frame, text="Back", command=back_to_main)
    back_button.pack(pady=5)
    
    if role == 'Pelanggan':
        # Show only login button
        login_button = tk.Button(login_frame, text="Login as Pelanggan", command=lambda: login_as_pelanggan(login_frame))
        login_button.pack(pady=5)
    else:
        # Show username and password fields
        tk.Label(login_frame, text=f"Login as {role}").pack(pady=5)
        tk.Label(login_frame, text="Username:").pack()
        username_entry = tk.Entry(login_frame)
        username_entry.pack()
        tk.Label(login_frame, text="Password:").pack()
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.pack()
        
        login_button = tk.Button(login_frame, text="Login", command=lambda: login_user(role, username_entry.get(), password_entry.get(), login_frame))
        login_button.pack(pady=5)
        
    def login_as_pelanggan(frame):
        messagebox.showinfo("Login", "Pelanggan logged in successfully!")
        # Proceed to pelanggan interface (placeholder)
        frame.pack_forget()
        show_pelanggan_interface()
        
def show_pelanggan_interface():
    pelanggan_frame = tk.Frame(root)
    pelanggan_frame.pack(pady=20)
    tk.Label(pelanggan_frame, text="Welcome, Pelanggan!").pack()
    tk.Button(pelanggan_frame, text="Logout", command=lambda: logout(pelanggan_frame)).pack(pady=5)
    
def logout(frame):
    frame.pack_forget()
    main_frame.pack(pady=20)
    
def login_user(role, username, password, frame):
    # Map the role names to CSV role names
    role_mapping = {'Pelayan/Dapur': 'pelayan', 'Kasir': 'kasir', 'Admin': 'admin', 'Owner': 'owner'}
    csv_role = role_mapping.get(role, role.lower())
    # Check if role exists in users dict
    if csv_role not in users:
        messagebox.showerror("Error", "Role not recognized.")
        return
    # Check for username and password match
    for user in users[csv_role]:
        if user['username'] == username and user['password'] == password:
            messagebox.showinfo("Login", f"{role} logged in successfully!")
            # Proceed to role's interface (placeholder)
            frame.pack_forget()
            show_role_interface(role)
            return
    # If no match found
    messagebox.showerror("Error", "Invalid username or password.")
    
def show_role_interface(role):
    role_frame = tk.Frame(root)
    role_frame.pack(pady=20)
    tk.Label(role_frame, text=f"Welcome, {role}!").pack()
    tk.Button(role_frame, text="Logout", command=lambda: logout(role_frame)).pack(pady=5)
    
root.mainloop()