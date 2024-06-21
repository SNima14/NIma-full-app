import CodeEditor
import NIMA_GUI
from customtkinter import *
from tkinter.messagebox import showerror

BTN_SIZE = 160

def main_setup() -> None:
    """
    MAIN FUCTION 
    =============
    for setup page
    """
    setup_window = CTk() # create setup window
    setup_window.geometry(f"400x300+{0}+{0}")

    def start_codeEditor_command() -> None: 
        """fuction for starting code editor"""
        start_codeEditor.pack_forget()
        start_NIMA_GUI.pack_forget()
        coolLabel.after(100, lambda: coolLabel.configure(text="Wait"))
        coolLabel.after(1100, lambda: coolLabel.configure(text="Wait."))
        coolLabel.after(2100, lambda: coolLabel.configure(text="Wait.."))
        coolLabel.after(3100, lambda: coolLabel.configure(text="Wait..."))
        coolLabel.after(4000, close_window_for_codeEditor)

    def close_window_for_codeEditor() -> None:
        """start_codeEditor_command helper function """
        setup_window.destroy()
        main_codeEditor()

    def main_codeEditor() -> None:
        """start_codeEditor_command helper function """
        try:
            window_codeEditor = CodeEditor.MainWindow()
            window_codeEditor.mainloop()
        except Exception as e:
            showerror(title=f"can't open code editor !! because of {e}")

    def start_NIMA_GUI_command() -> None:
        """fuction for starting NIMA_GUI"""
        start_codeEditor.pack_forget()
        start_NIMA_GUI.pack_forget()
        coolLabel.after(100, lambda: coolLabel.configure(text="Wait"))
        coolLabel.after(1100, lambda: coolLabel.configure(text="Wait."))
        coolLabel.after(2100, lambda: coolLabel.configure(text="Wait.."))
        coolLabel.after(3100, lambda: coolLabel.configure(text="Wait..."))
        coolLabel.after(4000, close_window_for_NIMA_GUI)

    def close_window_for_NIMA_GUI() -> None:
        """start_NIMA_GUI_command helper function """
        setup_window.destroy()
        main_NIMA_GUI()

    def main_NIMA_GUI() -> None:
        """start_NIMA_GUI_command helper function """
        try:
            window_NIMA_GUI = NIMA_GUI.Window()
            window_NIMA_GUI.mainloop()
        except Exception as e:
            showerror(title=f"can't open code editor !! because of {e}")
    
    start_codeEditor = CTkButton(setup_window,text="start python code editor",width=BTN_SIZE,command=start_codeEditor_command)
    start_codeEditor.pack(pady=(5,0))

    start_NIMA_GUI = CTkButton(setup_window,text="start NIMA_GUI",width=BTN_SIZE,command=start_NIMA_GUI_command)
    start_NIMA_GUI.pack(pady=(5,0))

    coolLabel = CTkLabel(setup_window,text="",font=CTkFont(size=60))
    coolLabel.pack()

    setup_window.mainloop()

if __name__ == "__main__":
    main_setup()