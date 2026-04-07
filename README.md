# 🎮 Python Arcade Project

Welcome to the **Python Arcade**!  

This is a simple Python project where you can play:

- **Rock Paper Scissors**  
- **Guess My Number**  

You can play each game **individually** or use the **Arcade mode** to switch between games without quitting Python.

---

## ⚡ Features

### Arcade mode:
- Lets you choose a game from a menu  
- Press `"Q"` to return to the arcade menu instead of quitting  

### Standalone mode:
- Run each game individually  
- Press `"Q"` to quit the game completely  

### Other Features:
- Tracks wins, game count, and winning percentage  
- Handles invalid inputs with friendly prompts  

---

## 🛠 How it was made

- **Language:** Python  
- **Modules:**  
  - `random` → for computer moves  
  - `sys` → to exit games in standalone mode  
     

- **Files:**  
  - `arcade.py` → Main menu and Arcade mode  
  - `rps.py` → Rock Paper Scissors logic  
  - `guess_number.py` → Guess My Number logic  

- **Logic:**  
  - Each game keeps track of stats (wins, games played)  
  - Arcade handles quitting differently from standalone mode  
  - Loops used to repeat games instead of recursion to prevent repeated messages  

---

## 📝 Challenges I Faced

- **Handling quit (`Q`) differently:**  
  - Arcade mode → return to menu  
  - Standalone mode → exit Python using `sys.exit()`  

- **Repeated messages in RPS:**  
  - Recursion initially caused `"Welcome back to the Arcade!"` to print multiple times  
  - Fixed using loops instead of recursion  

- **Statistics calculation:**  
  - Tracking wins, game count, and winning percentage  
  - Ensuring division by zero is avoided when no games have been played  

- **Input validation:**  
  - Only accepts `1`, `2`, `3`, `Y`, `Q`  
  - Friendly messages guide the user to valid input  

- **Tiny syntax bug:**  
  - A missing `()` or misplaced `return` could stop the whole game from working  
  - It was amazing to see that such a small thing could break everything, but also rewarding when I fixed it!  

---

## 💖 What I Enjoyed Most

- Seeing all the pieces come together in the arcade menu  
- Playing the games I created myself  
- Learning to **track stats** and use **loops, functions, and enums** in Python  
- Understanding how a small syntax mistake can affect the whole program  

---

## 🎯 Future Improvements

- Add more games like **Tic-Tac-Toe** or **Dice Roller**  
- Add a **leaderboard** to track multiple players  
- Save player stats to a file to keep progress between sessions  
- Add **ASCII art or animations** for a more fun arcade experience  

---

## 🎓 About Me

I’m learning Python and this project helped me practice:

- Functions and recursion  
- Loops and input validation  
- Modules and importing files  
- Using `sys.exit()` for quitting  
- Handling program flow differently depending on standalone or arcade mode  

It was exciting to see the games come together and work smoothly after fixing that one tiny `()` issue that had stopped everything before!  

---

## 🎉 Enjoy the Arcade!
Run python arcade.py -n "YourName" and have fun! 👋
