import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["animation.html"] = "jshtml"  # <-- IMPORTANT

def showAnimation(movie, frameRate=24):
    """Display an animation in a Jupyter notebook."""
    _show_move_with_framerate(movie, frameRate)

def _show_move_with_framerate(movie, frameRate=24):
    """
    movie: list of PIL.Image
    frameRate: frames per second
    """

    # Duration per frame in ms (same as your GIF code)
    interval = 1000 / frameRate

    first = np.array(movie[0])

    fig, ax = plt.subplots()
    im = ax.imshow(first)
    ax.axis("off")

    # Add a framerate text overlay
    txt = ax.text(
        5, 5,
        f"{frameRate} FPS",
        color="white",
        fontsize=12,
        ha="left",
        va="top",
        bbox=dict(facecolor="black", alpha=0.5, pad=3)
    )

    def update(i):
        im.set_data(np.array(movie[i]))
        return [im, txt]

    ani = FuncAnimation(
        fig,
        update,
        frames=len(movie),
        interval=interval,  
        blit=True
    )

    return ani