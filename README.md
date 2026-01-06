# 🚨 Educational DoS Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](#)
[![Build Status](https://img.shields.io/badge/build-passing-lightgrey.svg)](#)

A **Python-based educational GUI application** designed to demonstrate the **mechanisms, detection, and impact of Denial-of-Service (DoS) attacks** in a **controlled and authorized environment**.  
This project is intended strictly for **learning, research, and defensive security education**.

---

## ⚠️ Legal & Ethical Disclaimer

This software is developed **solely for educational and research purposes**.  
It must **only** be used on systems and networks you **own or have explicit permission to test**.

Any unauthorized or malicious use of this software is **illegal and unethical**.  
The developer assumes **no responsibility** for misuse.

---

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Architecture](#-technical-architecture)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Credits & Contact](#-credits--contact)
- [License](#-license)

---

## ✨ Features

- 🧪 **Multiple DoS Simulation Types**  
  Demonstrates common denial-of-service techniques for learning purposes.

- 📊 **Real-Time Visualization**  
  Live graphs showing traffic behavior, request rates, and bandwidth usage.

- 🖥️ **System Monitoring**  
  Displays real-time CPU and RAM usage using cross-platform tools.

- 🎨 **Modern GUI Interface**  
  Clean, themeable interface with Light and Dark modes.

- 📈 **Advanced Statistics**  
  Tracks packet counts, average rates, and peak values.

- ⚙️ **Fully Configurable Parameters**  
  Adjustable inputs for controlled experimentation and analysis.

---

## 🚀 Installation

### Prerequisites

- Python **3.6 or higher**
- `pip` (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mphosiphosenkosi-collab/educational-dos-simulator.git
   cd educational-dos-simulator

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Running the appliaction**
    ```bash
    python dos_simulator.py

## 🧰 Usage

⚠️ Use only on local or authorized test environments (e.g., 127.0.0.1 or a lab VM).

## Example 1: Learning Traffic Behavior

- Launch the application

- Select a simulation type

- Observe how traffic patterns change in real-time graphs

- Analyze packet rates and bandwidth usage

## Example 2: System Resource Monitoring

- Run a simulation at low intensity

- Watch CPU and RAM usage metrics update live

- Understand how traffic volume impacts system resources

## Example 3: Parameter Experimentation

- Adjust delay, packet size, or thread count

- Compare results across different configurations

- Use statistics to evaluate performance trends

## 🏗️ Technical Architecture

Language: Python

- GUI Framework: Tkinter (custom themed)

- Concurrency: Python threading

- Networking: Socket-based simulation logic

- Visualization: Matplotlib

- Data Analysis: Pandas

- System Metrics: Psutil

The application uses a multi-threaded design to ensure the GUI remains responsive while simulations run independently.

## 📁 Project Structure

    educational-dos-simulator/
    ├── dos_simulator.py      # Main application entry point
    ├── requirements.txt      # Python dependencies
    ├── README.md             # Documentation
    ├── LICENSE               # MIT License
    └── assets/
        └── screenshot.png    # Optional screenshots


## 👨‍💻 Credits & Contact

Johannes Siphosenkosi Sibiya

GitHub: https://github.com/mphosiphosenkosi-collab

Developed as a capstone project for learning network security concepts and Python application design.


## 📜 License
    This project is licensed under the MIT License.

