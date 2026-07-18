# PRODIGY_CS_02 – Image Encryption Tool

## Task Description

This task is part of the **Prodigy InfoTech Cyber Security Internship**.

The objective is to develop a Python program that implements a simple **Image Encryption Tool** using pixel manipulation techniques. The program encrypts and decrypts images by applying a mathematical operation to each pixel using a user-defined secret key. The same key is required to restore the original image.

---

## Features

- Encrypt images using pixel manipulation
- Decrypt encrypted images
- User-defined secret key
- Preserves image dimensions and quality
- Simple and easy-to-use command-line interface
- Supports common image formats (JPG, PNG)

---

## Technologies Used

- Python 3
- Pillow (PIL) Library
- Visual Studio Code (VS Code)

---

## Task Structure

```
PRODIGY_CS_02/
│── image_encryptor.py
│── input.jpg
│── encrypted.png
│── decrypted.png
│── README.md
```

---

## How to Run the Project in Visual Studio Code

### Step 1

Open **Visual Studio Code**.

### Step 2

Open the project folder containing **image_encryptor.py**.

### Step 3

Open the integrated terminal:

```
Terminal → New Terminal
```

### Step 4

Activate the project virtual environment, then install dependencies from `requirements.txt`:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Windows Command Prompt
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Step 5

Run the program using:

```bash
python image_encryptor.py
```

### Step 6

Choose one of the following options:

- Encrypt
- Decrypt

### Step 7

Enter the secret key when prompted.

The program will:

- Encrypt `input.jpg` and generate `encrypted.png`
- Decrypt `encrypted.png` and generate `decrypted.png`

---

## Sample Output

```
===== IMAGE ENCRYPTION TOOL =====

Enter Encrypt(E) or Decrypt(D): E
Enter Secret Key: 4

Image Encrypted Successfully!
Saved as: encrypted.png
```

```
===== IMAGE ENCRYPTION TOOL =====

Enter Encrypt(E) or Decrypt(D): D
Enter Secret Key: 4

Image Decrypted Successfully!
Saved as: decrypted.png
```

---

## Learning Outcomes

- Understanding basic image encryption techniques
- Learning pixel manipulation using Python
- Working with the Pillow (PIL) library
- Performing mathematical operations on RGB pixel values
- Building a simple image processing application
- Understanding the basics of encryption and decryption

---

## Author

**Muthoju Vishista**

Cyber Security Intern – Prodigy InfoTech
