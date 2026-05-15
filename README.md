# Monty Hall Simulation

A Python simulation of the Monty Hall problem to empirically prove the winning probability with and without switching doors.

## What is the Monty Hall Problem?

In the Monty Hall problem, a contestant picks one of three doors. Behind one door
is a car; behind the others are goats. The host opens a different door revealing a
goat, then asks if the contestant wants to switch.

Math result: switching raises your win probability from $\frac{1}{3}$ to $\frac{2}{3}$.

## Installation
```
pip install streamlit
```

## Usage
```bash
python main.py 
```
### Sample Output

```
Winning percentage without switching doors: 33.20%
Winning percentage with    switching doors: 66.50%
```

### Launch the dashboard
```
streamlit run app.py
```
Then open http://localhost:8501 in your browser.
## Functions

- `montyhaal(switch)` — simulates a single game. If `switch=True`, the player switches doors.
- `counter(num)` — runs `num` games and returns the win count for each strategy.

## Requirements

* Python 3.x — no external libraries needed.
* streamlit

