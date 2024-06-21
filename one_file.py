from customtkinter import * #TODO : It is improting all this things too
from tkinter.messagebox import showerror,showinfo
from typing import Any,Tuple                        
from Nimapydoc import MyDecorator as decorator
from sys import getsizeof
import sys
import io
from Nimapydoc import YourPersonalVersion
main__version__ = YourPersonalVersion(1,9,1)

######################################################
"""             code editor scope starts           """
######################################################
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

######################################################
"""              code editor scope ends            """
######################################################



######################################################
"""             NIMA_GUI scope starts              """
######################################################

python_text = """Python is a popular high-level programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python emphasizes code readability and simplicity, making it an excellent choice for beginners and experienced programmers alike.

Why Python?
Easy to Learn: Python has a simple and easy-to-understand syntax, making it ideal for beginners.
Versatile: Python can be used for a wide range of applications, including web development, data analysis, artificial intelligence, machine learning, scientific computing, and more.
Large Standard Library: Python comes with a vast standard library that provides modules and functions for various tasks, reducing the need to write code from scratch.
Community Support: Python has a large and active community of developers who contribute to its growth, share resources, and offer support through forums, tutorials, and documentation.
Cross-Platform: Python is available on multiple platforms, including Windows, macOS, and Linux, making it highly portable."""

java_text = """
Java is a high-level, object-oriented programming language developed by Sun Microsystems (now owned by Oracle Corporation) in the mid-1990s. It was designed with the principle of "Write Once, Run Anywhere" (WORA), meaning that Java programs can run on any device that has a Java Virtual Machine (JVM), regardless of the underlying hardware and software platform."""

cpp_text = """
C++ is a versatile and powerful programming language that was developed by Bjarne Stroustrup at Bell Labs in the late 1970s. It is an extension of the C programming language with added features for object-oriented programming (OOP). C++ is widely used in various domains, including systems programming, game development, embedded systems, scientific computing, and more. Here are some key features and characteristics of C++:

Object-Oriented Programming (OOP): C++ supports the core principles of object-oriented programming, including classes, objects, inheritance, encapsulation, and polymorphism. This allows developers to write modular, reusable, and maintainable code.
Efficiency and Performance: C++ is known for its efficiency and performance, making it suitable for applications that require low-level manipulation of hardware resources and high computational speed. C++ gives developers direct control over memory management and system resources.
Standard Template Library (STL): C++ includes a powerful standard library known as the Standard Template Library (STL), which provides a rich collection of data structures (such as vectors, lists, maps, and sets) and algorithms (such as sorting, searching, and mathematical operations). The STL enables developers to write code more efficiently by leveraging reusable components.
Compatibility with C: C++ is largely compatible with the C programming language, allowing developers to seamlessly integrate existing C code into C++ projects and vice versa. This interoperability makes it easier to leverage existing libraries and frameworks written in C.
Portability: C++ code can be compiled and executed on a wide range of platforms and operating systems, including Windows, macOS, Linux, and various embedded systems. This portability makes C++ suitable for developing cross-platform applications.
Community and Ecosystem: C++ has a large and active community of developers, which has led to the creation of numerous libraries, frameworks, and tools to support C++ development. Popular libraries include Boost, OpenGL, Qt, and many others.
Flexibility: C++ offers a high degree of flexibility, allowing developers to choose between different programming paradigms (procedural, object-oriented, and generic programming) based on the requirements of their projects. This flexibility makes C++ suitable for a wide range of application domains.
Complexity and Learning Curve: While C++ offers a lot of power and flexibility, it also has a steep learning curve and can be more complex compared to other programming languages. Developers need to have a good understanding of memory management, pointers, and other low-level concepts to write efficient and bug-free C++ code."""

