from collections import defaultdict

class TuringMachine:
    def __init__(self, 
                 states, 
                 input_symbols, 
                 tape_symbols, 
                 blank_symbol, 
                 transitions, 
                 start_state, 
                 accept_states, 
                 reject_states=None, 
                 max_steps=10000):
        self.states = set(states)
        self.input_symbols = set(input_symbols)
        self.tape_symbols = set(tape_symbols)
        self.blank_symbol = blank_symbol
        self.transitions = transitions  # dict: (state, symbol) -> (new_state, write_symbol, move)
        self.start_state = start_state
        self.accept_states = set(accept_states)
        self.reject_states = set(reject_states or [])
        self.max_steps = max_steps

    def run(self, input_string, show_steps=True):
        # initialize tape as a defaultdict of blank_symbol and ensure at least index 0 exists
        tape = defaultdict(lambda: self.blank_symbol)
        if input_string:
            for i, ch in enumerate(input_string):
                tape[i] = ch
        else:
            tape[0] = self.blank_symbol  # ensure non-empty tape for printing

        head = 0
        state = self.start_state
        steps = 0

        if show_steps:
            lo, hi = min(tape.keys()), max(tape.keys())
            print("Initial tape:", ''.join(tape[i] for i in range(lo, hi+1)))
            self._print_tape(tape, head)

        while steps < self.max_steps:
            current_symbol = tape[head]
            key = (state, current_symbol)
            if state in self.accept_states:
                if show_steps:
                    print(f"Machine entered accept state '{state}' after {steps} steps.")
                return True, self._tape_to_string(tape), steps
            if state in self.reject_states:
                if show_steps:
                    print(f"Machine entered reject state '{state}' after {steps} steps.")
                return False, self._tape_to_string(tape), steps

            if key not in self.transitions:
                # no defined transition -> reject (or halt)
                if show_steps:
                    print(f"No transition defined for state '{state}' with symbol '{current_symbol}'. Halting and rejecting.")
                return False, self._tape_to_string(tape), steps

            new_state, write_symbol, move = self.transitions[key]
            # perform action
            tape[head] = write_symbol
            if move == 'R':
                head += 1
            elif move == 'L':
                head -= 1
            elif move == 'S':
                pass
            else:
                raise ValueError("Move must be 'L', 'R', or 'S' (stay).")

            state = new_state
            steps += 1

            if show_steps:
                print(f"Step {steps}: ({key}) -> (state='{new_state}', write='{write_symbol}', move='{move}')")
                self._print_tape(tape, head)

        # exceeded max steps
        if show_steps:
            print(f"Exceeded maximum steps ({self.max_steps}). Halting and rejecting.")
        return False, self._tape_to_string(tape), steps

    def _tape_to_string(self, tape):
        # convert to string trimming leading/trailing blanks
        indices = list(tape.keys())
        lo, hi = min(indices), max(indices)
        s = ''.join(tape[i] for i in range(lo, hi+1))
        return s.strip(self.blank_symbol) or self.blank_symbol

    def _print_tape(self, tape, head):
        indices = list(tape.keys())
        lo, hi = min(indices), max(indices)
        tape_str = ''.join(tape[i] for i in range(lo, hi+1))
        head_pos = head - lo
        print("Tape: ", tape_str)
        print("       " + " " * head_pos + "^ (head)")
        print("")

# === Binary increment TM definition ===
blank = '_'
states = {'q0', 'q1', 'q_accept'}
input_symbols = {'0','1'}
tape_symbols = {'0','1', blank}
start_state = 'q0'
accept_states = {'q_accept'}

# transitions: (state, symbol) -> (new_state, write_symbol, move)
transitions = {
    ('q0','0'): ('q0','0','R'),
    ('q0','1'): ('q0','1','R'),
    ('q0', blank): ('q1', blank, 'L'),

    ('q1','0'): ('q_accept','1','S'),
    ('q1','1'): ('q1','0','L'),
    ('q1', blank): ('q_accept','1','S'),
}

tm_increment = TuringMachine(
    states=states,
    input_symbols=input_symbols,
    tape_symbols=tape_symbols,
    blank_symbol=blank,
    transitions=transitions,
    start_state=start_state,
    accept_states=accept_states,
    max_steps=1000
)

# === Quick run examples ===
examples = ["1011", "111", "0", ""]  # last is empty tape -> will write 1
for ex in examples:
    print("\n")
    print(f"Input: '{ex or '<empty>'}'")
    accepted, final_tape, steps = tm_increment.run(ex, show_steps=True)
    print(f"Result: accepted={accepted}, final tape (trimmed)='{final_tape}', steps={steps}")
    print("\n\n")
