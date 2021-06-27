import tkinter as tk


LARGE_FONT_STYLE = ("Arial", 30)
SMALL_FONT_STYLE = ("Arial", 16)


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("320x540")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            1: (5, 1), 2: (5, 2), 3: (5, 3),
            ".": (6, 2), 0: (6, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.operations1 = {"*": "\u00D7", "+": "+"}
        self.operations2 = {"/": "\u00F7", "-": "-"}
        self.trigonometric_operations = {"sin": "sin", "cos": "cos", "tan": "tan"}
        self.first_row = {"pi": "π", "log": "log", "ln": "ln", "abs": "abs", "e": "e"}
        self.perm_comb_symbol = {"P": "nPr", "C": "nCr"}
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        # BASIC BUTTONS
        self.create_digit_buttons()
        self.create_delete_button()
        self.create_equals_button()
        self.create_clear_button()
        self.create_additional_buttons()

    def create_additional_buttons(self):
        self.create_square_button()
        self.create_sqrt_button()
        self.create_cube_button()
        self.create_exp_button()
        self.create_right_parenthesis_button()
        self.create_left_parenthesis_button()
        self.create_ans_button()
        self.create_perm_and_comb_buttons()
        self.create_operator1_buttons()
        self.create_operator2_buttons()
        self.create_trigonometric_buttons()
        self.create_first_row_buttons()

    def create_first_row_buttons(self):
        i = 1
        for operator, symbol in self.first_row.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(column=i, row=0, sticky=tk.NSEW)
            i += 1

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator1_buttons(self):
        i = 4
        for operator, symbol in self.operations1.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_operator2_buttons(self):
        i = 4
        for operator, symbol in self.operations2.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i, column=5, sticky=tk.NSEW)
            i += 1

    def create_trigonometric_buttons(self):
        i = 1
        for operator, symbol in self.trigonometric_operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(column=i, row=1, sticky=tk.NSEW)
            i += 1

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def create_cube_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b3", bg="gray10", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=3, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg="firebrick3", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="del", bg="firebrick3", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    def create_right_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg="gray10", fg="ghost white",
                           font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=5, sticky=tk.NSEW)

    def create_left_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg="gray10", fg="ghost white",
                           font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_perm_and_comb_buttons(self):
        i = 4
        for operator, symbol in self.perm_comb_symbol.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white",
                               font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(column=i, row=2, sticky=tk.NSEW)
            i += 1

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="chocolate1", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=5, sticky=tk.NSEW)

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text="Ans", bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=4, sticky=tk.NSEW)

    def create_exp_button(self):
        button = tk.Button(self.buttons_frame, text="EXP", bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=6, column=3, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="gray37",
                               fg="lavender", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="gray37",
                         fg="lavender", padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

        
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
