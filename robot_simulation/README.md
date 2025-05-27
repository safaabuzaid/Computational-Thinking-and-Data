# Roomba Robot Cleaning Simulation

Simulates a group of Roomba-like robots cleaning a rectangular room using different movement strategies. The program compares how long it takes the robots to clean a specified percentage of the room, modeling real-world constraints like collisions with walls and random movement direction changes.

---

## Problem Description

This simulation models how multiple robots clean a room divided into 1x1 tiles. Each robot starts at a random position and moves in a random direction. Robots clean tiles they pass over and change direction when they hit walls. The simulation continues until a defined fraction of the room is clean.

---

## Skills Learned

- Object-Oriented Programming (OOP) in Python
- Class design and abstraction
- Simulation modeling and logic
- Working with floating-point positions and geometric constraints
- Random behavior and motion algorithms
- Performance comparison of algorithms (strategies)
- Data analysis and visualization

---

## Files

- Main_Code.py: Main simulation logic and robot classes
- ps2_visualize.py: Visualization tool
- README.md: This file

---

## How It Works

1. The room is represented as a grid of tiles.
2. Robots move around the room with a constant speed.
3. Robots clean tiles they enter and avoid moving through walls.
4. Two strategies are implemented:
   - StandardRobot: Picks a new direction only when it hits a wall.
   - RandomWalkRobot: Picks a new random direction after each move.
5. The program compares cleaning times for different numbers of robots and room sizes.
