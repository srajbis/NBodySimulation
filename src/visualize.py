import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_trajectories(positions_dict, interval, save_path=None, colors=None): #save_path a colors jsou volitelne parametry
    fig, ax = plt.subplots() #inicializace grafickeho okna
    
    # nastaveni a pojmenovani os
    ax.set_aspect('equal')
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")

    #výpočet globální limitů x a y os
    all_x = []  # vytvořím prázdný list pro všechny x souřadnice
    # 1. projdu seznamy pozic pro každé těleso
    for pos in positions_dict.values():
        # 2. v každém seznamu projdu jednotlivé prvky (Vektory)
        for p in pos:
            # 3. uložím si jen souřadnici X
            all_x.append(p.x)
    
    # obdobně pro y souřadnice
    all_y = []
    for pos in positions_dict.values():
        for p in pos:
            all_y.append(p.y)

    xmin, xmax = min(all_x), max(all_x) #vícenanásobné přiřazení
    ymin, ymax = min(all_y), max(all_y)

    span = max(xmax - xmin, ymax - ymin)

    ax.set_xlim(xmin - 0.1*span, xmax + 0.1*span) #nastavení limitů os s malým okrajem
    ax.set_ylim(ymin - 0.1*span, ymax + 0.1*span)

    #Vytvoření prázdného slovníku čar a bodů, do kterých se uloží tělesa jako klíče 
    lines = {}
    points = {}
    
    # Procházíme všechna jména těles v našem slovníku pozic
    for name in positions_dict:
        # Nejdříve zjistíme, jestli máme barvu pro toto těleso k dispozici
        if colors is not None and name in colors:
            c = colors[name]  # Pokud ano, vezmeme ji ze slovníku
        else:
            c = 'black'       # Pokud ne (nebo slovník není), dáme černou   
        
        # vytvoříme objekt pro čáru (trajektorii)
        line_list = ax.plot([], [], label=name, color=c)
        # ax.plot vrací seznam o jednom prvku, tak si z něj ten prvek [0] vytáhneme ručně 
        line_object = line_list[0] 
        
        # Vytvoříme objekt pro tečku (aktuální polohu planety)
        point_list = ax.plot([], [], 'o', color=c)
        point_object = point_list[0]
        
        # Uložíme si tyto "ovladače" ke grafice do našich slovníků podle jména
        lines[name] = line_object
        points[name] = point_object

    ax.legend()

    def update(frame):
        # 1. Projdeme všechna tělesa ve slovníku jedno po druhém
        for name in positions_dict:
            # Získáme kompletní historii pozic (seznam objektů Vector) pro dané těleso
            full_history = positions_dict[name]
            
            # 2. Příprava seznamů pro souřadnice X a Y od začátku až po aktuální snímek (frame)
            current_x_coords = []
            current_y_coords = []
            
            
            # iteruju pro všechny body od 0 do frame a pro každý si přidám x a y do seznamů
            for i in range(frame + 1):
                point = full_history[i]
                current_x_coords.append(point.x)
                current_y_coords.append(point.y)
            
            # 3. Aktualizace trajektorie (čáry)
            # Metoda set_data přepíše starou čáru novým seznamem bodů
            # zde přeresluju celou čáru v každém framu
            line_artist = lines[name]
            line_artist.set_data(current_x_coords, current_y_coords)
            
            # 4. Aktualizace polohy tělesa (tečky)
            # Získáme souřadnice z úplně posledního přidaného bodu v aktuálním výběru
            point_artist = points[name]
            last_x = current_x_coords[len(current_x_coords) - 1]
            last_y = current_y_coords[len(current_y_coords) - 1]
            
            # Tečka je technicky čára o jednom bodu, proto musí být souřadnice v seznamu []
            # zde překresluju pouze poslení bod
            point_artist.set_data([last_x], [last_y])
        
        # 5. Funkce musí vrátit seznam všech objektů, které má Matplotlib překreslit
        all_lines = list(lines.values())
        all_points = list(points.values())
        return all_lines + all_points  # vracím seznam všech čar a bodů, potřebné pro blit = true ve FuncAnimation (prekresluje se pouze zmena)

    # 5. SPUŠTĚNÍ ANIMACE
    # Zjistíme počet snímků podle délky historie (všechny seznamy jsou stejně dlouhé)
    first_key = list(positions_dict.keys())[0]
    total_frames = len(positions_dict[first_key])

    # Tady voláme FuncAnimation - všimni si, že 'update' už nemá další parametry
    ani = FuncAnimation(fig, update, frames=total_frames, interval=interval, blit=True)

    # 6. ZOBRAZENÍ NEBO ULOŽENÍ
    if save_path:
        print(f"Ukládám animaci do: {save_path}")
        # writer='ffmpeg' vyžaduje mít v počítači nainstalovaný program ffmpeg
        ani.save(save_path, writer='ffmpeg', fps=30)
    else:
        # Pokud cestu nezadáme, jen otevřeme okno s grafem
        plt.show()