# Adventure Text Game (Python)

A simple **console-based adventure game** written in Python that demonstrates object-oriented programming concepts such as classes, inheritance, and basic game logic. Players choose a character class, select a difficulty level, and battle random enemies using skills until victory or defeat.

---

## 🎮 Game Overview

In this text-based adventure game, the player:

* Chooses a character class (**Knight** or **Bow Master**)
* Selects a difficulty level (**Easy, Medium, Hard**)
* Encounters random enemies
* Uses skills to defeat enemies in turn-based combat

The game continues until the player is defeated or chooses to stop fighting.

---

## ✨ Features

* **Object-Oriented Design**

  * Uses classes such as `Player`, `Knight`, `BowMaster`, `Enemy`, and `Skill`

* **Multiple Character Classes**

  * Knight: Melee-focused skills
  * Bow Master: Ranged and poison-based attacks

* **Turn-Based Combat System**

  * Player attacks first using selected skills
  * Enemy retaliates if still alive

* **Difficulty Levels**

  * Easy, Medium, and Hard affect enemy health

* **Random Enemy Encounters**

  * Enemies include Wild Boar, Goblin, Wyvern, and Golem

---

## 🛠 Technologies Used

* **Python 3**
* **Random Module** – For enemy selection
* **Object-Oriented Programming (OOP)**

---

## 📂 Project Structure

```
adventure-text-game/
│
├── game.py        # Main game file
├── README.md      # Documentation
```

---

## ⚙️ Requirements

* Python **3.x**

(No external libraries required)

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/adventure-text-game.git
cd adventure-text-game
```

2. Run the game:

```bash
python game.py
```

---

## 🧭 How to Play

1. Choose your character:

   * `[1] Knight`
   * `[2] Bow Master`

2. Enter your character name.

3. Select difficulty level:

   * `[1] Easy`
   * `[2] Medium`
   * `[3] Hard`

4. During combat:

   * Choose a skill by entering its number
   * Defeat the enemy before your health reaches zero

5. Decide whether to fight again after each battle.

---

## 🧪 Sample Gameplay

```
A wild Goblin appears with 60 health!

Choose a skill to use:
[1] Slash - A mighty sword attack!
[2] Shield Bash - Bashes the enemy with a shield to stun.
```

---

## 🎓 Learning Objectives

This project is ideal for practicing:

* Python OOP fundamentals
* Class inheritance and composition
* User input handling
* Simple game loops and logic

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Gereuel Brillantes**
BSIT Student – Guagua National Colleges, Inc.

---

## ⭐ Acknowledgment

Created as a learning project to explore Python programming and text-based game development.

If you enjoyed this project, feel free to ⭐ the repository.
