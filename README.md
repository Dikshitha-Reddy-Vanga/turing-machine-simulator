# Turing Machine Simulator

A Python-based implementation of a Turing Machine simulator that demonstrates the working of a fundamental computational model. This project includes a working example of a binary increment machine.

---

## Project Overview

This project simulates a Turing Machine, a theoretical model of computation used in computer science to understand how algorithms work at a fundamental level. The simulator allows defining states, transitions, and tape operations, and executes step-by-step computation on an input string.

A binary increment example is implemented to demonstrate how a Turing Machine processes and transforms input.

---

## Features

* Generic Turing Machine implementation
* Configurable states, symbols, and transitions
* Step-by-step execution with tape visualization
* Head movement tracking (Left, Right, Stay)
* Accept and reject state handling
* Maximum step limit to prevent infinite loops
* Example: Binary increment operation

---

## Tech Stack

* Python 3
* Collections module (defaultdict)

---

## Project Structure

```id="p3k9sd"
Turing machine.py
README.md
```

---

## How It Works

The Turing Machine consists of:

* Tape: Infinite memory represented using a dictionary
* Head: Reads and writes symbols on the tape
* States: Define the current condition of the machine
* Transition Function: Determines next action based on current state and symbol

Each transition follows the format:

```id="k2l9qp"
(current_state, symbol) -> (new_state, write_symbol, move)
```

Where move can be:

* L (Left)
* R (Right)
* S (Stay)

---

## Example: Binary Increment

The included example simulates binary addition by incrementing a binary number.

### Sample Inputs

* 1011 → Output: 1100
* 111 → Output: 1000
* 0 → Output: 1
* Empty input → Output: 1

---

## How to Run

1. Ensure Python is installed
2. Download or clone the repository
3. Open terminal in the project folder

Run the program:

```id="l8m2xs"
python "Turing machine.py"
```

---

## Output

The simulator displays:

* Initial tape state
* Each computation step
* Head position
* Final result and number of steps

---

## Future Improvements

* Add support for multiple predefined Turing Machines
* Create a GUI-based simulator
* Allow user-defined input via command line
* Export execution trace to file
* Add visualization for state transitions

---

## Author

Dikshitha Reddy Vanga

---

## License

This project is open-source and available under the MIT License.
