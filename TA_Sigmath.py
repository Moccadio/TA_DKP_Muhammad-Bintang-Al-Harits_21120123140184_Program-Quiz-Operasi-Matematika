import tkinter as tk
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
    def __init__(self, parent, total_quiz, total_jawaban, salah_jawab):
        self.parent = parent
        self.total_quiz = total_quiz
        self.total_jawaban = total_jawaban
        self.salah_jawab = salah_jawab

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.show_results()

    def show_results(self):
        result_text = f"Quiz Berakhir!\n\nTotal Quiz: {self.total_quiz}\nJawaban Benar: {self.total_jawaban}\nJawaban Salah: {self.salah_jawab}"
        tk.Label(self.frame, text=result_text, font=("Helvetica", 14)).pack(pady=20)
        
        tk.Button(self.frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)
        tk.Button(self.frame, text="Keluar Aplikasi", command=self.parent.quit).pack(pady=10)

    def back_to_main_menu(self):
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
        self.main_menu()

    def main_menu(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        tk.Label(self.main_frame, text="Welcome to SigMath", font=("Poppins", 16)).pack(pady=20)

        tk.Button(self.main_frame, text="Mulai Quiz", command=self.select_difficulty).pack(pady=10)
        tk.Button(self.main_frame, text="Tutorial", command=self.start_tutorial).pack(pady=10)
        tk.Button(self.main_frame, text="Keluar Aplikasi", command=self.root.quit).pack(pady=10)

        identity_frame = tk.Frame(self.main_frame)
        identity_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor=tk.W)
        tk.Label(identity_frame, text="Tugas Akhir\nMuhammad Bintang Al Harits\n21120123140184",
                 font=("Poppins", 8)).pack(side=tk.LEFT, fill=tk.X)

    def select_difficulty(self):
        self.main_frame.destroy()
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack()

        tk.Label(self.difficulty_frame, text="Pilih Mode:", font=("Poppins", 14)).pack(pady=10)

        self.difficulty = tk.StringVar()
        tk.Radiobutton(self.difficulty_frame, text="Baby Gronk", variable=self.difficulty, value="easy").pack()
        tk.Radiobutton(self.difficulty_frame, text="Rizzler", variable=self.difficulty, value="medium").pack()
        tk.Radiobutton(self.difficulty_frame, text="Skibidi Abyss", variable=self.difficulty, value="hard").pack()

        tk.Button(self.difficulty_frame, text="Mulai Quiz", command=self.start_quiz_with_difficulty).pack(pady=10)
        tk.Button(self.difficulty_frame, text="Kembali ke Main Menu", command=self.back_to_main_menu).pack(pady=10)

    def start_quiz_with_difficulty(self):
        selected_difficulty = self.difficulty.get()
        if selected_difficulty:
            self.difficulty_frame.destroy()
            self.difficulty = selected_difficulty
            self.start_quiz()

    def start_quiz(self):
        self.main_frame.destroy()
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack()
        self.start_time = time.time()
        self.timer_label = tk.Label(self.quiz_frame, text="05:00")
        self.timer_label.pack()
        self.update_timer()

        self.current_problem = None
        self.total_jawaban = 0
        self.salah_jawab = 0
        self.question_count = 0
        self.total_quiz = self.get_total_quiz()
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
        if hasattr(self, "tutorial_frame"):
            self.tutorial_frame.destroy()
        if hasattr(self, "difficulty_frame"):
            self.difficulty_frame.destroy()
        self.main_menu()

    def create_widgets(self):
        self.problem_label = tk.Label(self.quiz_frame, text="")
        self.problem_label.pack()

        self.answer_entry = tk.Entry(self.quiz_frame)
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        self.feedback_label = tk.Label(self.quiz_frame, text="")
        self.feedback_label.pack()

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
                factors.remove(bilangan1)
                bilangan2 = random.choice(factors)
            else:
                bilangan2 = random.randint(1, max_operand)
            
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
            self.root.after(1000, self.update_timer)
        else:
            self.show_results()

    def show_results(self):
        self.quiz_frame.destroy()
        if self.difficulty == "hard" and self.total_jawaban == 50:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Selamat! Anda telah menjadi 'Sigma Male Mewing'!"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)

        elif self.difficulty == "hard" and self.total_jawaban > 40:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Selamat! Anda telah menjadi 'Only in Ohio'!"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)

        elif self.difficulty == "hard" and self.total_jawaban > 30:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Kerja bagus! Namun kemampuanmu belum sebanding dengan Skibidi Toilet"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)

        elif self.difficulty == "medium" and self.total_jawaban == 20:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Selamat! Anda telah menjadi 'Level 50 Rizz'!"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)
        
        elif self.difficulty == "easy" and self.total_jawaban == 10:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Selamat! Anda telah menjadi 'Baby Gronk'!"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)
        else:
            HasilJawaban(self.root, self.total_quiz, self.total_jawaban, self.salah_jawab)
            congratulation_text = "Beristirahatlah! Mio Mirza menunggumu!"
            tk.Label(self.root, text=congratulation_text, font=("Helvetica", 14)).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()