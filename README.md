# Python Menu-Driven Tank Simulator

A command-line tank simulation project written in Python to demonstrate basic process control, operator interaction, and automation-style logic using a menu-driven interface.

---

## Overview

This project simulates a simple tank system that allows a user to interact with the process through a text-based menu. It was built to practice Python programming while also applying real-world automation and controls concepts such as tank level management, fill and drain operations, state changes, and basic alarm handling.

This project is a good example of how software logic can be used to represent industrial-style process behavior in a simple and understandable way.

---

## Features

- Menu-driven command-line interface
- Tank fill and drain simulation
- Tank level monitoring
- Basic control logic
- Operator-style interaction
- Alarm and limit concepts
- Beginner-friendly structure
- Great project for learning Python and automation fundamentals

---

## Why I Built This

I built this project to strengthen my Python skills while working on something related to controls and automation. Tank systems are common in industrial environments, so this simulator gave me a way to practice programming with a process that connects to real-world control concepts.

It also helped me think through how an operator might interact with a system, how process variables change over time, and how simple protections like high and low limits can be implemented in code.

---

## Technologies Used

- **Python 3**
- Command-Line Interface (CLI)

---

## How It Works

When the program starts, it displays a menu of available actions. The user selects an option, and the simulator updates the tank system based on that command.

Depending on the version of the simulator, actions may include:

- Viewing current tank level
- Filling the tank
- Draining the tank
- Starting or stopping a pump
- Resetting the tank
- Displaying alarms or warnings
- Exiting the simulator

The system can be designed to prevent invalid conditions such as:

- Overfilling the tank
- Draining below zero
- Running actions outside safe operating limits

---

## Example Menu

```text
1. View Tank Level
2. Fill Tank
3. Drain Tank
4. Start Pump
5. Stop Pump
6. Reset Tank
7. Exit
