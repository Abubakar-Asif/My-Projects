
# Number Guessing Game

A simple and interactive Python console game where the player tries to guess a randomly generated number between 1 and 100.  
The program gives hints after each guess and tracks the best (lowest) number of attempts as a high score.

---

## Features

- Generates a random number between 1 and 100  
- Provides feedback for each guess (“Too High” / “Too Low”)  
- Validates user input and handles invalid entries gracefully  
- Saves and updates the best score automatically  
- Fully console-based and beginner-friendly

---

## Technologies Used

- **Language:** Python 3  
- **Modules:** `random` (built-in)

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```
2. Navigate into the project folder:
   ```bash
   cd number-guessing-game
   ```
3. Run the Python file:
   ```bash
   python number_gussing_game.py
   ```

---

## High Score System

The program stores the fewest number of guesses (the high score) in a local file named:
```
number_guss_data.txt
```
When the player beats the existing record, the new score is saved automatically.

---

## Example Gameplay

```
Enter your guss : 45
Too Low.
Enter your guss : 78
Too High.
Enter your guss : 62
You gussed the right number.
Congrulation , you break the high score.
Previous high score 10.
Your high score 3.
```

---

## Future Improvements

- Add difficulty levels (Easy, Medium, Hard)  
- Create a GUI version using Tkinter  
- Display total attempts and session history  

---

## Author

**Abubakar Asif**  
Beginner Python Developer passionate about creating small games and exploring data science.

---

## License

This project is open-source and available for personal or educational use.
