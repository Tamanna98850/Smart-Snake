# 🐍 Smart Snake

### Play. Analyze. Improve.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![Pandas](https://img.shields.io/badge/Analytics-Pandas-purple)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Processing-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

**Smart Snake** is an interactive Python-based Snake Game that combines traditional game development with **database management and data analytics**.

Unlike a basic Snake Game, Smart Snake records gameplay information, maintains player performance data, provides a leaderboard, generates analytics, and produces performance reports.

The project demonstrates how **Python, Pygame, OOP, SQLite, Pandas, NumPy and Matplotlib** can work together in one complete application.

---

## 🎯 Project Objective

The main objective of Smart Snake is to build an engaging game while demonstrating practical programming and data-analysis concepts.

The project aims to:

* 🎮 Provide an interactive Snake Game
* 🏆 Track player scores and rankings
* 🗄️ Store game history using SQLite
* 📊 Analyze player performance
* 📈 Generate performance reports
* 🔊 Provide sound effects
* 🧩 Use Object-Oriented Programming
* 📁 Maintain organized and modular project architecture

---

## ✨ Key Features

### 🎮 Gameplay

* Classic Snake gameplay
* Smooth snake movement
* Food collection
* Score tracking
* Snake length tracking
* Level progression
* Obstacles
* Power-ups
* Game Over system
* Restart functionality

### 🏆 Leaderboard

* Player ranking
* Best scores
* Player names
* Game performance tracking
* Achievement support

### 📊 Analytics Dashboard

Smart Snake stores gameplay data and uses it for analysis.

Analytics can include:

* Total games played
* Highest score
* Average score
* Player performance
* Snake length
* Level performance
* Food-related statistics
* Game history

### 🗄️ Database

SQLite is used to store game-related information.

Stored information can include:

* Player name
* Score
* Snake length
* Level
* Food information
* Game results
* Game history

### 🔊 Sound System

The project includes sound support for:

* Food collection
* Game start
* Game pause
* Game over
* Additional game events

---

## 🛠️ Technology Stack

| Technology     | Purpose                           |
| -------------- | --------------------------------- |
| **Python**     | Core programming language         |
| **Pygame**     | Game development and graphics     |
| **OOP**        | Modular and reusable architecture |
| **SQLite**     | Game-history database             |
| **Pandas**     | Data analysis                     |
| **NumPy**      | Numerical processing              |
| **Matplotlib** | Data visualization                |
| **CSV**        | Performance reports               |
| **Git**        | Version control                   |
| **GitHub**     | Project hosting                   |

---

## 📁 Project Structure

```text
Smart Snake/
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   │
│   └── analytics/
│       ├── achievements.py
│       ├── analytics.py
│       └── dashboard.py
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
├── screenshots/
│   ├── 01_main_menu.png
│   ├── 02_gameplay.png
│   ├── 03_leaderboard.png
│   └── 04_statistics.png
│
├── sounds/
│   ├── food.wav
│   ├── game_over.wav
│   ├── pause.wav
│   └── start.wav
│
├── main.py
├── main_backup.py
├── README.md
├── requirements.txt
├── game_history.db
├── analytics_game_history.csv
└── smart_snake_performance_report.csv
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Tamanna98850/Smart-Snake.git
```

### 2. Open the Project

```bash
cd Smart-Snake
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key       | Action              |
| --------- | ------------------- |
| **↑**     | Move Up             |
| **↓**     | Move Down           |
| **←**     | Move Left           |
| **→**     | Move Right          |
| **ENTER** | Select Menu         |
| **ESC**   | Return to Main Menu |
| **R**     | Restart Game        |
| **M**     | Toggle Sound        |
| **N**     | Toggle Music        |

> Controls may depend on the current implementation of the game modules.

---

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

---

## 🗄️ Database Architecture

Smart Snake uses **SQLite** to store gameplay information.

```text
Player
   │
   ▼
Gameplay
   │
   ├── Score
   ├── Level
   ├── Snake Length
   ├── Food Data
   └── Game Result
   │
   ▼
SQLite Database
   │
   ▼
Game History
```

The main database file is:

```text
game_history.db
```

---

## 📊 Data Analytics Flow

Gameplay data can be transformed into useful performance insights.

```text
Gameplay
    ↓
SQLite Database
    ↓
Game History
    ↓
Pandas DataFrame
    ↓
NumPy Processing
    ↓
Analytics
    ↓
Matplotlib Visualization
    ↓
Performance Reports
```

The project includes CSV-based analytics/report files:

```text
analytics_game_history.csv
smart_snake_performance_report.csv
```

---

## 🏆 Leaderboard System

The leaderboard uses stored gameplay information to display player performance.

It can help identify:

* Highest-scoring players
* Best game performances
* Player rankings
* Historical performance

This makes the game more engaging while also demonstrating database-based ranking logic.

---

## 🧩 Object-Oriented Design

The project uses Object-Oriented Programming to keep different game components organized.

Important classes/modules include:

```text
Player
Snake
Food
Obstacle
PowerUp
Game
Leaderboard
SoundManager
Dashboard
```

This modular design makes the project easier to:

* Understand
* Test
* Maintain
* Extend
* Debug

---

## 🧪 Testing

The major features of Smart Snake have been tested.

### Functional Testing

* [x] Main Menu
* [x] Player Name Entry
* [x] Snake Movement
* [x] Food Collection
* [x] Score System
* [x] Level System
* [x] Obstacles
* [x] Power-Ups
* [x] Game Over
* [x] Restart
* [x] Main Menu Return
* [x] Leaderboard
* [x] Statistics
* [x] SQLite Storage
* [x] CSV Reports
* [x] Sound System
* [x] Application Exit

---

## 📈 Performance Reports

Smart Snake can generate or maintain performance data in CSV format.

Example report files:

```text
analytics_game_history.csv
smart_snake_performance_report.csv
```

These files can be opened with:

* Microsoft Excel
* Google Sheets
* Pandas
* Other spreadsheet/data-analysis tools

---

## 🔮 Future Scope

Future versions of Smart Snake can include:

* 🌐 Online leaderboard
* 👥 Multiplayer mode
* 👤 Player profiles
* ☁️ Cloud database
* 🤖 AI-based difficulty adjustment
* 🎯 Multiple game modes
* 🏅 Advanced achievement system
* 📊 Interactive analytics dashboard
* 📱 Mobile version
* 🌍 Online player statistics

---

## 💡 What This Project Demonstrates

Smart Snake demonstrates practical knowledge of:

```text
Python
   ↓
Object-Oriented Programming
   ↓
Pygame
   ↓
SQLite
   ↓
Pandas + NumPy
   ↓
Data Analytics
   ↓
Matplotlib
   ↓
Git + GitHub
```

It is therefore both a **game-development project** and a **data-oriented Python project**.

---

## 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* OOP concepts
* Classes and objects
* Modular programming
* Game loops
* Event handling
* Collision detection
* Database operations
* Data storage
* Data analysis
* Data visualization
* CSV processing
* Git version control
* GitHub project management

---

## 👩‍💻 Developer

### Tamanna

**Project:** Smart Snake

**Category:** Python Game Development + Data Analytics

**Technologies:** Python, Pygame, SQLite, Pandas, NumPy, Matplotlib

---

## 📜 Project Motto

> **"Play. Analyze. Improve."**

---

## ⭐ Support the Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **educational and portfolio purposes**.
