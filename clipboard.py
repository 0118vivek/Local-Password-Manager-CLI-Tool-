# Password Copy with Auto-Clear

import pyperclip
import time
import threading

def copy_to_clipboard(data, timeout=10):
    pyperclip.copy(data)
    print(f"Password copied to clipboard. It will clear in {timeout} seconds.")
    def clear():
        time.sleep(timeout)
        pyperclip.copy("")
    threading.Thread(target=clear).start()
