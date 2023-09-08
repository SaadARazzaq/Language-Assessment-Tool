import tkinter as tk
from tkinter import ttk

# Function to calculate the overall band score
def calculate_band_score():
    listening_score = sliders[0]["slider"].get()
    speaking_score = sliders[1]["slider"].get()
    reading_score = sliders[2]["slider"].get()
    writing_score = sliders[3]["slider"].get()

    overall_score = (listening_score + speaking_score + reading_score + writing_score) / 4

    # Round the calculated overall score to the nearest 0.5
    overall_score = round(overall_score * 2) / 2

    # Display the calculated overall score
    result_label.config(text=f"Overall Band Score: {overall_score:.1f}")

root = tk.Tk()
root.title("IELTS Band Score Calculator")

# Create a frame
frame = ttk.Frame(master=root, padding=20)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create sliders for setting scores with labels
sliders = [
    {"label": "Listening", "row": 0},
    {"label": "Speaking", "row": 1},
    {"label": "Reading", "row": 2},
    {"label": "Writing", "row": 3},
]

# Define the custom values for the sliders
slider_values = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]

def update_slider_value(slider, value_label):
    # Get the current slider value
    value = slider.get()
    
    # Find the closest custom value
    closest_value = min(slider_values, key=lambda x: abs(x - value))
    
    # Set the slider value to the closest custom value
    slider.set(closest_value)
    
    # Update the label text
    value_label.config(text=f"{closest_value:.1f}")

for idx, slider_info in enumerate(sliders):
    label_text = slider_info["label"] + " Score:"
    row = slider_info["row"]

    label = ttk.Label(frame, text=label_text)
    label.grid(column=0, row=row, padx=10, pady=5, sticky=tk.W)

    slider = ttk.Scale(frame, from_=0, to=9, orient="horizontal", length=200)
    slider.grid(column=1, row=row, padx=10, pady=5)
    slider.set(0)  # Set the initial value to 0

    value_label = ttk.Label(frame, text="0.0")
    value_label.grid(column=2, row=row, padx=5)

    # Bind slider movement to update the value labels
    slider.bind("<Motion>", lambda event, slider=slider, label=value_label: update_slider_value(slider, label))
    
    sliders[idx]["slider"] = slider  # Store the slider in the sliders dictionary

# Create a button to calculate the overall band score
calculate_button = ttk.Button(frame, text="Calculate Band Score", command=calculate_band_score)
calculate_button.grid(column=0, row=4, columnspan=2, pady=10)

# Create a label to display the calculated overall score
result_label = ttk.Label(frame, text="", font=("Helvetica", 16))
result_label.grid(column=0, row=5, columnspan=3, pady=10)

# Disable window resizing as well as maximizing
root.resizable(False, False)

# Start the Tkinter main event loop
root.mainloop()
