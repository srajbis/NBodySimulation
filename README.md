# NBodySimulation

This project is a Python simulation of a gravitational **three-body system**, featuring two stars and a planet. It uses **Velocity Verlet integration** for numerical stability and allows visualization of the trajectories over time.

## Features

- **Multi-body Simulation:** Gravitational interactions between multiple celestial bodies.
- **Numerical Stability:** Accurate position and velocity updates using the Velocity Verlet method.
- **Visualization:** Real-time trajectory animation using `matplotlib`.
- **Extensibility:** Easily extendable to more bodies or different initial conditions.

## Requirements

- Python 3.7+
- `matplotlib` library

## How to Run the Simulation

Follow these steps to get the simulation running on your local machine:

### 1. Clone the Repository
Open your terminal and run the following commands:

```bash
git clone https://github.com/srajbis/NBodySimulation
```

Go to folder NBodySimulation

```bash
cd NBodySimulation
```


### 2. Install Required Packages
It is recommended to use a virtual environment. Install the necessary dependencies using:

```bash
python -m venv venv
```

```bash
pip install -r requirements.txt
```


### 3. Run the Simulation
Launch the main script with this command:

```bash
python src/main.py
```


> NOTE: Body properties (mass, initial position, velocity) can be edited directly in the main.py file to experiment with different orbital setups.