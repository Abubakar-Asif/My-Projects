# Jarvis Bot

A simple **Python-based virtual assistant** named **Jarvis** that can open and search popular websites using voice feedback. This project demonstrates automation with speech synthesis and web control.

## Features

- Voice feedback using `pyttsx3`
- Opens popular websites like Google, YouTube, Facebook, Instagram, and News portals
- Performs search queries directly on supported platforms
- Simple command-based interaction system
- Exit functionality with polite voice response

## How It Works

1. **Activation Phase:**
   - Jarvis initializes and waits for the user to type the activation name ("jarvis").

2. **Command Phase:**
   - Once activated, the user can give commands such as:
     - `open google`
     - `open youtube`
     - `open instagram`
     - `open facebook`
     - `open news`
     - `open google and search cats`
     - `open youtube and search music`
   - Jarvis responds through both text and voice using `pyttsx3`.

3. **Exit Phase:**
   - Use `exit` or `quit` to close the program.

## Requirements

Install the necessary dependencies before running the program:

```bash
pip install pyttsx3
```

*(The `webbrowser` module is part of Python’s standard library, so no need to install it.)*

## How to Run

1. Clone this repository or copy the source file.
2. Save it as `jarvis_bot.py`.
3. Run it using:

```bash
python jarvis_bot.py
```

4. Type commands in the terminal to interact with Jarvis.

## Example Commands

| Command                        | Action                                       |
|--------------------------------|----------------------------------------------|
| `open google`                  | Opens Google                                 |
| `open youtube and search ai`   | Searches “ai” on YouTube                     |
| `open instagram`               | Opens Instagram                              |
| `open facebook and search tech`| Searches “tech” on Facebook                  |
| `exit`                         | Exits the assistant                          |

## Future Improvements

- Add speech recognition for voice input
- Include more web services (e.g., Twitter, Reddit)
- Add GUI for easier interaction

## Author

**Abubakar Asif**  
Python Developer | Data Science Learner | Tech Enthusiast

---
*The End.*
