import customtkinter as ctk
from customtkinter import filedialog
import os

# Class for the main application
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # set aesthetics
        self.title("Marionette App - Setup Assistant")
        icon_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        ctk.set_appearance_mode("System")

        # Create and pack the TabFrame
        self.tab_frame = TabFrame(self, self.update_content)
        self.tab_frame.pack(side="left", fill="y")

        # Create and pack the ContentFrame
        self.content_frame = ContentFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Set the default tab
        self.update_content("Validate")

    def update_content(self, tab_name):
        # Update the contents in the ContentFrame
        self.content_frame.update_for_tab(tab_name)
        # Update tab button colors
        self.tab_frame.update_tab_colors(tab_name)

# Class for the tab frame
class TabFrame(ctk.CTkFrame):
    def __init__(self, master, update_callback):
        super().__init__(master)
        # Report and update the current tab
        self.update_callback = update_callback

        # buttons as tabs
        self.blanklabel = ctk.CTkLabel(self, text="")
        self.blanklabel.pack(pady=10, padx=10)

        self.tab1 = ctk.CTkButton(self, text="Validate",command=lambda: self.update_callback("Validate"))
        self.tab1.pack(pady=5, padx=10, fill="both", expand=True)

        self.tab2 = ctk.CTkButton(self, text="Build",command=lambda: self.update_callback("Build"))
        self.tab2.pack(pady=5, padx=10, fill="both", expand=True)

        self.tab3 = ctk.CTkButton(self, text="Distribute",command=lambda: self.update_callback("Distribute"))
        self.tab3.pack(pady=5, padx=10, fill="both", expand=True)

        self.tab4 = ctk.CTkButton(self, text="Report",command=lambda: self.update_callback("Report"))
        self.tab4.pack(pady=5, padx=10, fill="both", expand=True)
        
        # Toggle
        self.toggle1 = ctk.CTkSwitch(self, text="Toggle", command=self.toggle_appearance_mode)
        self.toggle1.pack(pady=25, padx=10, fill="both", )
    
    def update_tab_colors(self, active_tab):
        #default_color = "#1F6AA5"  # Blue
        default_color = '"#A0A0A0", "#505050"' # Grey
        selected_color = "#324B6E" # Dark Blue

        self.tab1.configure(fg_color=("#A0A0A0", "#505050"))
        self.tab2.configure(fg_color=("#A0A0A0", "#505050"))
        self.tab3.configure(fg_color=("#A0A0A0", "#505050"))
        self.tab4.configure(fg_color=("#A0A0A0", "#505050"))

        if active_tab == "Validate":
            self.tab1.configure(fg_color=selected_color)
        elif active_tab == "Build":
            self.tab2.configure(fg_color=(selected_color))
        elif active_tab == "Distribute":
            self.tab3.configure(fg_color=selected_color)
        elif active_tab == "Report":
            self.tab4.configure(fg_color=selected_color)

    def toggle_appearance_mode(self):
        # Toggle between light and dark modes
        if self.toggle1.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def show_validate_widgets():
        self.content_frame.Clear()

# Class for the content frame
class ContentFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create and pack the TitleFrame
        self.title_frame = TitleFrame(self)
        self.title_frame.pack(fill="x", pady=10, padx=10, side="top")

        # Create and pack the OutputFrame
        self.output_frame = OutputFrame(self)
        self.output_frame.pack(fill="both", expand=True, pady=5, padx=10)

        # Create and pack the InputFrame
        self.input_frame = InputFrame(self)
        self.input_frame.pack(fill="x", pady=10, padx=10, side="bottom")

    def update_for_tab(self, tab_name):
        if tab_name == "Validate":
            self.title_frame.update_title("Validate Data")
            self.output_frame.update_output("")
            self.input_frame.update_input("Click here to select file...","Validate")
            self.title_frame.update_combobox(["Validate All", "Validate Branch", "Validate GCI"])
        if tab_name == "Build":
            self.title_frame.update_title("Job Builder")
            self.output_frame.update_output("")
            self.input_frame.update_input("Select File...","Build")
            self.title_frame.update_combobox(["EDIINV A/B", "CUSDEC A/B", "FLAGJOB", "ABRTSTRM", "TAKEDWN"])
        if tab_name == "Distribute":
            self.title_frame.update_title("Distribute Files")
            self.output_frame.update_output("")
            self.input_frame.update_input("Select File...","Distribute")
            self.title_frame.update_combobox(["All", "JOB", "DAT", "STREAM", "Validate"])
        if tab_name == "Report":
            self.title_frame.update_title("Generate Report")
            self.output_frame.update_output("")
            self.input_frame.update_input("Select File...","Save")
            self.title_frame.update_combobox(["Markdown"])

# Class for the title frame (inside of Content Frame)
class TitleFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.title = ctk.CTkLabel(self, text="Current Tab Title", font=("Calibri", 20, "bold"))
        self.title.pack(padx=10, expand=True, side="left")
        
        #combobox_var = ctk.StringVar(value="option 2")
        self.combobox1 = ctk.CTkComboBox(self, state="readonly")
        self.combobox1.pack(side="right")
    
    # Update the title text based on the selected tab
    def update_title(self, text):
        self.title.configure(text=text)
    
    # Update the combobox based on the selected tab
    def update_combobox(self, options):
        self.combobox1.configure(values=options)
        if options: # Ensure options actually exist
            self.combobox1.set(options[0]) # Set default option


# Class for the output frame (inside of Content Frame)
class OutputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.textbox = ctk.CTkLabel(self, text="", width=600, height=400)
        self.textbox.pack(pady=5, padx=10)

    def update_output(self, text):
        self.textbox.configure(text=text)

# Class for the input frame (inside of Content Frame)
class InputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.entry = ctk.CTkEntry(self, placeholder_text="Click here to select file...",)
        self.entry.pack(pady=10, padx=10,fill="x", expand=True, side="left")

        # Set Focus logic to open the dialog box
        self.dialog_open = False
        self.entry.bind("<FocusIn>", self.open_file_dialog)

        self.button = ctk.CTkButton(self, text="Enter")
        self.button.pack(pady=10, padx=10, side="right")
    
    def open_file_dialog(self, event):
        if not self.dialog_open:
            self.dialog_open = True
            file_path = filedialog.askopenfilename(title="Select File")
            self.button.focus_set()
            if file_path:
                self.entry.delete(0, "end")
                self.entry.insert(0, file_path)
            self.dialog_open = False


    def update_input(self, placeholder_text, button_text):
        self.entry.delete(0, "end")
        self.entry.insert(0, placeholder_text)
        self.button.configure(text=button_text)

if __name__ == "__main__":
    app = App()
    # Get the App Coordinates and lock in geometry
    #app.update()
    app.minsize(app.winfo_width(), app.winfo_height())
    x_cordinate = int((app.winfo_screenwidth() / 2) - (app.winfo_width() / 2))
    y_cordinate = int((app.winfo_screenheight() / 2) - (app.winfo_height() / 2))
    app.geometry("+{}+{}".format(x_cordinate-300, y_cordinate-200))
    app.resizable(False, False)

    for index in [0, 1, 2]:
        app.columnconfigure(index=index, weight=1)
        app.rowconfigure(index=index, weight=1)

    app.mainloop()
