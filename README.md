# 🐍 Smart Snake

### A Data-Driven Snake Game using Python, Pygame, SQLite and Pandas

> **Play. Analyze. Improve.**

Smart Snake is an enhanced Snake Game developed using **Python and Pygame** with database integration and data analytics.

The project combines traditional snake-game mechanics with **SQLite database storage, Pandas-based analytics, leaderboard management, statistics and power-ups**.

---

## 🎯 Project Objective

The main objective of Smart Snake is to create an interactive Snake Game while demonstrating practical implementation of:

* Python Programming
* Object-Oriented Programming
* Pygame Game Development
* SQLite Database
* Pandas Data Analysis
* Game Statistics
* Leaderboard System
* Modular Project Structure

---

## ✨ Features

### 🎮 Gameplay

* Classic Snake movement
* Arrow-key controls
* Food collection
* Dynamic score
* Snake growth
* Increasing game levels
* Obstacles
* Game Over system
* Restart functionality

### ⚡ Power-Ups

Smart Snake includes special power-ups such as:

* Speed Boost
* Double Score
* Shield

Power-ups make the gameplay more challenging and interactive.

### 🏆 Leaderboard

The game stores player performance and provides:

* Player name
* Best score
* Ranking
* Game history
* Achievement information

### 📊 Statistics & Analytics

The project uses **Pandas** to analyze game data.

Analytics can include:

* Total games
* Highest score
* Average score
* Player performance
* Snake length
* Game levels
* Food types
* Game history

### 💾 Database

Game records are stored using **SQLite**.

The database stores information such as:

* Player name
* Score
* Snake length
* Level
* Food type
* Game date

### 🔊 Sound System

The project supports:

* Food sound
* Power-up sound
* Game-over sound
* Background music

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Main programming language |
| Pygame     | Game development and UI   |
| SQLite     | Game data storage         |
| Pandas     | Data analysis             |
| NumPy      | Numerical/data processing |
| Matplotlib | Data visualization        |
| OOP        | Modular game architecture |

---

## 📁 Project Structure

```text
Smart Snake/
│
├── main.py
├── main_backup.py
├── README.md
├── game_history.db
├── smart_snake_performance_report.csv
│
├── game/
│   ├── __init__.py
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
│   ├── __init__.py
│   ├── db.py
│   │
│   └── analytics/
│       ├── __init__.py
│       ├── analytics.py
│       └── dashboard.py
│
└── sounds/
    ├── food.wav
    ├── game_over.wav
    └── pause.wav
```

---

## 🗄️ Database

Smart Snake uses an SQLite database named:

```text
game_history.db
```

Game performance is stored after a game ends.

Example information:

```text
Player Name
Score
Snake Length
Level
Food Type
Game Date
```

The stored data can then be analyzed using Pandas.

---

## 📊 Data Analytics

Pandas is used to convert game-history data into useful information.

Example analytics:

```text
Highest Score
Average Score
Total Games
Best Player
Average Snake Length
Level Performance
```

This makes Smart Snake more than a simple game because the project also demonstrates **data-driven analysis**.

---

## 🎮 Controls

| Key         | Action                  |
| ----------- | ----------------------- |
| ↑           | Move Up                 |
| ↓           | Move Down               |
| ←           | Move Left               |
| →           | Move Right              |
| R           | Restart after Game Over |
| ESC         | Return to Main Menu     |
| M           | Toggle Sound            |
| N           | Toggle Music            |
| ENTER       | Select Menu             |
| Mouse Click | Select Menu             |

---

## 🚀 How to Run

### 1. Open the project folder

Open the terminal inside:

```text
Smart Snake
```

### 2. Install dependencies

If the dependency file is available:

```powershell
pip install -r requirements.txt
```

If your file is currently named `requirment.txt`, rename it to:

```text
requirements.txt
```

Then run:

```powershell
pip install -r requirements.txt
```

### 3. Start the game

```powershell
python main.py
```

---

## 🕹️ Game Flow

```text
Main Menu
    ↓
Start Game
    ↓
Enter Player Name
    ↓
Play Snake
    ↓
Collect Food
    ↓
Increase Score
    ↓
Power-Ups / Obstacles
    ↓
Game Over
    ↓
Save Result to SQLite
    ↓
Leaderboard / Statistics
```

---

## 🏆 Project Highlights

Smart Snake demonstrates the integration of multiple programming concepts in one project:

```text
Python
   +
OOP
   +
Pygame
   +
SQLite
   +
Pandas
   +
NumPy
   +
Matplotlib
   ↓
Smart Snake
```

---

## 📈 Future Improvements

Possible future enhancements include:

* Online leaderboard
* Multiple game modes
* Difficulty selection
* Player profiles
* More power-ups
* Achievement badges
* Advanced analytics dashboard
* Performance graphs
* AI-based difficulty adjustment
* Cloud database
* Multiplayer mode

---

## 🧪 Testing

The following core features have been tested:

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
* SQLite Data Storage
* Game Exit

---

## 📌 Project Status

**Core Game Development: Complete ✅**

**Database Integration: Complete ✅**

**Leaderboard: Complete ✅**

**Analytics: Complete ✅**

**Final Documentation: In Progress 🚧**

---

## 👩‍💻 Developed By

**Tamanna**

### Smart Snake

> **Play. Analyze. Improve.**

---

## 📄 License

This project is created for **educational and learning purposes**.
