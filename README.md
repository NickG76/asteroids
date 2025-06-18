
# Asteroid Game

This is my astseroid game I created with boot.dev

## Prerequisites
You will need to install python 3 and pip, use these commands in your linux or WSL terminal (please see documentation on how to install with mac or windows native terminal)




```bash
sudo apt install python3
sudo apt install python3-pip
```
## Cloning the repository
Use this to clone the repository
```bash
git clone https://github.com/NickG76/asteroids.git
cd ./asteroids
```
## How to setup 
Use this to install the environment and install pygame
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## How to setup the environment and exit the environment
Setup
*** Please use location/to/asteroids to locate your directory ***
```bash
cd location/to/asteroids/
source venv/bin/activate
```
Exit
```bash
deactivate 
```
## How to Run
To run the game, use
```bash
python3 main.py
```
## How to play
Use W A S D to move and SPACE to shoot, you hit an asteroid, it's game over!

When the game finishes, look at our terminal to view your score.
