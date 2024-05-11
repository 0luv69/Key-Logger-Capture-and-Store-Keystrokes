# Key Logger - Capture and Store Keystrokes

## Introduction

This Python script records user keystrokes for a specified duration, storing them in a designated folder. Customize logging time and access detailed documentation for seamless usage.

## Installation

1. Ensure Python is installed on your system.
2. Clone or download the repository containing the key logger code.
3. Navigate to the directory containing the code.

## Installation of Dependencies

1. Open a terminal or command prompt.
2. Use the following command to install required libraries:

`pip install -r requirements.txt`

## Usage

1. Open the terminal or command prompt.
2. Navigate to the directory containing the key logger code.
3. Run the script using Python:
   
`python key_logger.py`

## Customization

- Adjust the `Timeee` constant at the top of the script to specify the logging duration in seconds.

## Accessing Logs

- Logs are saved in a folder named "key logs" within the directory containing the script.
- Two files are generated:
- `Edited_<timestamp>.txt`: Contains formatted logs.
- `All_<timestamp>.txt`: Contains raw keystrokes.

## Exiting the Program

- The program automatically exits after the specified logging duration.
- To manually terminate the program, use the appropriate system command (e.g., Ctrl+C on Windows or Linux).

## Code Flow

The code for this key logger is designed to execute a continuous loop while capturing user keystrokes. It utilizes the `pynput.keyboard` library to monitor and record key events. 

Upon execution, the script initializes a listener to capture key presses (`on_press`), while the `on_release` function remains empty, allowing the program to continue running until manually terminated.

The `writter()` function is responsible for writing the captured keystrokes to text files. It creates a directory named "key logs" within the script's directory and saves two files: one with formatted logs and the other containing raw keystrokes.

The `caller()` function controls the duration of logging by introducing a delay based on the specified time constant (`Timeee`). After the specified duration, it triggers the `writter()` function to save the logs and exits the program.

The script utilizes global variables to store and manipulate keystroke data, facilitating seamless integration of key logging functionality.

