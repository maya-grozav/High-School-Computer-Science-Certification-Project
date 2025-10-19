# The Little Game  
*A Pygame 2D game inspired by* **The Little Prince** *by Antoine de Saint-Exupéry*

## Overview
**The Little Game** is a 2D side-scrolling game built in *Python (Pygame)*. You play as *The Little Prince*, who just arrived on the *King's* planet, and must now bring him gold.


The app begins with a menu screen:
![Game menu](/ReadMe_images/game-menu.png)
and with any key press the game starts.
<p align="center">
  <img src="./ReadMe_images/little-prince-arriving.png" width="48%" alt="Little prince ariving">
  <img src="./ReadMe_images/birds-leaving.png" width="48%" alt="Birds leaving">
</p>

## Controls ##
The following keys control the Little Prince 
| Action | Key(s) | Image |
|--------|--------|-------|
| Jump | `W`, `SPACE`, or `↑` | ![Little prince jumping](/ReadMe_images/little-prince-jumping.gif) |
| Move Left | `A` or `←` | ![Little prince walking left](/ReadMe_images/walking-left.gif) |
| Move Right | `D` or `→` | ![Little prince walking right](/ReadMe_images/walking-right.gif) |
| Play dialogue | `ENTER` | ![King talking](/ReadMe_images/king-talking.gif) |
| Pick up gold | `P` | ![Little prince picking up gold](/ReadMe_images/pick-up.gif) |
| Give gold | `G` | ![Little prince giving King gold](/ReadMe_images/give.gif) |


## In-game instructions ##
The game provides instructions, either directly or through the King’s dialogue:
| Action | Instruction |
|--------|-------------|
| Game starts - Find the king | ![Move instruction](/ReadMe_images/move-instruction.png) |
| Interact with the King | ![King found](/ReadMe_images/king-found.png) |
| Collect gold | ![King talking](/ReadMe_images/king-talking.gif) |
| Pick up gold | ![Pick up instruction](/ReadMe_images/pick-up-instruction.png) |
| Give gold to the King | ![Give instruction](/ReadMe_images/give-instruction.png) |
| Collect more gold | ![A king needs more](/ReadMe_images/a-king-needs-more.png) |

## Game Mechanics  

- **Dialogue System:** Characters communicate through animated on-screen text
- **Collectibles:** Gold items appear randomly; you must collect a number of them to finish the game
- **Animations:** Birds, movement, and idle states are animated using timed Pygame events  
- **Environment:** Parallax scrolling and looping backgrounds enhance depth and continuity

## How to run the game ##
- You must have both Python and Pygame installed
- Run the game with `python ATESTAT.py` in a console; Run the command in the folder containing the project
