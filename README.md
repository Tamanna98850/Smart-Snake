# 🐍 Smart Snake

### Play. Analyze. Improve.

**Smart Snake** is an interactive Snake Game developed using **Python and Pygame**, enhanced with **SQLite database storage, leaderboard, player statistics and data analytics**.

---

## 🎯 Project Objective

The objective of Smart Snake is to combine game development with practical data-management and data-analysis concepts.

The project demonstrates:

* Python programming
* Object-Oriented Programming
* Pygame
* SQLite
* Pandas
* NumPy
* Matplotlib
* Data analysis
* Player performance tracking

---

## ✨ Features

### 🎮 Gameplay

* Snake movement
* Food collection
* Score system
* Increasing levels
* Obstacles
* Power-ups
* Game Over system
* Restart option

### 🏆 Leaderboard

* Player ranking
* Best score
* Player performance
* Achievements
* Game history

### 📊 Analytics

* Total games
* Highest score
* Average score
* Snake length
* Player performance
* Level performance
* Food-type analysis
* Performance reports

### 🔊 Sound System

* Food sound
* Game-over sound
* Start sound
* Pause sound
* Background/game sound support

---

## 🛠️ Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core programming     |
| Pygame     | Game development     |
| SQLite     | Database             |
| Pandas     | Data analysis        |
| NumPy      | Numerical processing |
| Matplotlib | Visualization        |
| OOP        | Modular architecture |

---

## 📁 Project Structure

```text
Smart Snake/
│
├── main.py
├── main_backup.py
├── README.md
├── requirements.txt
├── game_history.db
├── analytics_game_history.csv
├── smart_snake_performance_report.csv
│
├── game/
│   ├── game.py
│   ├── snake.py
│   ├── player.py
│   ├── food.py
│   ├── obstacle.py
│   ├── powerup.py
│   ├── leaderboard.py
│   ├── menu.py
│   └── sound_manager.py
│
├── database/
│   ├── db.py
│   └── analytics/
│       ├── achievements.py
│       ├── analytics.py
│       └── dashboard.py
│
└── sounds/
    ├── food.wav
    ├── game_over.wav
    ├── pause.wav
    └── start.wav
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Tamanna98850/Smart-Snake.git
```

Move into the project folder:

```bash
cd Smart-Snake
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

---

## 🎮 Controls

| Key   | Action              |
| ----- | ------------------- |
| ↑     | Move Up             |
| ↓     | Move Down           |
| ←     | Move Left           |
| →     | Move Right          |
| ENTER | Select Menu         |
| ESC   | Return to Main Menu |
| R     | Restart             |
| M     | Toggle Sound        |
| N     | Toggle Music        |

---

## 🗄️ Database

Smart Snake uses SQLite for storing game history.

### Database

```text
game_history.db
```

### Stored Information

* Player name
* Score
* Snake length
* Level
* Food type
* Game date

---

## 📊 Data Analytics

Game-history data can be processed using Pandas.

```text
SQLite Database
       ↓
Game History
       ↓
Pandas DataFrame
       ↓
Data Processing
       ↓
Statistics
       ↓
Reports / Charts
```

---

## 🏆 Leaderboard

The leaderboard uses stored game data to calculate player rankings and best scores.

Players can view their performance and achievements after playing.

---

## 🧪 Testing

The main project features have been tested, including:

* Main Menu
* Player Name Entry
* Snake Movement
* Food Collection
* Score System
* Power-Ups
* Obstacles
* Game Over
* Restart
* Main Menu Return
* Leaderboard
* Statistics
* SQLite Storage
* Application Exit

---

## 🚀 Future Scope

Future versions can include:

* Multiplayer mode
* Online leaderboard
* Player profiles
* More game modes
* Advanced analytics dashboard
* AI-based difficulty
* Cloud database
* Additional achievements

---

## 📸 Screenshots
## 📸 Screenshots

### 🏠 Main Menu

![Smart Snake Main Menu](screenshots/01_main_menu.png)

---

### 🎮 Gameplay

![Smart Snake Gameplay](screenshots/02_gameplay.png)

---

### 🏆 Leaderboard

![Smart Snake Leaderboard](screenshots/03_leaderboard.png)

---

### 📊 Statistics

![Smart Snake Statistics](screenshots/04_statistics.png)


Screenshots of the game can be added here:

```text
Main Menu
Gameplay
Leaderboard
Statistics
Game Over
```

---

## 👩‍💻 Developer

**Developed By: Tamanna**

### 🐍 Smart Snake

> **Play. Analyze. Improve.**

---

## ⭐ Project

If you find this project useful, you can give the repository a star ⭐
