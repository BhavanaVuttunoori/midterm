
# MIDTERM: Advanced Python Calculator

## Project Overview

This project is a **Python-based advanced calculator** that supports:

* Interactive **REPL command-line interface**
* **Arithmetic operations**: addition, subtraction, multiplication, division, square, modulus, power, root, integer division, percent, absolute difference
* **Calculation history management** using Pandas (view, clear, save, load)
* **Dynamic plugin system** for adding new functionalities
* **Comprehensive logging** and **environment variable configuration**
* Modular, maintainable, and extensible code using **design patterns** (Factory, Memento, Observer)
* Undo/Redo functionality
* Error handling and input validation

The architecture is designed for easy future enhancements while maintaining clean, robust code.

---

## Prerequisites

* **Python 3.10+** (64-bit)
* **pip**
* **Git**
* Optional: Visual C++ Redistributable for Windows

---

## Windows-Specific Setup

### Enable Long Path Support

Avoid “filename too long” errors:

1. Win → Settings → System → About → Advanced System Settings
2. Environment Variables → New System Variable:

   * Name: `LONG_PATH_TOOL`
   * Value: `1`
3. Reboot your PC.

### Install Git for Windows

1. [Download Git](https://git-scm.com/download/win)
2. Check recommended options during installation.
3. Verify installation:

```cmd
git --version
```

4. Configure Git:

```cmd
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global core.longpaths true
```

---

## Ubuntu/Linux Setup

1. **Install Python 3.10+ and pip**:

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip git -y
python3 --version
pip3 --version
```

2. **Create project folder**:

```bash
mkdir ~/advanced_calculator
cd ~/advanced_calculator
```

3. **Create & activate a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Upgrade pip and install dependencies**:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install python-dotenv pandas colorama pytest pytest-cov
```

---

## Project Implementation Steps

### Step 1: Implement Arithmetic Operations (Factory Pattern)

Operations implemented:

* Addition, Subtraction, Multiplication, Division
* Power, Root, Modulus, Integer Division
* Percent, Absolute Difference

Use **operation classes** and a **Factory** to instantiate them dynamically.

### Step 2: Undo/Redo (Memento Pattern)

* Save each calculator state in a `CalculatorMemento`
* Allow undoing or redoing multiple steps

### Step 3: Observer Pattern

* `LoggingObserver` logs calculations
* `AutoSaveObserver` saves history automatically
* Calculator notifies observers after each calculation

### Step 4: Configuration Management (.env)

Example `.env` file:

```
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=50
CALCULATOR_AUTO_SAVE=True
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

Load using `python-dotenv`.

### Step 5: Error Handling & Validation

* Custom exceptions for operations and input validation
* Ensure numeric inputs and valid operations

### Step 6: Logging

* Log all calculations and errors to a configurable file
* Use different log levels (`DEBUG`, `INFO`, `ERROR`)

### Step 7: REPL Commands

Supported commands:

* Arithmetic: `add`, `subtract`, `multiply`, `divide`, `power`, `root`, `modulus`, `int_divide`, `percent`, `abs_diff`
* History: `history_show`, `history_clear`, `history_save`, `history_load`
* Utility: `last_op`, `menu`, `exit`

### Step 8: Serialization & CSV Persistence

* Save history to CSV
* Load history from CSV
* Use Pandas for efficient history management

### Step 9: Unit Testing

```bash
pytest -v
pytest --cov=app --cov-report=html --cov-fail-under=90
```

* Test operations, undo/redo, logging, error handling, and edge cases

### Step 10: Optional Enhancements

* Dynamic help menu
* Color-coded CLI using Colorama
* Extensible plugin system

---

## Running the Calculator

With virtual environment activated:

```bash
python main.py
```

---

## Environment Variables (Optional)

Set environment variables for logging and history:

```text
LOG_LEVEL=DEBUG
LOG_OUTPUT=./logs/app.log
HISTORY_PATH=./calculator_history
ENVIRONMENT=DEVELOPMENT
```

---

## Useful Commands

| Task                    | Windows Command                 | Linux/Ubuntu Command            |
| ----------------------- | ------------------------------- | ------------------------------- |
| Activate venv           | `venv\Scripts\activate.bat`     | `source venv/bin/activate`      |
| Deactivate venv         | `deactivate`                    | `deactivate`                    |
| Upgrade pip             | `python -m pip install -U pip`  | `python3 -m pip install -U pip` |
| List installed packages | `pip list`                      | `pip list`                      |
| Export environment      | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Clear terminal          | `cls`                           | `clear`                         |
| Kill Python process     | `Ctrl + C`                      | `Ctrl + C`                      |
| Open file               | `notepad filename.py`           | `nano filename.py`              |

-