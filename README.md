# Image to Text (OCR) - Portable Python GUI App

---

## Overview

This is a lightweight, portable Python GUI application that performs OCR (Optical Character Recognition) using Tesseract. It allows you to either capture a screen snippet or select an image file and instantly extract text.

You can use `image_to_text.exe` independently without needing Python installed. Just double-click and start using it.

Alternatively, you can run `image_to_text.py` with the `bin` folder present in the same directory.

I wrote this because it was annoying to visit online websites to use image-to-text tools repeatedly. It's not that I didn't trust the websites—it just wasn't the best solution for a recurring issue.

Although there is a related project in [https://github.com/zstrathe/tesseract\_portable\_windows](https://github.com/zstrathe/tesseract_portable_windows) (not a hyperlink), it was not optimized for ease of use. I took inspiration from that project but built this tool with a more seamless GUI and cleaner integration.

---

## Features

* Screen snippet tool to select a region and extract text
* Upload image files and extract text
* Output is shown in a resizable GUI window
* Option to save extracted text to a `.txt` file
* Fully portable — requires no installation beyond Python and dependencies (or use the `.exe`)

---

## File Structure

```

Tesseract_Portable/
├── image_to_text.py           # Main Python script
├── image_to_text.exe          # Compiled executable (optional)
├── requirements.txt           # Dependencies
└── bin/                       # Contains Tesseract binaries and trained data
    ├── tesseract.exe
    ├── tessdata/
    │   └── eng.traineddata
    └── [...DLLs, tools, configs...]
```

---

## Dependencies

These are the exact versions used:

```
numpy==2.0.2
opencv-python==4.11.0.86
pytesseract==0.3.13
PyAutoGUI==0.9.54
pillow==11.2.1
```

---

## How to Use

1. Make sure `tesseract.exe` is present in the `bin/` directory.

2. Run `image_to_text.py` using Python **or** use the provided `.exe`.

3. Choose either:

   * **Snippet** to take a screenshot area, **or**
   * **Select Image File** to upload an image

4. Text will appear in a new window with an option to save it.

5. Download 'image_to_text.exe' from the releases tab. For those who aren’t familiar with using GitHub, you can directly download the .exe file from this link and run it without any setup:

**https://github.com/adithya22-glitch/Image_to_text_OCR/releases/download/v1.0.0/image_to_text.exe**

---

## Notes

* Tesseract version: 5.3.2 (downloaded from https://github.com/UB-Mannheim/tesseract/wiki)
* Tesseract path is auto-set from the local `bin/` folder. No installation required.
* Works only on Windows.
* Its advisable to run  `tesseract.exe` file  with the `bin` folder present.
* If you want the extracted text to be stored in a '.txt' file, you can click on 'yes' on this 'Save Output' window. the '.txt' file will be saved in the same directory the 'image_to_text.exe' or 'image_to_text.py' file will be run on.
  ![image](https://github.com/user-attachments/assets/b17588c9-2514-4869-a12e-fcd4e8c3cb4b)


---

## License

MIT License — Free to use, modify, and distribute with attribution.

---

Author

Adithya M. Varambally, Berlin, Germany

---

If you have questions or improvements, feel free to fork this and enhance it!
