# Automated Feedback Filler for Academia SRM
This script provides a simple way to automate the process of filling feedback using the pynput library in Python. By running this script, the cursor will automatically move through a series of feedback fields, pressing the down arrow key and tab key as necessary.


## Prerequisites
1. `Python 3.x`

2. `pynput library`

## Installation
1. Install Python 3.x from the official Python website: https://www.python.org/downloads/

2. Install the pynput library by running the following command:
```
pip install pynput
```

3. Copy the code from the provided file `(feedback_filler.py)` into a Python file.

4. Run the Python script.

5. Ensure that the cursor is positioned at the first index position in the feedback field.

6. The script will automatically move the cursor through each feedback field, pressing the down arrow key and tab key as necessary to fill the feedback.

7. Customize the script as needed to adjust the timing between key presses or the number of down arrow key presses.

### Note: 
The script assumes that the feedback fields are sequential and the down arrow key needs to be pressed multiple times to reach the next field. Modify the 'fill_feedback' function accordingly if your feedback fields have a different layout or require different key presses to navigate.


## Contributing
If you find any issues or have any suggestions for improvement, feel free to create a pull request or open an issue.


## License
This project is licensed under the `MIT License` - see the License file for details.
