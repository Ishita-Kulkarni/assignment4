📘 Professional Calculator

A modular Python calculator with advanced arithmetic operations and a robust testing framework using pytest.

🚀 Features

Modular architecture (operations, calculation, tests)

Comprehensive unit and parameterized tests

Automatic test discovery with pytest

Continuous integration ready (GitHub Actions support)

Easy to extend with new operations

🧩 Project Structure
professional_calc/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── operations/
│   │   ├── __init__.py
│   │   ├── addition.py
│   │   ├── subtraction.py
│   │   ├── multiplication.py
│   │   └── division.py
│   └── calculation/
│       ├── __init__.py
│       ├── calculation.py
│       └── calculation_factory.py
│
├── tests/
│   ├── __init__.py
│   ├── test_operations.py
│   └── test_calculations.py
│
├── venv/
├── requirements.txt
├── pytest.ini
└── README.md

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/professional_calc.git
cd professional_calc

2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Tests
pytest -v

🧪 Example Usage

You can run the calculator using:

python3 app/main.py


Example in code:

from app.calculation.calculation_factory import get_operation

add = get_operation("add")
print(add(5, 7))  # Output: 12

🧠 Code Documentation

Each file should include:

Docstrings at the top of modules and classes.

Inline comments explaining logic.

Example:

def divide(a, b):
    """
    Performs division of two numbers.

    Args:
        a (float): numerator
        b (float): denominator

    Returns:
        float: result of division
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

🧰 Testing

All tests are located under the tests/ directory.
Use parameterized tests for covering multiple cases efficiently.

Example test:

import pytest
from app.operations.addition import add

@pytest.mark.parametrize("a,b,expected", [(1,2,3), (5,7,12), (-1,1,0)])
def test_add(a, b, expected):
    assert add(a, b) == expected