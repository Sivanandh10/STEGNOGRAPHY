# Image Steganography Tool 📸🔒

## Brief Description 🌟
This project is a **Python-based Image Steganography Tool** that allows you to **hide secret messages** within images and **retrieve them** later. It provides a **user-friendly interface** built with **Tkinter**, making it easy to encrypt and decrypt messages using images. The tool ensures that your messages are securely hidden within the image pixels, and only those with the correct password can decrypt the hidden message.

---

## Detailed Description 🛠️

### Features ✨
- **Encrypt Messages**: Hide your secret message within an image.
- **Decrypt Messages**: Retrieve the hidden message from the encrypted image.
- **Password Protection**: Secure your hidden message with a password.
- **User-Friendly Interface**: Easy-to-use GUI for seamless interaction.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

### How It Works 🧠
1. **Encryption**:
   - The tool takes an input image, a secret message, and a password.
   - It stores the message length in the first pixel of the image.
   - The message is then encrypted and hidden in the subsequent pixels of the image.
   - The encrypted image is saved as `encryptedImage.png`.

2. **Decryption**:
   - The tool reads the encrypted image and retrieves the message length from the first pixel.
   - Using the password, it decrypts the message hidden in the image pixels.
   - The decrypted message is displayed to the user.

### Code Structure 📂
- **Tkinter GUI**: The interface is built using Tkinter, providing a clean and intuitive design.
- **OpenCV**: Used for image processing and manipulation.
- **File Dialog**: Allows users to browse and select images from their system.
- **Gradient Background**: The UI features a multicolor gradient background for a modern look.

### Requirements 📋
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Tkinter (usually comes pre-installed with Python)

### Output 🚀
1. **Encryption**:
   ![image](https://github.com/user-attachments/assets/e7912a7f-fb6c-4415-84b8-b28f044d14c9)
2. **Decryption**:
   ![image](https://github.com/user-attachments/assets/22a84c54-c4c5-4113-8056-aa8c516b038b)

3. **Sample Outputs**:
   ![image](https://github.com/user-attachments/assets/91294e07-8670-4b1b-b2d3-97de313926a6)
   ![image](https://github.com/user-attachments/assets/3a3cd550-b555-43e4-ae9c-4c30c8d0995b)
   ![image](https://github.com/user-attachments/assets/19cd65ce-4381-4c81-8982-a26c641e5183)

### **@sivanandh cc**