csharp_text = """C# (pronounced "C sharp") is a modern, object-oriented programming language developed by Microsoft as part of its .NET initiative in the early 2000s. It is designed for building robust, scalable, and efficient applications for the Microsoft ecosystem, including desktop, web, mobile, cloud, and gaming platforms. Here are some key features and characteristics of C#:

Object-Oriented Programming (OOP): Like C++, C# is an object-oriented programming language that supports classes, objects, inheritance, encapsulation, and polymorphism. It provides a straightforward syntax for creating and working with objects and their behaviors.
Type Safety and Memory Management: C# offers strong type safety and automatic memory management through the use of a garbage collector. This helps prevent common programming errors related to memory leaks, null references, and type mismatches.
Unified Development Environment: C# is closely integrated with the Microsoft Visual Studio development environment, which provides powerful tools for coding, debugging, testing, and deploying C# applications. Visual Studio offers features such as IntelliSense, code refactoring, and built-in project templates to streamline development workflows.
Cross-Platform Development: While C# was originally developed for Windows-based platforms, Microsoft has expanded its reach by introducing .NET Core and later .NET 5, which are cross-platform frameworks that support C# development on Windows, macOS, and Linux. This allows developers to build applications that run on a variety of operating systems.
Extensive Frameworks and Libraries: C# benefits from a rich ecosystem of frameworks, libraries, and tools provided by the .NET platform. This includes the .NET Framework (for Windows-based applications), .NET Core (for cross-platform applications), ASP.NET (for web development), Xamarin (for mobile development), and Unity (for game development), among others. These frameworks enable developers to leverage pre-built components and APIs to accelerate development.
"""

html_text = """
HTML (Hypertext Markup Language) is the standard markup language used to create and design web pages. It provides the structure and content of a web page by using a set of elements and tags that define various components such as headings, paragraphs, images, links, forms, and more. Here are some key points about HTML:

Markup Language: HTML is a markup language, not a programming language. It consists of a set of markup tags that describe the structure of content on a web page. HTML tags are enclosed in angle brackets (< >) and usually come in pairs, with an opening tag and a closing tag.
Elements and Tags: HTML documents are built using elements, which are defined by tags. Tags are keywords enclosed in angle brackets that specify how content should be formatted or displayed. For example, the <p> tag is used to create paragraphs, <h1> to <h6> tags for headings, <img> tag for images, <a> tag for links, and so on.
Document Structure: Every HTML document starts with a <!DOCTYPE html> declaration, which specifies the HTML version and document type. The document structure typically includes the <html>, <head>, and <body> elements. The <html> element contains the entire HTML document, while the <head> element contains metadata such as the page title, character encoding, and links to external resources. The <body> element contains the main content of the web page.
Attributes: HTML tags can include attributes that provide additional information or specify behavior for elements. Attributes are added to the opening tag and consist of a name and a value. For example, the <img> tag includes attributes such as src (source) for specifying the image file, alt for alternative text, width and height for dimensions, and so on.
Semantic HTML: Semantic HTML refers to the practice of using HTML elements to convey the meaning and structure of content, rather than just its appearance. Semantic elements such as <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>, and <figure> provide context and clarity to the content, which is beneficial for accessibility, search engine optimization (SEO), and code maintainability."""


