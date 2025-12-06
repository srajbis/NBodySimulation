import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_trajectories(positions_dict, interval=50, save_path=None):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")

    # compute limits
    all_x = [p.x for pos in positions_dict.values() for p in pos]
    all_y = [p.y for pos in positions_dict.values() for p in pos]
    margin = 0.1
    xmin, xmax = min(all_x)*(1-margin), max(all_x)*(1+margin)
    ymin, ymax = min(all_y)*(1-margin), max(all_y)*(1+margin)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # create lines and points
    lines = {}
    points = {}
    for name in positions_dict:
        line, = ax.plot([], [], label=name)
        point, = ax.plot([], [], 'o')
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
        ani.save(save_path, writer='ffmpeg', fps=30, dpi=200)
    else:
        plt.show()
