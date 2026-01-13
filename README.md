# NBodySimulation

This project is a Python-based simulator of gravitational interactions between multiple celestial bodies (N-body problem). 
The default configuration simulates a binary star system with two suns and a single planet on an unstable orbit. Additional configurations can be tested. 
It uses **Velocity Verlet integration** for numerical stability and allows visualization of the trajectories over time.

## Features

- **Multi-body Simulation:** Gravitational interactions between multiple celestial bodies.
- **Numerical Stability:** Accurate position and velocity updates using the Velocity Verlet method.
- **Visualization:** Real-time trajectory animation using `matplotlib`.
- **Extensibility:** Easily extendable to more bodies or different initial conditions.
- **Custom Vector Library:** Implementation of 2D vector operations (addition, subtraction, normalization, magnitude) for physical calculations.

## Project structure
Source Code (src folder):

main.py: The main entry point. Contains the initial conditions (mass, velocity, position) and runs the simulation loop.

simulation.py: The simulation engine. Contains the Simulation class responsible for force calculations and time stepping.

body.py: Definition of the Body class. Represents a celestial body with mass, position, velocity, force, and color.

vector.py: A helper class for 2D vector mathematics with operator overloading.

visualize.py: A module for rendering animations and managing graphical output.

Testing (tests folder)

test_body.py: Verifies the accuracy of gravitational force calculations.

test_vector.py: Tests the mathematical operations of the vector library.

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
It is recommended to use a virtual environment:

```bash
python -m venv venv
```
Activate the enviroment:

```bash
.\venv\Scripts\activate
```

Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```


### 3. Run the Simulation
Launch the main script with this command:

```bash
python src/main.py
```

> NOTE: Body properties (mass, initial position, velocity) can be edited directly in the main.py file to experiment with different orbital setups.


## Physic backround
The program solves Newton's Law of Universal Gravitation: F = G * (m1 * m2) / r^2. To update the state of the system, the Velocity Verlet algorithm is used in three phases:

1) Update positions based on current velocity and acceleration.

2) Calculate new forces (and thus new acceleration) at the new positions.

3) Update velocities using the average of the old and new acceleration.

> NOTE: Because planets are modeled as infinitesimal points, the simulation may become unstable if two bodies get too close. In these cases, the gravitational force can become realistically high due to the $1/r^2$ calculation, leading to a "slingshot" effect or calculation errors. Softening factor needs to be implemented.


## Automated tests
The project includes a suite of tests to ensure calculation integrity. Run the tests using pytest:
Command: 
```bash
pytest
```
The tests specifically check:

Accurate force summation during multi-body interactions.

Correct vector normalization.

Handling of edge cases, such as preventing division by zero during body collisions.



