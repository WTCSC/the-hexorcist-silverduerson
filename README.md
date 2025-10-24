# Hexorcist – Base Converter Powered by Agony and Despair

Hexorcist is a simple yet versatile **number base converter** written in Python. It can convert numbers between any base from **2 to 36**. This project also includes a set of **automated tests** using `pytest` to ensure correctness.

---

## Features

- Convert numbers from any base (2–36) to decimal.
- Convert decimal numbers to any base (2–36).
- Handles uppercase and lowercase letters seamlessly.
- Validates input for base compatibility and invalid characters.
- Includes round-trip testing to ensure accurate conversions.

---

## Getting Started

### Prerequisites

- Python 3.x
- `pytest` (for running tests)

Install pytest using pip if you don’t have it:

`bash
pip install pytest`

## Usage

Run `python Hexorcist.py`

### Example Run

Welcome to the Hexorcist the converter powered by agony and despair                       
Enter your number (e.g., 'C7'): 12                                    
Enter the original base (2-36): 5                                  
Enter the target base (2-36): 12                                              

12 (base 5) = 7 (base 12)

## Run Test

Bash `pytest`

#### Test should output

Test session starts
collected 3 items

test_hexorcist.py ...   [100%]

3 passed in 0.02s

