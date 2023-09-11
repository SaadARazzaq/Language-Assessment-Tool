# Language-Assessment-Tool 🔊

The Language Assessment Tool is a Python application with a user-friendly graphical interface. It allows users to estimate their overall IELTS band score based on scores for the Listening, Speaking, Reading, and Writing sections.

![image](https://github.com/SaadARazzaq/Language-Assessment-Tool/assets/123338307/0fd27272-6473-4f4c-be0a-8143b1f298c0)

## Features 🌟

- **Interactive Sliders**: Easily select scores between 0 and 9 using intuitive sliders.

- **Real-time Updates**: Watch as the displayed values update in real-time while you adjust the scores.

- **Overall Score Calculation**: Press the "Calculate Band Score" button to get your estimated overall band score, rounded to the nearest 0.5.

## Getting Started 🚀

- Setup a Virtual environment
  ```bash
  python3 -m venv myenv
  ```
  ```bash
  myenv\Scripts\activate   # For Windows
  ```
  ```bash
  source myenv/bin/activate  # For Linux and Mac
  ```
  ```bash
  pip install tk
  ```
  
- Now run the `main.py` script.

## Customization 🛠️

Feel free to customize the application:

- **Slider Values**: Adjust the `slider_values` list to include specific score values that match your requirements.

- **GUI Styling**: Modify the appearance of the GUI, such as fonts, colors, and widget placement, to fit your preferences.

- **Scoring Methodology**: If you have a different scoring methodology, you can modify the `calculate_band_score` function accordingly.

## Dependencies 📦

- Python 3.x

## Usage 🖥️

1. Use the sliders to input your scores for Listening, Speaking, Reading, and Writing.

2. Click the "Calculate Band Score" button to see the estimated overall IELTS band score.

## Acknowledgments 🙏

Special thanks to the Tkinter library and the Python community for making this project possible. I am really thankful to ChatGPT as well to help me with the GUI of this project.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
