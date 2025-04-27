from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
from gender_prediction import emotion, ageAndgender  # Add this import
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, PhotoImage
from PIL import ImageTk, Image
names = set()


class MainUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Face Recognition System")
        self.resizable(False, False)
        self.geometry("500x250")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Main container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create main menu
        label = tk.Label(container, text="Face Recognition System", font=self.title_font, fg="#263942")
        label.grid(row=0, column=0, pady=20)

        detect_btn = tk.Button(container, text="Detect Faces", 
                             command=self.start_detection,
                             fg="#ffffff", bg="#263942",
                             width=20, height=2)
        detect_btn.grid(row=1, column=0, pady=10)

        add_user_btn = tk.Button(container, text="Add New User", 
                                command=self.add_user,
                                fg="#ffffff", bg="#263942",
                                width=20, height=2)
        add_user_btn.grid(row=2, column=0, pady=10)

        age_gender_btn = tk.Button(container, text="Age & Gender Detection", 
                                 command=self.age_gender_detection,
                                 fg="#ffffff", bg="#263942",
                                 width=20, height=2)
        age_gender_btn.grid(row=3, column=0, pady=10)

        emotion_btn = tk.Button(container, text="Emotion Detection", 
                              command=self.emotion_detection,
                              fg="#ffffff", bg="#263942",
                              width=20, height=2)
        emotion_btn.grid(row=4, column=0, pady=10)

        quit_btn = tk.Button(container, text="Quit", 
                           command=self.on_closing,
                           fg="#263942", bg="#ffffff",
                           width=20, height=2)
        quit_btn.grid(row=5, column=0, pady=10)

    def start_detection(self):
        messagebox.showinfo("INFO", "Starting face recognition for all users\n\nPress 'q' to quit recognition window")
        results = main_app()  # Get the results
        if results:
            result_message = "\n".join([f"{name}: {confidence:.2f}%" for name, confidence in results])
            messagebox.showinfo("Detection Results", f"Recognized Users:\n{result_message}")
        else:
            messagebox.showinfo("Detection Results", "No faces recognized.")

    def add_user(self):
        # Create a new window for user addition
        add_window = tk.Toplevel(self)
        add_window.title("Add New User")
        add_window.geometry("400x200")
        
        tk.Label(add_window, text="Enter name:", font='Helvetica 12 bold').pack(pady=10)
        name_entry = tk.Entry(add_window, font='Helvetica 11')
        name_entry.pack(pady=5)

        def start_capture_process():
            name = name_entry.get()
            if name == "None" or name == "" or name in names:
                messagebox.showerror("Error", "Invalid name or user already exists!")
                return
            
            add_window.destroy()
            messagebox.showinfo("INSTRUCTIONS", "We will capture 300 pictures of your face.")
            num_images = start_capture(name)
            
            if num_images >= 300:
                train_classifer(name)
                names.add(name)
                messagebox.showinfo("Success", "User added and model trained successfully!")
            else:
                messagebox.showerror("Error", "Not enough images captured!")

        tk.Button(add_window, text="Start Capture", 
                 command=start_capture_process,
                 fg="#ffffff", bg="#263942").pack(pady=20)

    def age_gender_detection(self):
        messagebox.showinfo("INFO", "Starting age and gender detection.\n\nPress 'q' to quit.")
        ageAndgender()

    def emotion_detection(self):
        messagebox.showinfo("INFO", "Starting emotion detection.\n\nPress 'q' to quit.")
        emotion()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            with open("nameslist.txt", "w") as f:
                for i in names:
                    f.write(i + " ")
            self.destroy()

if __name__ == "__main__":
    app = MainUI()
    try:
        icon = Image.open('icon.png')
        icon_render = ImageTk.PhotoImage(icon)
        app.iconphoto(True, icon_render)
    except:
        pass
    app.mainloop()
