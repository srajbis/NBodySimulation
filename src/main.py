import math
from simulation import Simulation
from body import Body
from vector import Vector
from visualize import animate_trajectories

sim = Simulation(dt=3600)  # 1 hod timestep

# parametry dvou slunci
d = 2e11
G = 6.67430e-11
M_sun = 1.989e31

# circular speed of each sun
v_sun = math.sqrt(G*M_sun / (d/2)) / 10
Sun1 = Body("Sun1", M_sun, Vector(-d/2, 0), Vector(0,  v_sun), sim_color="orange")
Sun2 = Body("Sun2", M_sun, Vector(d/2,  0), Vector(0, -v_sun), sim_color="red")

#smaller planet orbiting both suns
r_planet = 2 * d
v_planet = math.sqrt(G * (2*M_sun) / r_planet)
Planet = Body("Planet", 5.972e27, Vector(r_planet, 0), Vector(0, v_planet), sim_color="blue")

sim.add_body(Sun1) #pridani objektu do simulace
sim.add_body(Sun2)
sim.add_body(Planet)

positions = {} # vytvoření prázdného SLOVNÍKU
for b in sim.bodies: # sim.bodies je seznam všech těles přidaných v simulaci
    # Vytvoření prázdného SEZNAMU pod jménem tělesa (klíčem)
    positions[b.name] = []
# vysledna struktura je seznam prazdnych seznamu, zabaleny ve slovniku


n_steps = 24 * 365 *10  # 10 years of one hour steps

for step in range(n_steps):
    sim.step()  # Posuneme vesmír o jeden krok simulace, .step definovan v simulation.py
    
    # Teď musíme uložit aktuální polohy všech těles
    for b in sim.bodies: 
        aktualni_jmeno = b.name           # zjistíme jméno tělesa
        aktualni_seznam = positions[aktualni_jmeno]  # najdeme ten správný seznam pro aktualni těleso
        
        # Vytvoříme NOVÝ objekt s aktuálními čísly
        nova_pozice = Vector(b.position.x, b.position.y) #.position je definovano v body.py. .x a .y definovano ve vector.py
        
        # Přidáme tuhle kopii do seznamu
        aktualni_seznam.append(nova_pozice)

colors = {}  # vytvoříme prázdný slovník, do ktereho ulozime informace z nasledujiciho for cyklu
for b in sim.bodies: 
    jmeno = b.name
    barva = b.sim_color
    # vložení jména (klíč) a k němu odpovídající barvy (hodnota) do slovníku
    colors[jmeno] = barva

animate_trajectories(positions, interval=1, colors = colors) #volani fce ze souboru visualize.py
print("Simulation complete.")
