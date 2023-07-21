import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    input_temperature = float(input_entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    if from_unit == to_unit:
        result_label["text"] = str(input_temperature)
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result_label["text"] = str(celsius_to_fahrenheit(input_temperature))
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result_label["text"] = str(celsius_to_kelvin(input_temperature))
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result_label["text"] = str(fahrenheit_to_celsius(input_temperature))
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result_label["text"] = str(fahrenheit_to_kelvin(input_temperature))
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result_label["text"] = str(kelvin_to_celsius(input_temperature))
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result_label["text"] = str(kelvin_to_fahrenheit(input_temperature))

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Create input entry
input_entry = tk.Entry(root, font=("Helvetica", 16))
input_entry.pack(pady=20)

# Create "From" unit dropdown
from_unit_var = tk.StringVar()
from_unit_var.set("Celsius")
from_unit_dropdown = tk.OptionMenu(root, from_unit_var, "Celsius", "Fahrenheit", "Kelvin")
from_unit_dropdown.pack()

# Create "To" unit dropdown
to_unit_var = tk.StringVar()
to_unit_var.set("Fahrenheit")
to_unit_dropdown = tk.OptionMenu(root, to_unit_var, "Celsius", "Fahrenheit", "Kelvin")
to_unit_dropdown.pack()

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=20)

# Create the result label
result_label = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 16))
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()
