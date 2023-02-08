# Mario-Bros by Jędrzej "Yendrula" Dudzicz

An adaptation of the Mario Bros game for a project from the Human Computer Communication class.

---

## Table of content
* [General info](#General-info)
* [Installation](#Installation)
* [Usage](#Usage)
* [Technologies](#technologies)

## General info

The game contains several views:

### 1. Menu
<img src="https://raw.githubusercontent.com/jedrzejd/Mario-Bros/master/imgs/menu.png" height="400">

The player can select the following buttons with the keys (1, 2, 3) or by moving the mouse.

a) Play
  - Launches the level selection view
  
b) Credits
  - The user receives information provided by the game developer
  
c) Quit
  - Ends the application

### 2. Level selection view
<img src="https://raw.githubusercontent.com/jedrzejd/Mario-Bros/master/imgs/levels.png" height="400">
The user moves between the available levels using the left and right arrows.

A particular level is selected by clicking the spacebar.

Only the first level is available at the beginning of the game, the others are locked and hidden from the player.

Animations are only played on unlocked levels.
There are 3 levels in the game. Completing the last one completes the game.

View after unlocking 3 levels.

<img src="https://raw.githubusercontent.com/jedrzejd/Mario-Bros/master/imgs/all_levels.png" height="400">

### 3. Level view
<img src="https://raw.githubusercontent.com/jedrzejd/Mario-Bros/master/imgs/game.png" height="400">

In the top left corner we see information about the player's status: 
- Life bar
- Player's score
- Number of coin points scored (silver coins count for 1, gold coins count for 5)
- Number of defeated opponents

The player moves around the board using the arrows (Left, Right and Space bar).

The goal of the board is to score as many points as possible and to find the portal to the next level (star)

## Installation on Linux/Macos

* Download and install `Python 3.10`

    ```
    https://www.python.org/downloads/release/python-3100/
    ```
* Download this repository and unzip


* Create python virtual environment

```bash
cd Mario-Bros-master
python3 -m venv venv
```

* Active python virtual environment

```bash
. venv/bin/activate
```

* Install require packages

```bash
pip install -r requirements.txt
```

### Usage

```bash
python3 main.py
```


## Technologies
- Python 3.10
- pygame
