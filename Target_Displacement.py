import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calculate_displacement():
    try:
        T = float(entry_period.get())
        soil_class = soil_class_combobox.get()

        if not soil_class:
            messagebox.showerror("Input Error", "Please select a soil class.")
            return

        # Constants for the formula based on soil class
        soil_constants = {
            "S1": (0.071, 0.014),
            "S2": (0.085, 0.017),
            "S3": (0.099, 0.020),
            "S4": (0.156, 0.053),
        }

        a, b = soil_constants[soil_class]
        D = a * T - b

        result_label.config(text=f"Target Displacement (D): {D:.4f} m")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical value for the fundamental period.")

# Create the main application window
app = tk.Tk()
app.title("Target Displacement Calculator")
app.geometry("600x500")
app.resizable(False, False)

# Title label
title_label = tk.Label(app, text="Target Displacement Calculator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Add an image spanning the width
try:
    img = Image.open("E:\\DESKTOP ACT\\Recherche LDMM\\py\\building2.png")
    img = img.resize((580, 150), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(app, image=photo)
    image_label.photo = photo
    image_label.pack(fill=tk.X, pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Frame for input fields
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

# Fundamental period input
period_label = tk.Label(input_frame, text="Fundamental Period (T):", font=("Arial", 12))
period_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_period = tk.Entry(input_frame, font=("Arial", 12))
entry_period.grid(row=0, column=1, padx=10, pady=5)

# Soil class selection
soil_class_label = tk.Label(input_frame, text="Soil Class:", font=("Arial", 12))
soil_class_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

soil_class_combobox = ttk.Combobox(input_frame, font=("Arial", 12), state="readonly")
soil_class_combobox["values"] = ["S1", "S2", "S3", "S4"]
soil_class_combobox.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(app, text="Calculate", font=("Arial", 14), command=calculate_displacement)
calculate_button.pack(pady=20)

# Result display
result_label = tk.Label(app, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the application
app.mainloop()
