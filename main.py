from tkinter import Tk, Label, Text, Button, Scrollbar, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from spellchecker import SpellChecker

class SpellCheckerGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Spell Checker")

        self.text_area = Text(self.window, height=20, width=80)
        self.text_area.pack()

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)

        self.spell_checker = SpellChecker()

        self.check_button = Button(self.window, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack()

        self.correct_button = Button(self.window, text="Correct Spelling", command=self.correct_spelling)
        self.correct_button.pack()

        self.save_button = Button(self.window, text="Save", command=self.save_file)
        self.save_button.pack()

        self.load_button = Button(self.window, text="Load", command=self.load_file)
        self.load_button.pack()

    def check_spelling(self):
        text = self.text_area.get("1.0", "end-1c")
        words = text.split()

        misspelled_words = self.spell_checker.unknown(words)

        if len(misspelled_words) == 0:
            messagebox.showinfo("Spell Checker", "No spelling errors found.")
        else:
            message = "Spelling errors found:\n\n"
            for word in misspelled_words:
                message += f"{word}\n"
            messagebox.showwarning("Spell Checker", message)

    def correct_spelling(self):
        text = self.text_area.get("1.0", "end-1c")
        words = text.split()

        corrected_text = ""
        for word in words:
            corrected_word = self.spell_checker.correction(word)
            corrected_text += corrected_word + " "

        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", corrected_text)

    def save_file(self):
        text = self.text_area.get("1.0", "end-1c")
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
                messagebox.showinfo("Spell Checker", "File saved successfully.")

    def load_file(self):
        file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("end", text)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    spell_checker_gui = SpellCheckerGUI()
    spell_checker_gui.run()
