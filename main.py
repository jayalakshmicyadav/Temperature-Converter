import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# GUI Functionality
def convert_temperature():
    try:
        temp = float(entry_temp.get())  # Get temperature input
        unit = unit_var.get()          # Get selected unit

        if unit == "Celsius":
            result.set(f"{temp} °C = {celsius_to_fahrenheit(temp):.2f} °F\n"
                       f"{temp} °C = {celsius_to_kelvin(temp):.2f} K")
        elif unit == "Fahrenheit":
            result.set(f"{temp} °F = {fahrenheit_to_celsius(temp):.2f} °C\n"
                       f"{temp} °F = {fahrenheit_to_kelvin(temp):.2f} K")
        elif unit == "Kelvin":
            result.set(f"{temp} K = {kelvin_to_celsius(temp):.2f} °C\n"
                       f"{temp} K = {kelvin_to_fahrenheit(temp):.2f} °F")
        else:
            messagebox.showerror("Error", "Invalid unit selection.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric temperature.")

# Tkinter GUI setup with modern styling
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("550x450")
root.config(bg="#F0F8FF")  # Light background for the window

# Styling Variables
bg_color = "#8dc9e3"  # Light blue background color
fg_color = "#F5FFFA"  # White foreground
entry_bg = "#F0FFF0"  # Light gray for entry fields
button_bg = "#F5FFFA"  # Soft teal color for buttons
button_fg = "#555D50"  # White button text
label_bg = "#D8BFD8"   # White background for labels

# Input Section
frame_input = ttk.Frame(root, padding=(10, 50), style="TFrame")
frame_input.grid(row=0, column=0, sticky="EW", padx=30, pady=20)

ttk.Label(frame_input, text="Enter Temperature:", font=("Monaco", 14), background=label_bg).grid(row=0, column=0, padx=10, pady=8, sticky="w")
entry_temp = ttk.Entry(frame_input, width=18, font=("Monaco", 14), background=entry_bg, justify="center")
entry_temp.grid(row=0, column=1, padx=10, pady=8)

ttk.Label(frame_input, text="Select Unit:", font=("Monaco", 14), background=label_bg).grid(row=1, column=0, padx=10, pady=8, sticky="w")
unit_var = tk.StringVar(value="Celsius")
combo_units = ttk.Combobox(frame_input, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], style="RoundedCombobox.TCombobox",state="readonly", font=("Monaco", 14), width=20)
combo_units.grid(row=1, column=1, padx=10, pady=8 )

# Convert Button
btn_convert = ttk.Button(frame_input, text="Convert", command=convert_temperature, style="TButton")
btn_convert.grid(row=2, column=0, columnspan=2, pady=20)

# Result Display
frame_result = ttk.Frame(root, padding=(10,100), style="TFrame")
frame_result.grid(row=1, column=0, sticky="EW", padx=30)

ttk.Label(frame_result, text="Conversion Results:", font=("Monaco", 14), background=label_bg).grid(row=0, column=0, padx=10, pady=8, sticky="w")
result = tk.StringVar(value="Result")
label_result = ttk.Label(frame_result, textvariable=result, font=("Monaco", 14), background="#ffffff", anchor="center", width=40, padding=15)
label_result.grid(row=1, column=0, padx=10, pady=8)

# Define custom styles for widgets
style = ttk.Style()
style.configure("TButton", font=("Monaco", 14), padding=(10, 8), background=button_bg, foreground=button_fg)
style.configure("TLabel", font=("Monaco", 14), background=label_bg, padding=10)
style.configure("TFrame", background="#E6E6FA")

# Run the application
root.mainloop()
