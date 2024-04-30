from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)


def calculate():
    """
    Converts the input miles value to kilometers and updates the kilometer_result_label with the result.
    """
    kilometer_result_label.config(text=f"{round(float(miles_input.get()) * 1.609, 2)}")

# Create an input field for the miles value
miles_input = Entry(width=12)
miles_input.grid(row=0, column=1)

# Create a button to calculate the conversion
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

# Create a label to display "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.config(padx=10, pady=10)
is_equal_label.grid(row=1, column=0)

# Create a label to display the converted kilometer value
kilometer_result_label = Label(text="0")
kilometer_result_label.config(padx=10, pady=10)
kilometer_result_label.grid(row=1, column=1)

# Create a label to display "Miles"
miles_label = Label(text="Miles")
miles_label.config(padx=10, pady=10)
miles_label.grid(row=0, column=2)

# Create a label to display "KM"
kilometer_label = Label(text="KM")
kilometer_label.config(padx=10, pady=10)
kilometer_label.grid(row=1, column=2)

window.mainloop()