class Lastbar(CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        def gender_comand():
            text = self.state_var_gender_radio.get()
            self.gender_label.configure(text=text)
            pass

        def checkbox_comand():
            if self.checkbox1.get() == "nima" and self.checkbox2.get() == "hamed":
                self.wellcome_label.configure(text="wellcome nima and hamed")
            elif self.checkbox1.get() == "nima" and self.checkbox2.get() == "nothing":
                self.wellcome_label.configure(text="wellcome nima")
            elif self.checkbox1.get() == "nothing" and self.checkbox2.get() == "hamed":
                self.wellcome_label.configure(text="wellcome hamed")
            elif (
                self.checkbox1.get() == "nothing" and self.checkbox2.get() == "nothing"
            ):
                self.wellcome_label.configure(text="????!!!!")

        def mod_switch_comand():
            text = self.mod_switch.get()
            self.mod_switch.configure(text=text)

        def weird_comand():
            weird = CTk()
            weird.geometry("200x200")
            weird.title("weird")

            weird_label = CTkLabel(weird, text="weird")
            weird_label.pack(pady=30, padx=30)

            weird.mainloop()

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.main_frame = CTkFrame(self, fg_color="#FAFAD2")
        self.main_frame.grid(column=0, row=0, sticky="news")

        self.main_frame.grid_columnconfigure(index=0, weight=4)

        self.main_frame.grid_rowconfigure(index=0, weight=8)
        self.main_frame.grid_rowconfigure(index=1, weight=8)
        self.main_frame.grid_rowconfigure(index=2, weight=0)

        ######################################top1_frame
        self.top1frame = CTkFrame(self.main_frame, fg_color="light blue")
        self.top1frame.grid(column=0, row=0, sticky="news")

        self.radio_label = CTkLabel(
            self.top1frame, text="radio button group", text_color="black"
        )
        self.radio_label.pack(pady=(10, 0))

        self.state_var_gender_radio = StringVar(value="")

        self.radio_btn1 = CTkRadioButton(
            self.top1frame,
            text="male",
            text_color="black",
            variable=self.state_var_gender_radio,
            value="male",
            command=gender_comand,
        )
        self.radio_btn1.pack(pady=(10, 0))

        self.radio_btn2 = CTkRadioButton(
            self.top1frame,
            text="female",
            text_color="black",
            variable=self.state_var_gender_radio,
            value="female",
            command=gender_comand,
        )
        self.radio_btn2.pack(pady=(10, 0))

        self.gender_label = CTkLabel(
            self.top1frame, text="your gender", text_color="black"
        )
        self.gender_label.pack(pady=(10, 0))

        ######################################top2_frame
        self.top2frame = CTkFrame(self.main_frame, fg_color="peach puff")
        self.top2frame.grid(column=0, row=1, sticky="news")

        self.checkbox1 = CTkCheckBox(
            self.top2frame,
            text_color="black",
            border_color="black",
            text="nima",
            onvalue="nima",
            offvalue="nothing",
            command=checkbox_comand,
        )
        self.checkbox1.pack(pady=(10, 0))

        self.checkbox2 = CTkCheckBox(
            self.top2frame,
            border_color="black",
            text_color="black",
            text="hamed",
            onvalue="hamed",
            offvalue="nothing",
            command=checkbox_comand,
        )
        self.checkbox2.pack(pady=(10, 0))

        self.wellcome_label = CTkLabel(
            self.top2frame, text="user ?", text_color="black"
        )
        self.wellcome_label.pack(pady=(10, 0))

        self.mod_label = CTkLabel(self.top2frame, text="your mod:", text_color="black")
        self.mod_label.pack(pady=(20, 0))

        self.state_var_mod = StringVar(value="good")

        self.mod_switch = CTkSwitch(
            self.top2frame,
            text="good",
            onvalue="good",
            offvalue="bad",
            variable=self.state_var_mod,
            text_color="black",
            button_color="#191970",
            button_hover_color="#0000CD",
            command=mod_switch_comand,
        )
        self.mod_switch.pack(pady=(10, 0))

        ######################################bottom_frame
        self.bottomframe = CTkFrame(self.main_frame, fg_color="mint cream")
        self.bottomframe.grid(column=0, row=2, sticky="news")

        self.last_btn = CTkButton(
            self.bottomframe,
            text="last widget",
            text_color="black",
            border_width=5,
            border_color="black",
            fg_color="mint cream",
            command=weird_comand,
            hover_color="lavender",
        )
        self.last_btn.pack(pady=20, padx=20)


class Midbar(CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        def languages_combobox_comand(choice):
            if choice == "java":
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, text=java_text)

            elif choice == "c++":
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, text=cpp_text)

            elif choice == "HTML":
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, text=html_text)

            elif choice == "c#":
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, text=csharp_text)

            elif choice == "python":
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, text=python_text)

        def delete_btn_comand():
            self.textbox.delete(0.0, END)

        def submit_btn_comand():
            text = self.entry.get()

            try:
                text = int(text)
            except:
                print("error")
                showerror(title="error", message="invalid text")

            if text > 100 or text < 0:
                showerror(title="error", message="invalid number")
            else:
                self.state_slider_var1.set(value=text)
                self.state_slider_var2.set(value=text)
                self.state_slider_var3.set(value=text)

        def back_to_setup_comand():

            self.textbox.delete(0.0,END)
            self.textbox.after(100,lambda:self.textbox.insert(0.0,text="wait"))
            self.textbox.after(1100,lambda:self.textbox.insert(END,text="."))
            self.textbox.after(2100,lambda:self.textbox.insert(END,text="."))
            self.textbox.after(3100,lambda:self.textbox.insert(END,text="."))
            self.textbox.after(4000,close_NIMA_GUI_for_setup)

        def close_NIMA_GUI_for_setup():
            try:
                self.master.destroy()
            except Exception as e:
                showerror(title=type(e).__name__,message=e)
            finally:
                main_setup()


        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.main_frame = CTkFrame(self, fg_color="black")
        self.main_frame.grid(column=0, row=0, sticky="news")

        self.main_frame.grid_columnconfigure(index=0, weight=3)
        self.main_frame.grid_columnconfigure(index=1, weight=1)
        self.main_frame.grid_rowconfigure(index=0, weight=2)
        self.main_frame.grid_rowconfigure(index=1, weight=3)

        ##################################top_left
        self.top_left = CTkFrame(self.main_frame, fg_color="#157746")
        self.top_left.grid(column=0, row=0, sticky="news")

        self.top_left.grid_columnconfigure(index=0, weight=1)
        self.top_left.grid_rowconfigure(index=0, weight=1)

        self.textbox = CTkTextbox(
            self.top_left,
            wrap="word",
            fg_color="light sea green",
            text_color="black",
            font=CTkFont(size=14),
        )
        self.textbox.grid(pady=15, padx=15, sticky="news")

        ##################################top_right
        self.top_right = CTkFrame(self.main_frame, fg_color="dark cyan")
        self.top_right.grid(column=1, row=0, sticky="news")

        self.languages_combobox = CTkComboBox(
            self.top_right,
            values=["python", "c++", "c#", "HTML", "java"],
            command=languages_combobox_comand,
            variable=StringVar(self.top_right, value="choose a language"),
            width=160,
        )
        self.languages_combobox.pack(pady=(10, 0), padx=5)

        self.delete_btn = CTkButton(
            self.top_right, text="delete", width=160, command=delete_btn_comand
        )
        self.delete_btn.pack(pady=(15, 0), padx=5)

        self.back_to_setup_btn = CTkButton(
            self.top_right, text="back to main meun", width=160, command=back_to_setup_comand
        )
        self.back_to_setup_btn.pack(pady=(15, 0), padx=5)

        ##################################bottom
        self.bottom = CTkFrame(self.main_frame, fg_color="silver")
        self.bottom.grid(column=0, row=1, sticky="news", columnspan=2)

        self.bottom.grid_columnconfigure(index=0, weight=50)
        self.bottom.grid_columnconfigure(index=1, weight=0)
        self.bottom.grid_rowconfigure(index=0, weight=50)
        self.bottom.grid_rowconfigure(index=1, weight=0)

        self.left_top_of_bottom = CTkFrame(self.bottom, fg_color="pink")
        self.left_top_of_bottom.grid(
            column=0, row=0, sticky="news", padx=(0, 10), pady=(10, 0)
        )

        self.state_slider_var1 = DoubleVar(value=30)
        self.state_slider_var2 = DoubleVar(value=60)
        self.state_slider_var3 = DoubleVar(value=40)
        self.state_slider_var4 = DoubleVar(value=50)
        self.state_slider_var5 = DoubleVar(value=70)

        self.first_slider = CTkSlider(
            self.left_top_of_bottom,
            width=500,
            height=25,
            button_length=70,
            variable=self.state_slider_var1,
            from_=0,
            to=100,
        )
        self.first_slider.pack(pady=(40, 0), padx=5)

        self.secend_slider = CTkSlider(
            self.left_top_of_bottom,
            width=450,
            height=20,
            variable=self.state_slider_var2,
            from_=0,
            to=100,
        )
        self.secend_slider.pack(pady=(40, 0), padx=5)

        self.third_slider = CTkSlider(
            self.left_top_of_bottom,
            width=450,
            height=20,
            variable=self.state_slider_var3,
            from_=0,
            to=100,
        )
        self.third_slider.pack(pady=(30, 0), padx=5)

        self.submit_btn = CTkButton(
            self.left_top_of_bottom,
            text="submit your number",
            command=submit_btn_comand,
        )
        self.submit_btn.pack(side="bottom", pady=10)

        self.right_top_of_bottom = CTkFrame(self.bottom, fg_color="gray")
        self.right_top_of_bottom.grid(
            column=1, row=0, sticky="news", padx=(0, 0), pady=(10, 0)
        )

        self.fourth_slider = CTkSlider(
            self.right_top_of_bottom,
            orientation="vertical",
            height=300,
            width=18,
            from_=0,
            to=100,
            variable=self.state_slider_var4,
        )
        self.fourth_slider.pack(side="left", padx=(9, 7))

        self.fiveth_slider = CTkSlider(
            self.right_top_of_bottom,
            orientation="vertical",
            height=300,
            width=18,
            from_=0,
            to=100,
            variable=self.state_slider_var5,
        )
        self.fiveth_slider.pack(side="left", padx=(0, 9))

        self.bottom_of_bottom = CTkFrame(self.bottom, fg_color="#DB7093")
        self.bottom_of_bottom.grid(
            column=0, row=1, sticky="news", columnspan=2, pady=(10, 0)
        )

        self.bottom_of_bottom.grid_columnconfigure(index=0, weight=1)
        self.bottom_of_bottom.grid_rowconfigure(index=0, weight=1)

        self.entry = CTkEntry(
            self.bottom_of_bottom,
            placeholder_text="put your numer here (between 0 and 100)",
        )
        self.entry.grid(column=0, row=0, pady=7, padx=5, sticky="news")


