import itertools
import random
import operator
import tkinter as tk
from tkinter import messagebox


def generate_numbers():
    return [random.randint(1, 9) for _ in range(4)]

def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception:
        return None

def generate_all_expressions(numbers):
    ops = ['+', '-', '*', '/']
    all_permutations = itertools.permutations(numbers)
    all_op_combinations = itertools.product(ops, repeat=3)
    
    valid_expressions = []
    for perm in all_permutations:
        for ops in all_op_combinations:
            expressions = [
                f"(({perm[0]} {ops[0]} {perm[1]}) {ops[1]} {perm[2]}) {ops[2]} {perm[3]}",
                f"({perm[0]} {ops[0]} ({perm[1]} {ops[1]} {perm[2]})) {ops[2]} {perm[3]}",
                f"{perm[0]} {ops[0]} (({perm[1]} {ops[1]} {perm[2]}) {ops[2]} {perm[3]})",
                f"{perm[0]} {ops[0]} ({perm[1]} {ops[1]} ({perm[2]} {ops[2]} {perm[3]}))"
            ]
            
            for expr in expressions:
                if evaluate_expression(expr) == 24:
                    valid_expressions.append(expr)
    
    return valid_expressions

def play_game():
    def check_expression(event=None):
        user_input = entry.get()
        if evaluate_expression(user_input) == 24:
            messagebox.showinfo("Result", "Correct! You made 24.")
            new_game()  # Automatically start a new game
        else:
            messagebox.showinfo("Result", "Incorrect.")
    
    def new_game():
        nonlocal numbers
        while True:
            numbers = generate_numbers()
            if generate_all_expressions(numbers):
                break
        label_numbers.config(text=f"Your numbers:\n{numbers}")
        entry.delete(0, tk.END)
    
    def show_solution():
        solutions = generate_all_expressions(numbers)
        if solutions:
            formatted_solutions = "\n".join([f"{i+1}. {sol}" for i, sol in enumerate(solutions)])
            messagebox.showinfo("Solutions", f"Solutions found: {len(solutions)}\n\nPossible solutions:\n" + formatted_solutions)
        else:
            messagebox.showinfo("Solutions", "No possible solutions exist for these numbers.")
    
    root = tk.Tk()
    root.title("24 Game")
    
    while True:
        numbers = generate_numbers()
        if generate_all_expressions(numbers):
            break
    
    label_numbers = tk.Label(root, text=f"Your numbers:\n{numbers}")
    label_numbers.pack()
    
    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Return>", check_expression)
    
    check_button = tk.Button(root, text="Check", command=check_expression)
    check_button.pack()
    
    new_game_button = tk.Button(root, text="New Game", command=new_game)
    new_game_button.pack()
    
    solution_button = tk.Button(root, text="Show Solution", command=show_solution)
    solution_button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    play_game()

