
# MIDTERM: Advanced Python Calculator

## Project Overview

The **Advanced Python Calculator** is a command-line based calculator designed to go beyond basic arithmetic. It implements **modern design patterns, robust error handling, and flexible configuration**, while remaining modular and extensible.

Key features include:

* Interactive **REPL interface** for real-time calculations
* Full **arithmetic operations**: addition, subtraction, multiplication, division, square, modulus, power, root, integer division, percent, absolute difference
* **History management** using Pandas, including save/load functionality
* **Undo/Redo** functionality for previous calculations
* **Dynamic plugin system** for extending the calculator without modifying core code
* **Logging** for all operations and errors
* **Environment-based configuration** through `.env` files
* **Modular architecture** using **Factory, Memento, and Observer** design patterns
* Input validation and custom exception handling

The architecture is designed for **easy future enhancements** while maintaining **clean, maintainable, and scalable code**.

---

## Prerequisites

Before setting up the project, ensure the following are installed:

* **Python 3.10+** (64-bit recommended)
* **pip** (Python package manager)
* **Git** (for version control)
* Optional for Windows: **Visual C++ Redistributable** for certain Python packages
* Recommended IDE: **VS Code, PyCharm, or any text editor with Python support**

---

## Windows-Specific Setup

### Enable Long Path Support

Windows has a default 260-character path limit which can break Python projects. To avoid errors:

1. Open **Control Panel → System → Advanced System Settings → Environment Variables**
2. Create a new system variable:

   * Name: `LONG_PATH_TOOL`
   * Value: `1`
3. Reboot your computer

### Install Git

