import tkinter as tk
from tkinter import ttk
import keyboard
import pyautogui
import time


class AutoTyperApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Autotyper")
        self.geometry("500x250")

        ttk.Label(self, text="Text to type:").pack(pady=10)

        self.text_entry = tk.Text(self, height=5, width=40)
        self.text_entry.pack(pady=10)

        ttk.Label(self, text="Shortcut key (e.g., ctrl+shift+a):").pack(pady=10)

        self.shortcut_entry = ttk.Entry(self)
        self.shortcut_entry.pack(pady=10)

        ttk.Label(self, text="Initial delay (seconds):").pack(pady=10)
        self.delay_var = tk.DoubleVar(value=0.1)  # default value of 0.1 seconds
        self.delay_entry = ttk.Entry(self, textvariable=self.delay_var)
        self.delay_entry.pack(pady=10)

        self.start_btn = ttk.Button(self, text="Start Listening", command=self.start_listening)
        self.start_btn.pack(pady=10)

        self.shortcut_key = ""

    def start_listening(self):
        self.shortcut_key = self.shortcut_entry.get()

        if not self.shortcut_key:
            print("Please enter a shortcut key.")
            return

        self.start_btn["state"] = "disabled"
        self.shortcut_entry["state"] = "disabled"
        self.text_entry["state"] = "disabled"
        self.delay_entry["state"] = "disabled"

        print(f"Listening for {self.shortcut_key} ...")

        # Using a lambda to avoid passing arguments
        keyboard.add_hotkey(self.shortcut_key, lambda: self.type_text())

    def type_text(self):
        # Add the delay
        time.sleep(self.delay_var.get())

        # Retrieve text from Text widget
        text_to_type = self.text_entry.get("1.0", tk.END)

        # Break the text into lines
        lines = text_to_type.splitlines()

        # Iterate over lines and type each one
        for i, line in enumerate(lines):
            linef = ""
            # remove all spaces from the start of the line until a character is found
            for char in line:
                if char != " ":
                    linef += char
                else:
                    break
            line = linef

            pyautogui.write(line)

            # If it's not the last line, simulate pressing "Enter"
            if i != len(lines) - 1:
                pyautogui.press('enter')


if __name__ == "__main__":
    app = AutoTyperApp()
    app.mainloop()

