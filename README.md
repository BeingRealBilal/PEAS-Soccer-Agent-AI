# AI Soccer Agent (PEAS Implementation)

A Python implementation of an Intelligent Agent for a soccer game environment based on the **PEAS** framework.

## Project Structure
- `soccer_agent.py`: Main simulation script.
- `PEAS_Report.docx`: Detailed theoretical breakdown of the agent.

## How it Works
The agent uses **Euclidean sensors** to track the ball. It operates in two main states:
1. **Search & Intercept**: Locating the ball in a 2D plane.
2. **Dribble & Score**: Navigating the ball to the goal and executing a stochastic shooting function.

## Setup
Run the simulation:
```bash
python soccer_agent.py
