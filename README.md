# 🎮 Rock Paper Scissors Game using Flask

A simple and interactive **Rock Paper Scissors** web game built using **Python Flask**, **HTML**, and **CSS**. The game allows the player to compete against the computer, keeps track of scores, and stores game history using Flask sessions.

---

## 📌 Features

- 🪨 Rock, 📄 Paper, ✂️ Scissors gameplay
- 💻 Random computer choice
- 🏆 Player, Computer, and Tie score tracking
- 📜 Game history (last 10 matches)
- 🔄 Reset score button
- 🎨 Modern responsive user interface
- 💾 Session-based score 
- ⚡ Smooth animations and hover effects

---

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Jinja2 Template Engine

---

## 📂 Project Structure

```
RockPaperScissors/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## 📥 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/RockPaperScissors.git
```

or download the ZIP file and extract it.

---

### Step 2: Navigate to the Project Folder

```bash
cd RockPaperScissors
```

---

### Step 3: Install Flask

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command:

```bash
python app.py
```

You will see something similar to:

```
* Running on http://127.0.0.1:5000/
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🎮 How to Play

1. Open the website.
2. Choose **Rock**, **Paper**, or **Scissors**.
3. The computer randomly selects its choice.
4. The result is displayed:
   - 🎉 You Win
   - 💻 Computer Wins
   - 🤝 It's a Tie
5. Scores are automatically updated.
6. The latest 10 matches are displayed in the Game History section.
7. Click **Reset Score** to clear all scores and history.

---

## 🏆 Game Rules

| Player Choice | Computer Choice | Result |
|---------------|-----------------|--------|
| Rock | Scissors | Player Wins |
| Rock | Paper | Computer Wins |
| Paper | Rock | Player Wins |
| Paper | Scissors | Computer Wins |
| Scissors | Paper | Player Wins |
| Scissors | Rock | Computer Wins |
| Same Choice | Same Choice | Tie |

---

## 📸 Screenshots

### Home Page

- Modern glassmorphism interface
- Three game buttons
- Scoreboard
- Game history

### Result Page

- Player choice
- Computer choice
- Animated result
- Updated scores

---

## 🔒 Session Management

The application uses Flask Sessions to store:

- Player Score
- Computer Score
- Tie Count
- Game History

Each user has their own independent scores during their browsing session.

---

## 🚀 Future Enhancements

- Add sound effects
- Dark mode
- Difficulty levels
- Multiplayer mode
- User login system
- Online leaderboard
- Timer mode
- Database integration
- AI-based computer strategy
- Tournament mode

---

## 📋 Requirements

Python Version:

```
Python 3.8 or above
```

Required Package:

```
Flask
```

Create a `requirements.txt` file containing:

```
Flask
```

---

## 👨‍💻 Author

**Name:** Manjunath A

Project: **Rock Paper Scissors Game using Flask**

---

## 📜 License

This project is created for educational and learning purposes.

Feel free to modify and improve it for your own projects.

---

## ⭐ Thank You

Thank you for checking out this project.

If you like this project, consider giving it a ⭐ on GitHub.
