import tkinter as tk
from tkinter import messagebox
import random
import time

class Bilangan:
    def __init__(self, operasional, bilangan1, bilangan2):
        self.operasional = operasional
        self.bilangan1 = bilangan1
        self.bilangan2 = bilangan2
        self.total_jawaban = self.hitung_jawaban()

    def hitung_jawaban(self):
        if self.operasional == "+":
            return self.bilangan1 + self.bilangan2
        elif self.operasional == "-":
            return self.bilangan1 - self.bilangan2
        elif self.operasional == "*":
            return self.bilangan1 * self.bilangan2
        elif self.operasional == "/":
            if self.bilangan2 != 0:
                return self.bilangan1 / self.bilangan2
            else:
                return "Error"

class HasilJawaban:
    def __init__(self, parent, total_quiz, total_jawaban, salah_jawab, username, difficulty):
        self.parent = parent
        self.total_quiz = total_quiz
        self.total_jawaban = total_jawaban
        self.salah_jawab = salah_jawab
        self.username = username
        self.difficulty = difficulty

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.save_to_leaderboard()
        self.show_results()

    def save_to_leaderboard(self):
        with open("leaderboard.txt", "a") as file:
            file.write(f"{self.username},{self.difficulty},{self.total_jawaban}\n")

    def show_results(self):
        result_text = f"Quiz Berakhir!\n\nTotal Quiz: {self.total_quiz}\nJawaban Benar: {self.total_jawaban}\nJawaban Salah: {self.salah_jawab}"
        tk.Label(self.frame, text=result_text, font=("Helvetica", 14)).pack(pady=20)
        
        tk.Button(self.frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)
        tk.Button(self.frame, text="Lihat Leaderboard", command=self.show_leaderboard).pack(pady=10)
        tk.Button(self.frame, text="Keluar Aplikasi", command=self.parent.quit).pack(pady=10)

    def show_leaderboard(self):
        self.frame.destroy()
        self.leaderboard_frame = tk.Frame(self.parent)
        self.leaderboard_frame.pack()

        tk.Label(self.leaderboard_frame, text="Leaderboard", font=("Helvetica", 16)).pack(pady=20)

        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()
            scores = [line.strip().split(",") for line in lines]

        scores.sort(key=lambda x: int(x[2]), reverse=True)

        for score in scores[:10]:
            tk.Label(self.leaderboard_frame, text=f"Username: {score[0]}, Mode: {score[1]}, Score: {score[2]}", font=("Helvetica", 12)).pack()

        tk.Button(self.leaderboard_frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)

    def back_to_main_menu(self):
        self.parent.destroy()
        root = tk.Tk()
        app = MathQuizApp(root)
        root.mainloop()

