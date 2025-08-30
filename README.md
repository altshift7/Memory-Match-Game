 Memory Match Game with Levels & Leaderboard

A desktop-based image matching game built with Python, Tkinter, Pillow, Pygame, and SQLite.
The game challenges players to match pairs of cards on grids that increase in size (4x4 → 8x8).
It features timers, click counters, levels, power-ups, audio feedback, dark mode, and a leaderboard that stores player progress across sessions.

 Features

 Level progression: 4x4 → 8x8 grids for increasing difficulty.

 Timer & click counter: Track performance in each level.

 Leaderboard with SQLite: Store and display scores across sessions.

 User accounts: Enter your name and save results persistently.

 Dark mode toggle: Switch between light and dark themes.

 Audio feedback: Added sounds for clicks, matches, and level completion.

 Power-ups: Boost gameplay with special abilities.

 Tech Stack

Python → Core logic and event handling.

Tkinter → GUI for the game board and menus.

Pillow (PIL) → Image handling (resizing, scaling).

Pygame → Audio playback for game sounds.

SQLite → Local database for storing scores and leaderboard.

 Project Structure
MemoryMatchGame/
│── game.py          # Main game logic (levels, grid, clicks, timer, dark mode)
│── database.py      # Handles SQLite database for scores & leaderboard
│── sound_test.py    # Manages sound effects using pygame
│── assets/          # Images and sounds used in the game
│── scores.db        # SQLite database (auto-created if missing)
│── requirements.txt # Project dependencies

 Installation & Setup

Clone the repository

git clone https://github.com/your-username/MemoryMatchGame.git
cd MemoryMatchGame


Create and activate a virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the game

python game.py

 Requirements

Contents of requirements.txt:

tkinter
pillow
pygame


(SQLite is built-in with Python, no extra install required.)

 Screenshots

<img width="502" height="410" alt="image" src="https://github.com/user-attachments/assets/a3b6cd54-0036-4f4d-acff-93d428cb728f" />

<img width="497" height="413" alt="image" src="https://github.com/user-attachments/assets/f67e4dfe-e889-4caf-83a6-79b1b550e02e" />

<img width="472" height="525" alt="image" src="https://github.com/user-attachments/assets/bf38b95a-c141-4f09-9fda-c746a84f441b" />

<img width="476" height="521" alt="image" src="https://github.com/user-attachments/assets/dbde04c4-4ec6-4d96-bafd-1fe39c5a9bcc" />

<img width="315" height="347" alt="image" src="https://github.com/user-attachments/assets/1f9d34b1-31be-4cb8-b2de-c651a0800fbb" />

<img width="664" height="738" alt="image" src="https://github.com/user-attachments/assets/598f651b-9b52-4d54-8de5-2c5ee9f106c7" />

<img width="867" height="951" alt="image" src="https://github.com/user-attachments/assets/be7744fa-56c3-465c-a988-d1fd84300c76" />

<img width="879" height="947" alt="image" src="https://github.com/user-attachments/assets/28bd9a4d-f7e0-4d3a-9634-0c6dcde9bb4b" />






 Learnings & Challenges

Learned how to design event-driven GUIs with Tkinter.

Integrated Pillow for image manipulation and Pygame for sound effects.

Gained experience with SQLite databases for storing persistent user data.

Faced challenges with virtual environments, package installation, and debugging imports, which improved understanding of Python environments.
