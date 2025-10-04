# Password Strength Detector Application

## About
The Password Strength Detector is a Python application that allows users to check the strength of their passwords and provides suggestions to improve weak passwords. The application also has a feature to generate strong passwords automatically.

This project is ideal for beginners and intermediate Python learners to practice using:
- String manipulation
- Conditional logic
- Loops
- Random password generation
- Text-to-speech functionality using `pyttsx3`

## Features
- Check password strength (Weak, Medium, Strong)
- Suggest improvements for weak passwords
- Generate a strong random password
- Text-to-speech guidance for better interactivity

## How it Works
1. User is prompted to enter a password.
2. The password is evaluated based on:
   - Length (minimum 8 characters)
   - Presence of lowercase letters
   - Presence of uppercase letters
   - Presence of numbers
   - Presence of special characters
3. The application provides feedback and suggestions for strengthening the password.
4. Users can type `generate` to get a suggested strong password.
5. Type `exit` or `quit` to close the application.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Abubakar-Asif/Git_and_GitHub_pratice.git
```
2. Navigate to the project folder:
```bash
cd Git_and_GitHub_pratice
```
3. Install required dependencies:
```bash
pip install pyttsx3
```

## Usage
Run the Python script:
```bash
python password_detector.py
```

### Commands inside the app:
- Enter any password to check its strength.
- Type `generate` to receive a suggested strong password.
- Type `exit` or `quit` to close the application.

## Example Output
```
Enter your password: password123
Your password strength is Medium.
Suggestions for a strong Password:
- Add Uppercase Letters.
- Add Special Characters.
```

## Technologies Used
- Python 3
- pyttsx3 for text-to-speech
- string and random modules

## Future Improvements
- Add GUI using Tkinter or PyQt5 for better user experience.
- Save password history securely.
- Add options for custom password length and complexity.

## License
This project is open-source and available under the MIT License.

