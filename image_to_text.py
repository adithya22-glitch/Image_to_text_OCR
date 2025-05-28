import os
import sys
import cv2
import numpy as np
import pyautogui
import pytesseract
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import time

# ---------- Portable Resource Path Helper ----------
def resource_path(relative_path):
    """Get absolute path to resource (works for dev and PyInstaller)"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ---------- Configure Tesseract Path ----------
pytesseract.pytesseract.tesseract_cmd = resource_path("bin/tesseract.exe")

# ---------- Timestamp Helper ----------
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# ---------- OCR Processing ----------
def process_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img).strip()
    show_text_window(text)

# ---------- Display Extracted Text GUI ----------
def show_text_window(text):
    top = tk.Toplevel(root)
    top.title("Extracted Text")
    top.geometry("600x400")

    txt = tk.Text(top, wrap="word", font=("Consolas", 11))
    txt.insert("1.0", text)
    txt.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(top, command=txt.yview)
    scrollbar.pack(side="right", fill="y")
    txt.config(yscrollcommand=scrollbar.set)

    def ask_save():
        save = messagebox.askyesno("Save Output", "Do you want to save the extracted text as a .txt file?", parent=top)
        if save:
            filename = f"extracted_text_{get_timestamp()}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"Text saved to:\n{filename}", parent=top)

    top.after(500, ask_save)

# ---------- Snipping Tool Mimic ----------
def capture_snippet():
    root.withdraw()
    time.sleep(0.5)

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    selecting = [False]
    rect = [0, 0, 0, 0]

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            selecting[0] = True
            rect[0], rect[1] = x, y
        elif event == cv2.EVENT_MOUSEMOVE and selecting[0]:
            rect[2], rect[3] = x, y
            temp = screenshot_cv.copy()
            cv2.rectangle(temp, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
            cv2.imshow("Snip Screen", temp)
        elif event == cv2.EVENT_LBUTTONUP:
            selecting[0] = False
            rect[2], rect[3] = x, y
            cv2.destroyWindow("Snip Screen")

            x1, y1 = min(rect[0], rect[2]), min(rect[1], rect[3])
            x2, y2 = max(rect[0], rect[2]), max(rect[1], rect[3])
            cropped = screenshot_cv[y1:y2, x1:x2]

            snippet_path = "snippet.png"
            cv2.imwrite(snippet_path, cropped)

            root.deiconify()
            process_image(snippet_path)

    cv2.imshow("Snip Screen", screenshot_cv)
    cv2.setMouseCallback("Snip Screen", mouse_callback)
    cv2.waitKey(0)

# ---------- File Select Option ----------
def select_image_file():
    root.withdraw()
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if filepath:
        process_image(filepath)
    root.deiconify()

# ---------- GUI Button Handler ----------
def on_button_click(option):
    if option == "snippet":
        capture_snippet()
    elif option == "select":
        select_image_file()
    elif option == "exit":
        root.quit()

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Image to Text (OCR)")
root.geometry("300x200")
root.attributes('-topmost', False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Choose an Option", font=("Arial", 14)).pack(pady=10)
tk.Button(frame, text="Snippet", width=20, command=lambda: on_button_click("snippet")).pack(pady=5)
tk.Button(frame, text="Select Image File", width=20, command=lambda: on_button_click("select")).pack(pady=5)
tk.Button(frame, text="Exit", width=20, command=lambda: on_button_click("exit")).pack(pady=5)

root.mainloop()