1. [Download Git for Windows](https://git-scm.com/download/win)
2. Select the following options during installation:

   * “Git from the command line and 3rd-party software”
   * “Use Windows default console window”
   * Enable pseudo-console support (optional)
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

### Install Python and pip

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip git -y
python3 --version
pip3 --version
```

### Create Project Folder

```bash
mkdir ~/advanced_calculator
cd ~/advanced_calculator
```

### Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Upgrade pip & Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install python-dotenv pandas colorama pytest pytest-cov
```

---

## Project Implementation

### 1. Directory Structure

A recommended directory structure:

```
advanced_calculator/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── operations/
│   │   ├── __init__.py
│   │   ├── addition.py
│   │   ├── subtraction.py
│   │   └── ...
│   ├── history/
│   │   ├── __init__.py
│   │   ├── history_manager.py
│   ├── observers/
│   │   ├── __init__.py
│   │   ├── logging_observer.py
│   │   ├── autosave_observer.py
│   └── utils/
│       ├── config.py
│       ├── exceptions.py
│       └── helpers.py
│
├── tests/
│   ├── test_operations.py
│   ├── test_history.py
│   └── test_observers.py
│
├── requirements.txt
├── README.md
└── .env
```

This structure separates **operations, history management, observers, and utility functions**, making the project modular and maintainable.

---

### 2. Arithmetic Operations (Factory Pattern)

**Factory Pattern** allows creation of operation objects without specifying concrete classes. Each arithmetic operation has its own class:

#### Example: `addition.py`

```python
class Addition:
    def execute(self, a, b):
        return a + b
```

#### Example: `operation_factory.py`

```python
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction

class OperationFactory:
    @staticmethod
    def get_operation(op_name):
        if op_name == "add":
            return Addition()
        elif op_name == "subtract":
            return Subtraction()
        # Add other operations as needed
```

#### Usage:

```python
factory = OperationFactory()
op = factory.get_operation("add")
result = op.execute(5, 3)  # Output: 8
```

This **makes adding new operations effortless** without touching core code.

---

### 3. Undo/Redo (Memento Pattern)

The **Memento Pattern** saves snapshots of calculator state:

```python
class CalculatorMemento:
    def __init__(self, state):
        self.state = state
```

```python
class Calculator:
    def __init__(self):
        self.history = []
        self.undo_stack = []

    def calculate(self, operation, a, b):
        result = operation.execute(a, b)
        self.history.append(result)
        self.undo_stack.append(result)
        return result

    def undo(self):
        if self.undo_stack:
            removed = self.undo_stack.pop()
            print(f"Undo: removed {removed}")
        else:
            print("Nothing to undo")
```

**Example Workflow:**

```python
calc = Calculator()
add = Addition()
calc.calculate(add, 5, 3)  # 8
calc.undo()                 # Undo last operation
```

---

### 4. Observer Pattern

Observers monitor calculator events for logging or autosaving:

```python
class Observer:
    def update(self, operation_name, result):
        raise NotImplementedError
```

```python
class LoggingObserver(Observer):
    def update(self, operation_name, result):
        with open("logs/app.log", "a") as f:
            f.write(f"{operation_name}: {result}\n")
```

**Usage:**

```python
calc.add_observer(LoggingObserver())
calc.notify("add", 8)
```

---

### 5. Configuration Management (.env)

Use **`python-dotenv`** to load environment variables:

```text
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=50
CALCULATOR_AUTO_SAVE=True
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

Load them in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
history_dir = os.getenv("CALCULATOR_HISTORY_DIR")
```

Perfect — we can absolutely build the README to a **full 550 lines** by continuing to expand **every section with detailed explanations, code snippets, examples, workflows, troubleshooting, and best practices**.

Here’s the plan to reach that goal:

---

## 6. REPL Commands with Examples

The calculator supports an interactive **REPL** (Read-Eval-Print Loop) interface. Users type commands and receive immediate results.

### Arithmetic Commands

* **add**

```text
> add 5 3
Result: 8
```

* **subtract**

```text
> subtract 10 4
Result: 6
```

* **multiply**

```text
> multiply 7 6
Result: 42
```

* **divide**

```text
> divide 12 4
Result: 3
```

* **power**

```text
> power 2 3
Result: 8
```

* **root**

```text
> root 16 2
Result: 4
```

* **modulus**

```text
> modulus 10 3
Result: 1
```

* **integer division**

```text
> int_divide 7 2
Result: 3
```

* **percent**

```text
> percent 50 200
Result: 25.0
```

* **absolute difference**

```text
> abs_diff 7 12
Result: 5
```

---

### History Commands

The calculator keeps a **running history** stored in Pandas DataFrames.

* **history_show**

```text
> history_show
1: add 5 3 = 8
2: subtract 10 4 = 6
```

* **history_clear**

```text
> history_clear
History cleared successfully.
```

* **history_save**

```text
> history_save
History saved to history/history_2025-11-03.csv
```

* **history_load**

```text
> history_load
History loaded from history/history_2025-11-02.csv
```

---

### Utility Commands

* **last_op**

```text
> last_op
Last operation: add 5 3 = 8
```

* **menu**

```text
> menu
Available commands:
add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff, history_show, history_clear, history_save, history_load, last_op, menu, exit
```

* **exit**

```text
> exit
Exiting Advanced Python Calculator...
```

---

## 7. History Management with Pandas

The calculator uses Pandas to **store, manipulate, and persist calculation history**.

### History DataFrame Example

```python
import pandas as pd

history_df = pd.DataFrame(columns=["Operation", "Operands", "Result", "Timestamp"])
```

Adding a calculation:

```python
from datetime import datetime

history_df = history_df.append({
    "Operation": "add",
    "Operands": [5, 3],
    "Result": 8,
    "Timestamp": datetime.now()
}, ignore_index=True)
```

Displaying history:

```python
print(history_df)
```

Saving history to CSV:

```python
history_df.to_csv("history/history_2025-11-03.csv", index=False)
```

Loading history:

```python
history_df = pd.read_csv("history/history_2025-11-03.csv")
```

---

## 8. Error Handling & Input Validation

The calculator uses **custom exceptions** to handle invalid operations:

```python
class InvalidOperationError(Exception):
    pass

class InvalidInputError(Exception):
    pass
```

### Example: Division by Zero

```python
def divide(a, b):
    if b == 0:
        raise InvalidInputError("Division by zero is not allowed")
    return a / b
```

### Example: Invalid Command

```python
command = "multiplyx"
try:
    op = OperationFactory.get_operation(command)
except Exception as e:
    print(f"Error: {e}")
```

---

## 9. Logging

All calculator events are logged for debugging and auditing.

### Configure Logging via `.env`

```
LOG_LEVEL=DEBUG
LOG_OUTPUT=./logs/app.log
```

### Logging Implementation

```python
import logging
import os

log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Calculator started")
```

### Example Log Entry

```
2025-11-03 12:45:21 - INFO - add 5 3 = 8
```

---

## 10. CSV Serialization Example

Persisting **history** ensures users can reload previous sessions.

```python
import pandas as pd

# Save history
history_df.to_csv("history/history.csv", index=False)

# Load history
history_df = pd.read_csv("history/history.csv")
```

**Autosave after each operation:**

```python
class AutoSaveObserver(Observer):
    def update(self, operation_name, result):
        history_df.to_csv("history/history.csv", index=False)
```

---

## 11. Unit Testing with `pytest`

Testing ensures **reliability of operations and workflows**.

### Sample Test: Addition

```python
from app.operations.addition import Addition

def test_addition():
    add = Addition()
    assert add.execute(5, 3) == 8
    assert add.execute(-1, 1) == 0
```

### Run Tests

```bash
pytest -v
pytest --cov=app --cov-report=html --cov-fail-under=90
```

Coverage ensures **all functions and edge cases** are tested.

---

## 12. Plugin System

The calculator supports **dynamic plugins**:

```python
# plugin_example.py
class SquareRootPlugin:
    def execute(self, x):
        return x ** 0.5
```

Load dynamically:

```python
import importlib

plugin = importlib.import_module("plugin_example")
result = plugin.SquareRootPlugin().execute(16)
print(result)  # Output: 4
```

---

## 13. Full Workflow Example

```text
> add 5 3
Result: 8
> multiply 8 2
Result: 16
> history_show
1: add 5 3 = 8
2: multiply 8 2 = 16
> undo
Undo: removed 16
> history_show
1: add 5 3 = 8
```

* Logging saves all operations
* Autosave writes history automatically
* Undo/Redo allows easy corrections

---

## 14. Troubleshooting

**Common Issues & Fixes:**

1. **`ModuleNotFoundError`**

   * Ensure virtual environment is active:

     ```bash
     source venv/bin/activate
     ```
2. **Path too long on Windows**

   * Enable long path support in system settings
3. **Python version mismatch**

   * Use Python 3.10+
   * Check version: `python --version`

---

## 15. Useful Commands

| Task                | Windows                         | Linux/Ubuntu                    |
| ------------------- | ------------------------------- | ------------------------------- |
| Activate venv       | `venv\Scripts\activate.bat`     | `source venv/bin/activate`      |
| Deactivate venv     | `deactivate`                    | `deactivate`                    |
| Upgrade pip         | `python -m pip install -U pip`  | `python3 -m pip install -U pip` |
| List packages       | `pip list`                      | `pip list`                      |
| Export environment  | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Clear terminal      | `cls`                           | `clear`                         |
| Kill Python process | `Ctrl + C`                      | `Ctrl + C`                      |
| Open file           | `notepad filename.py`           | `nano filename.py`              |

---

