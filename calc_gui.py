import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DEFAULT_FONT_STYLE = ("Arial", 20)


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            ".": (5, 2), 0: (5, 1)
        }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        # BASIC BUTTONS
        self.create_digit_buttons()
        self.create_multiplication_button()
        self.create_addition_button()
        self.create_division_button()
        self.create_subtraction_button()
        self.create_delete_button()
        self.create_equals_button()
        self.create_clear_button()
        self.create_additional_buttons()

        #self.bind_keys()

    """ def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))"""

    def create_additional_buttons(self):
        self.create_square_button()
        self.create_sqrt_button()
        self.create_raise_button()
        self.create_exp_button()
        self.create_tan_button()
        self.create_cos_button()
        self.create_sin_button()
        self.create_logarithm_button()
        self.create_right_parenthesis_button()
        self.create_left_parenthesis_button()
        self.create_ans_button()
        self.create_ln_button()

    def create_raise_button(self):
        button = tk.Button(self.buttons_frame, text="^", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text="tan", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text="cos", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text="sin", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_logarithm_button(self):
        button = tk.Button(self.buttons_frame, text="log\u2081\u2080", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_ln_button(self):
        button = tk.Button(self.buttons_frame, text="ln", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=5, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)

        button.grid(row=2, column=4, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="del", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=2, column=5, sticky=tk.NSEW)

    def create_right_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=5, sticky=tk.NSEW)

    def create_left_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_division_button(self):
        button = tk.Button(self.buttons_frame, text="\u00F7", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    def create_multiplication_button(self):
        button = tk.Button(self.buttons_frame, text="\u00D7", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def create_addition_button(self):
        button = tk.Button(self.buttons_frame, text="+", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_subtraction_button(self):
        button = tk.Button(self.buttons_frame, text="-", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=4, column=5, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="gray37",
                               fg="gray0", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="gray37",
                         fg="gray0", padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221,)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="chocolate1", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=5, column=5, sticky=tk.NSEW)

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text="Ans", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=5, column=4, sticky=tk.NSEW)

    def create_exp_button(self):
        button = tk.Button(self.buttons_frame, text="EXP", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=5, column=3, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