class Sidebar(CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        def combobox1_comand(choice):
            set_appearance_mode(choice)

        self.widget_scaling_list = []

        for scale in range(1, 81, 10):
            n = 101 - scale
            self.widget_scaling_list.append(f"{n}%")

        self.grid_columnconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)

        self.main_frame = CTkFrame(self)
        self.main_frame.grid(column=0, row=0, rowspan=4, sticky="news")

        self.label_1 = CTkLabel(
            self.main_frame, text="nima homam", font=CTkFont(family="Algerian", size=15)
        )
        self.label_1.pack(pady=(15, 0))

        self.btn_1 = CTkButton(self.main_frame, text="click 1th", fg_color="#47A2A2")
        self.btn_1.pack(pady=(10, 0), padx=10)

        self.btn_2 = CTkButton(self.main_frame, text="click 2th")
        self.btn_2.pack(pady=(10, 0), padx=10)

        self.disabled_btn = CTkButton(
            self.main_frame, state="disabled", text="disabled btn"
        )
        self.disabled_btn.pack(pady=(10, 0), padx=10)

        self.combobox2 = CTkComboBox(self.main_frame, values=self.widget_scaling_list)
        self.combobox2.pack(side="bottom", pady=(0, 10))

        self.widget_scaling_label = CTkLabel(self.main_frame, text="Widget scaling:")
        self.widget_scaling_label.pack(side="bottom", pady=(0, 5))

        self.combobox1 = CTkComboBox(
            self.main_frame,
            values=["dark", "light", "system"],
            command=combobox1_comand,
        )
        self.combobox1.pack(side="bottom", pady=(0, 10))

        self.appearance_mode_label = CTkLabel(self.main_frame, text="Appearance mode")
        self.appearance_mode_label.pack(side="bottom", pady=(0, 5))


class Window(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry("1000x550")
        self.title("Nima App")

        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=3)
        self.grid_columnconfigure(index=2, weight=1)

        self.grid_rowconfigure(index=(0, 1), weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(column=0, row=0, sticky="news", rowspan=2)

        self.midbar = Midbar(self)
        self.midbar.grid(column=1, row=0, sticky="news", rowspan=2)

        self.lastbar = Lastbar(self)
        self.lastbar.grid(column=2, row=0, sticky="news", rowspan=2)
######################################################
"""               NIMA_GUI scope ends              """
######################################################



######################################################
"""                setup scope starts              """
######################################################
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
            window_codeEditor = MainWindow()
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
            window_NIMA_GUI = Window()
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
######################################################
"""                 setup scope ends               """
######################################################