class PilihMode:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.frame = tk.Frame(parent)
        self.frame.pack()

        tk.Label(self.frame, text="Pilih Mode:", font=("Poppins", 14)).pack(pady=10)

        self.difficulty = tk.StringVar()
        tk.Radiobutton(self.frame, text="Baby Gronk", variable=self.difficulty, value="easy").pack()
        tk.Radiobutton(self.frame, text="Rizzler", variable=self.difficulty, value="medium").pack()
        tk.Radiobutton(self.frame, text="Skibidi Abyss", variable=self.difficulty, value="hard").pack()

        tk.Button(self.frame, text="Mulai Quiz", command=self.start_quiz_with_difficulty).pack(pady=10)
        tk.Button(self.frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)

    def start_quiz_with_difficulty(self):
        selected_difficulty = self.difficulty.get()
        if selected_difficulty:
            self.callback(selected_difficulty)
            self.frame.destroy()

    def back_to_main_menu(self):
        self.frame.destroy()
        self.parent.destroy()
        root = tk.Tk()
        app = MathQuizApp(root)
        root.mainloop()

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SigMath")
        self.root.geometry("800x600")
        self.quiz_duration = 300 
        self.start_time = None
        self.timer_label = None 
        self.difficulty = None  
        self.username = None
        self.login_screen()

    def login_screen(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(fill="both", expand=True)

        tk.Label(self.login_frame, text="Login to SigMath", font=("Poppins", 16)).pack(pady=20)

        tk.Label(self.login_frame, text="Username:", font=("Poppins", 14)).pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        tk.Label(self.login_frame, text="Password:", font=("Poppins", 14)).pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.login_frame, text="Login", command=self.check_login).pack(pady=10)
        tk.Button(self.login_frame, text="Register", command=self.show_register).pack(pady=10)
        tk.Button(self.login_frame, text="Keluar Aplikasi", command=self.root.quit).pack(pady=10)

    def show_register(self):
        self.login_frame.destroy()
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(fill="both", expand=True)

        tk.Label(self.register_frame, text="Register to SigMath", font=("Poppins", 16)).pack(pady=20)

        tk.Label(self.register_frame, text="Username:", font=("Poppins", 14)).pack()
        self.new_username_entry = tk.Entry(self.register_frame)
        self.new_username_entry.pack()

        tk.Label(self.register_frame, text="Password:", font=("Poppins", 14)).pack()
        self.new_password_entry = tk.Entry(self.register_frame, show="*")
        self.new_password_entry.pack()

        tk.Label(self.register_frame, text="Confirm Password:", font=("Poppins", 14)).pack()
        self.confirm_password_entry = tk.Entry(self.register_frame, show="*")
        self.confirm_password_entry.pack()

        tk.Button(self.register_frame, text="Register", command=self.register_user).pack(pady=10)
        tk.Button(self.register_frame, text="Back to Login", command=self.back_to_login).pack(pady=10)

    def register_user(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match.")
            return

        with open("users.txt", "a") as file:
            file.write(f"{new_username},{new_password}\n")

        messagebox.showinfo("Registration Successful", "You have registered successfully.")
        self.register_frame.destroy()
        self.login_screen()

    def back_to_login(self):
        self.register_frame.destroy()
        self.login_screen()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                saved_username, saved_password = user.strip().split(",")
                if username == saved_username and password == saved_password:
                    self.username = username
                    self.login_frame.destroy()
                    self.main_menu()
                    return

        messagebox.showerror("Login Failed", "Username atau password salah.")

    def main_menu(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        widgets = [
            tk.Label(self.main_frame, text="Welcome to SigMath", font=("Poppins", 16)),
            tk.Button(self.main_frame, text="Mulai Quiz", command=self.select_difficulty),
            tk.Button(self.main_frame, text="Tutorial", command=self.start_tutorial),
            tk.Button(self.main_frame, text="Keluar Aplikasi", command=self.root.quit)
        ]

        for widget in widgets:
            widget.pack(pady=10)

        identity_frame = tk.Frame(self.main_frame)
        identity_frame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Label(identity_frame, text="Tugas Akhir\nMuhammad Bintang Al Harits\n21120123140184", font=("Poppins", 8), anchor=tk.W).pack(side=tk.LEFT, fill=tk.X)

    def select_difficulty(self):
        self.main_frame.destroy()
        PilihMode(self.root, self.start_quiz_with_difficulty)

    def start_quiz_with_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.start_quiz()

    def start_quiz(self):
        self.main_frame.destroy()
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack()
        self.start_time = time.time()
        self.timer_label = tk.Label(self.quiz_frame, text="05:00")
        self.timer_label.pack()
        self.update_timer()  # Memulai pembaruan timer

        self.current_problem = None
        self.total_jawaban = 0
        self.salah_jawab = 0
        self.question_count = 0
        self.total_quiz = self.get_total_quiz()  # Mendapatkan jumlah soal berdasarkan kesulitan
        self.create_widgets()

    def get_total_quiz(self):
        if self.difficulty == "easy":
            return 10
        elif self.difficulty == "medium":
            return 20
        else:
            return 50

    def start_tutorial(self):
        self.main_frame.destroy()
        self.tutorial_frame = tk.Frame(self.root)
        self.tutorial_frame.pack()

        self.tutorial_label = tk.Label(self.tutorial_frame, text="Tutorial Mode", font=("Poppins", 16))
        self.tutorial_label.pack(pady=20)

        tk.Label(self.tutorial_frame, text="Penjumlahan:", font=("Poppins", 14)).pack()
        tk.Label(self.tutorial_frame, text="1 + 2 = 3", font=("Poppins", 14)).pack()
        
        tk.Label(self.tutorial_frame, text="Pengurangan:", font=("Poppins", 14)).pack()
        tk.Label(self.tutorial_frame, text="5 - 3 = 2", font=("Poppins", 14)).pack()
        
        tk.Label(self.tutorial_frame, text="Perkalian:", font=("Poppins", 14)).pack()
        tk.Label(self.tutorial_frame, text="4 * 3 = 4 + 4 + 4 = 16", font=("Poppins", 14)).pack()
        
        tk.Label(self.tutorial_frame, text="Pembagian:", font=("Poppins", 14)).pack()
        tk.Label(self.tutorial_frame, text="10 / 2 = (2) + (2) + (2) + (2) + (2) = 5", font=("Poppins", 14)).pack()

        tk.Button(self.tutorial_frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)

    def back_to_main_menu(self):
        self.tutorial_frame.destroy()
        self.main_menu()    

    def create_widgets(self):
        self.problem_label = tk.Label(self.quiz_frame, text="")
        self.problem_label.pack()

        self.answer_entry = tk.Entry(self.quiz_frame)
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        
        self.feedback_label = tk.Label(self.quiz_frame, text="")
        self.feedback_label.pack()

        self.feedback_label.config(text="")

        self.new_problem()


    def new_problem(self):
        current_time = time.time()
        if self.question_count < self.total_quiz and current_time - self.start_time < self.quiz_duration:
            self.question_count += 1
            operasionals = ["+", "-", "*", "/"]
            operasional = random.choice(operasionals)
            if self.difficulty == "easy":
                max_operand = 10
            elif self.difficulty == "medium":
                max_operand = 25
            else:
                max_operand = 50
            bilangan1 = random.randint(1, max_operand)
            
            if operasional == "/":
                factors = [i for i in range(2, max_operand+1) if bilangan1 % i == 0]
                factors.remove(bilangan1)  # Menghapus bilangan1 dari faktor-faktor yang mungkin
                bilangan2 = random.choice(factors)
            else:
                bilangan2 = random.randint(1, max_operand)  # Untuk operasi lain, masih dapat dipilih secara acak
            
            self.current_problem = Bilangan(operasional, bilangan1, bilangan2)
            self.problem_label.config(text=f"Question {self.question_count}/{self.total_quiz}: {bilangan1} {operasional} {bilangan2} = ")
        else:
            self.show_results()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = float(user_answer)
            if user_answer == self.current_problem.total_jawaban:
                self.total_jawaban += 1
                self.feedback_label.config(text="Correct!")
            else:
                self.salah_jawab += 1
                self.feedback_label.config(text="Incorrect. Try again.")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")
        self.answer_entry.delete(0, "end")
        self.new_problem()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = self.quiz_duration - elapsed_time
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            self.timer_label.config(text=f"{int(minutes):02d}:{int(seconds):02d}")
            self.root.after(1000, self.update_timer)  # Memperbarui timer setiap detik
        else:
            self.show_results()

    def show_results(self):
        self.quiz_frame.destroy()
        HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab, self.username, self.difficulty)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()