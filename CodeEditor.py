from Nimapydoc import YourPersonalVersion
from customtkinter import * #TODO : It is improting all this things too
from typing import Tuple
from tkinter.messagebox import showerror, showinfo
from Nimapydoc import MyDecorator as decorator
from sys import getsizeof
import sys
import io
main__version__ = YourPersonalVersion(1,1,1)


class CodeEditor(CTkTextbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Return>", self.auto_indent)
        self.bind("<Tab>", self.indent)
        self.bind("<Shift-Tab>", self.unindent)

    def auto_indent(self, event=None):
        """
        Automatically indents the next line based on the current line's indentation.
        """
        current_line = self.get("insert linestart", "insert lineend")
        indentation = len(current_line) - len(current_line.lstrip())

        # Insert newline
        self.insert("insert", "\n" + " " * indentation)

        # Prevent default behavior
        return "break"

    def indent(self, event=None):
        """
        Inserts a tab character or spaces at the cursor position.
        """
        self.insert("insert", " " * 4)  # Using 4 spaces for a tab
        return "break"  # Prevent default behavior

    def unindent(self, event=None):
        """
        Removes an indentation level.
        """
        current_line = self.get("insert linestart", "insert")
        if current_line.startswith(" " * 4):
            self.delete("insert linestart", "insert linestart + 4c")
        return "break"


class MainWindow(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        @decorator.timer
        def execute():
            execute_text = self.textbox1.get("1.0", END)
            # Redirect stdout and stderr to a StringIO object
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = mystdout = io.StringIO()
            sys.stderr = mystderr = io.StringIO()
            try:
                exec(execute_text)
            except Exception as e:
                showerror(title=type(e).__name__,message=e)
            # Reset stdout and stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            # Display the output in the output text box
            self.output_textbox.delete("1.0", END)
            self.output_textbox.insert(END, mystdout.getvalue() + mystderr.getvalue())

        def exit_command():
            self.destroy()
            showinfo(title="exiting...",message="exited secssusfully")

        self.title("Nima python code editor")
        self.geometry(f"600x500+{int(self.winfo_screenwidth()/2) - 200}+{int(self.winfo_screenheight()/2) - 250}")
        self.minsize(width=550,height=490)

        # Configure the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.textbox1 = CodeEditor(
            self,
            width=450,
            height=180,
            corner_radius=2,
            activate_scrollbars=True,
            wrap="word",
            font=CTkFont(family="Fira Code",size=13)
        )
        self.textbox1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.btn1 = CTkButton(
            self, width=140, height=28, text="Execute Code", command=execute
        )
        self.btn1.grid(row=1, column=0, columnspan=2, padx=10, pady=(5,0),sticky="n")
        self.nimalabel=CTkLabel(self,text="Autor: Nima Homam!",font=CTkFont(family="Fira Code",size=15))
        self.nimalabel.grid(row=1,column=0,columnspan=2,padx=8,sticky="w")

        self.output_textbox = CTkTextbox(
            self,
            width=450,
            height=180,
            corner_radius=2,
            activate_scrollbars=True,
            wrap="word",
            state="normal",
        )
        self.output_textbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.exit_btn = CTkButton(self, text="Exit the Program", command=exit_command)
        self.exit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=(5,0),sticky="n")


def main_codeEditor():
    wind = MainWindow()
    print(getsizeof(wind))

    wind.mainloop()
