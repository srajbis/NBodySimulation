import pytest
from src.vector import Vector
from src.body import Body
from src.simulation import Simulation

def test_body_initialization():
    b = Body("Test", 10, Vector(0, 0), Vector(1, 1))
    assert b.name == "Test"
    assert b.mass == 10
    assert b.position.x == 0
    assert b.velocity.y == 1

def test_reset_force():
    b = Body("Body", 5, Vector(0, 0), Vector(0, 0))
    b.force = Vector(10, -5)
    b.reset_force()
    assert b.force.x == 0 and b.force.y == 0

def test_add_force_between_two_bodies():
    b1 = Body("A", 5.972e24, Vector(0, 0), Vector(0, 0))
    b2 = Body("B", 7.348e22, Vector(384400000, 0), Vector(0, 0))  # vzdálenost Země–Měsíc
    b1.reset_force()
    b2.reset_force()
    b1.add_force(b2)
    assert b1.force.x > 0  # přitažlivost ve směru k b2
    # Neověřujeme sílu na b2, protože metoda ji sama neaktualizuje


def test_update_position_and_velocity():
    sim = Simulation(dt=1)
    b = Body("Body", 1, Vector(0, 0), Vector(1, 0))
    sim.add_body(b)

    sim.compute_forces()
    sim.step()

    # správné hodnoty podle pořadí aktualizace v Simulation.step()
    assert b.position.x == 1.0  # pozice se zvýšila o v*dt, akcelerace ještě nebyla započtena
    assert b.velocity.x == 1.0  # rychlost se aktualizovala částečně podle nové akcelerace