# Central Library App

A Python-based **Central Library Management System** that allows users to list, borrow, return, and search for books using a simple text-based interface — enhanced with **voice interaction** using `pyttsx3`.

---

## Features

**List Books** – View all available books in the library  
**Borrow Books** – Borrow a book and automatically update the record  
**Return Books** – Return a book (handles duplicates automatically)  
**Search Books** – Search whether a specific book is available  
**Voice Support** – Each action is read aloud using the `pyttsx3` library for a better user experience  
**File Management** – Uses a `.txt` file to maintain library data persistently  

---

## How It Works

The app stores book records inside a file named `Central_Library_File.txt`.  
Each time you borrow or return a book, the system updates this file automatically — no database needed!

---

## Technologies Used

- **Python 3.x**
- **pyttsx3** (for text-to-speech)
- **File I/O** (for data persistence)

---

## How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/YourUsername/Central-Library-App.git
   ```
2. **Navigate to the project folder**
   ```bash
   cd Central-Library-App
   ```
3. **Install required library**
   ```bash
   pip install pyttsx3
   ```
4. **Run the program**
   ```bash
   python main.py
   ```

---

## Example Usage

```text
********** Welcome To The Central Library **********
Please Choose An Option :
1. List all available books.
2. Borrow a book.
3. Return a book.
4. Exit the program.
5. Search a book.
```

🎙️ The app will also speak each prompt and message using your system’s voice engine.

---

## File Structure

```
Central-Library-App/
│
├── main.py                  # Main program file
├── Central_Library_File.txt # File where all books are stored
└── README.md                # Project documentation
```

---

## Future Improvements

- Add a GUI using `tkinter`
- Track borrowers and return dates
- Add authentication for library users

---

## Author

**Abubakar Asif**  
Python Developer | Data Science Enthusiast | Project Builder  
[GitHub Profile](https://github.com/Abubakar-Asif)

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

*If you like this project, please give it a star on GitHub !*