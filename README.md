
# MIDTERM: Advanced Python Calculator (Windows Setup)

## Project Overview

This project is a **Python-based advanced calculator** that supports:

* Interactive **REPL command-line interface**
* **Arithmetic operations**: addition, subtraction, multiplication, division, **square**, **modulus**, **power**
* **Calculation history management** using Pandas (view, clear, save, load)
* **Dynamic plugin system** for adding new functionalities
* **Comprehensive logging** and **environment variable configuration**
* Modular, maintainable, and extensible code using **design patterns**

The architecture is designed for easy future enhancements while maintaining clean, robust code.

---

## Prerequisites

* **Python 3.10+** (64-bit) – Ensure “Add Python to PATH” is checked during install.
* **pip** – Comes with Python.
* **Git for Windows** – Needed for version control.
* Optional: **Visual C++ Redistributable** for some Python packages:
  [VC Redist 64-bit](https://aka.ms/vs/17/release/vc_redist.x64.exe)

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
2. During installation, check:

   * “Git from the command line and also from 3rd-party software”
   * “Use Windows’ default console window”
   * “Enable experimental support for pseudo consoles” (optional)
3. Verify installation:

```bash
git --version
```

4. Configure Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global core.longpaths true
```

5. Generate SSH key for GitHub (optional, HTTPS works too):

```bash
ssh-keygen -t ed25519 -C "you@example.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub | clip
```

Add the public key in GitHub → Settings → SSH and GPG keys → “New SSH key”.

---

## Project Setup

1. **Create project folder** (short path recommended, e.g., `C:\dev`):

```cmd
mkdir C:\dev
cd C:\dev
```

2. **Create & activate a virtual environment**:

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

3. **Upgrade pip and install dependencies**:

```cmd
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## Running the Calculator

With the virtual environment activated:

```cmd
python main.py
```

This launches the **REPL interface**, supporting commands like:

* `add <num1> <num2>`
* `subtract <num1> <num2>`
* `multiply <num1> <num2>`
* `divide <num1> <num2>`
* `square <num>`
* `modulus <num1> <num2>`
* `power <num1> <num2>`
* `history_show` | `history_clear` | `history_save` | `history_load`
* `last_op` | `menu` | `exit`

---

## Enhanced Features

* **New arithmetic operations**: `square`, `modulus`, `power`
* **Dynamic Plugin System**: Add new functionality without changing core code
* **Calculation History Management**: view, save, load, and clear history with Pandas
* **Robust Logging**: configurable log levels via environment variables
* **Design Patterns**: Facade, Command, Factory Method for modularity and scalability
* **Error Handling**: EAFP & LBYL approaches for safe operation
* **Interactive REPL**: Real-time feedback for commands

---

## Environment Variables (Optional)

Set environment variables in Windows (Control Panel → System → Environment Variables) for logging and history:

```text
LOG_LEVEL=DEBUG
LOG_OUTPUT=.\logs\app.log
HISTORY_PATH=.\calculator_history
ENVIRONMENT=DEVELOPMENT
```

---

## Testing & Coverage

Run unit tests:

```cmd
pytest -v
```

Check code coverage and linting:

```cmd
pytest --pylint --cov
```

* Ensures the application behaves as expected
* 32 tests cover arithmetic operations, history, and edge cases

---

## Useful Windows Commands

| Task                    | Command                         |
| ----------------------- | ------------------------------- |
| Activate venv           | `venv\Scripts\activate.bat`     |
| Deactivate venv         | `deactivate`                    |
| Upgrade pip             | `python -m pip install -U pip`  |
| List installed packages | `pip list`                      |
| Export environment      | `pip freeze > requirements.txt` |
| Clear terminal          | `cls`                           |
| Kill Python process     | `Ctrl + C`                      |
| Open file               | `notepad filename.py`           |
| Check Python path       | `where python`                  |
| Check Git path          | `where git`                     |

---

?
