import tkinter as tk
from tkinter import messagebox

class RegisterForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Form")

        # Variabel untuk menyimpan data username dan password
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Label dan Entry untuk input username
        tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(root, textvariable=self.username)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Label dan Entry untuk input password
        tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, textvariable=self.password, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Tombol untuk register
        tk.Button(root, text="Register", command=self.register).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Inisialisasi data pendaftaran
        self.registered_users = {}  # Kamus kosong untuk menyimpan data pendaftaran

    def register(self):
        # Simpan username dan password yang dimasukkan pengguna
        new_username = self.username.get()
        new_password = self.password.get()

        # Periksa apakah username sudah terdaftar
        if new_username in self.registered_users:
            messagebox.showerror("Registration Failed", "Username already exists!")
        else:
            # Tambahkan username dan password baru ke dalam kamus data pendaftaran
            self.registered_users[new_username] = new_password
            messagebox.showinfo("Registration Successful", "Registration successful! You can now login.")
            # Setelah berhasil mendaftar, tutup jendela pendaftaran
            self.root.destroy()
            # Tampilkan jendela login
            login_window = LoginForm(tk.Tk())
            login_window.root.mainloop()

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")

        # Variabel untuk menyimpan data username dan password
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Label dan Entry untuk input username
        tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(root, textvariable=self.username)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Label dan Entry untuk input password
        tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, textvariable=self.password, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Tombol untuk login
        tk.Button(root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        # Simpan username dan password yang dimasukkan pengguna
        entered_username = self.username.get()
        entered_password = self.password.get()

        # Cek apakah username dan password valid (sesuai dengan data pendaftaran)
        if entered_username in register_window.registered_users and \
                register_window.registered_users[entered_username] == entered_password:
            # Jika login berhasil, tampilkan pesan selamat datang
            messagebox.showinfo("Login Successful", f"Welcome, {entered_username}!")
        else:
            # Jika login gagal, tampilkan pesan kesalahan
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    register_window = RegisterForm(root)
    root.mainloop()
