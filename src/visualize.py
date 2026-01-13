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

    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)

    span = max(xmax - xmin, ymax - ymin)

    ax.set_xlim(xmin - 0.1*span, xmax + 0.1*span)
    ax.set_ylim(ymin - 0.1*span, ymax + 0.1*span)

    # create lines and points
    lines = {}
    points = {}

    for name in positions_dict:
        c = colors.get(name, 'black') if colors else 'black'

        line, = ax.plot([], [], label=name, color=c)
        point, = ax.plot([], [], 'o', color=c)
        lines[name] = line
        points[name] = point

    ax.legend()

    def update(frame):
        for name, pos_list in positions_dict.items():
            xs = [p.x for p in pos_list[:frame+1]]
            ys = [p.y for p in pos_list[:frame+1]]
            lines[name].set_data(xs, ys)
            points[name].set_data([xs[-1]], [ys[-1]])
        return list(lines.values()) + list(points.values())

    ani = FuncAnimation(fig, update, frames=len(next(iter(positions_dict.values()))),
                        interval=interval, blit=True)

    if save_path:
        ani.save(save_path, writer='ffmpeg', fps=30, dpi=200) #nefunkcni
    else:
        plt.show()
