from sidecar import Sidecar
from IPython.display import display, HTML
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["animation.html"] = "jshtml"  # <-- IMPORTANT

def showAnimation(movie, frameRate=24):
    """Display an animation in a Jupyter notebook!
       > Needs Sidecar installed."""
    title = getattr(movie[0], "filename", "Animation")
    sc = Sidecar(title=title)
    with sc:
        display(_show_move_as_animation(movie, frameRate))

# Jupyter needs HTML explicitly returned so we can see the animation
def _show_move_as_animation(movie, frameRate=24):
    """
    movie: list of PIL.Image objects
    frameRate: frames per second (matches your GIF writer)
    Returns: HTML object that Jupyter can display as an animation
    """
    if len(movie) == 0:
        raise ValueError("movie is empty")

    # Make sure all frames will be same size
    first = np.array(movie[0])

    fig, ax = plt.subplots()
    ax.axis("off")

    im = ax.imshow(first)

    # Overlay FPS text
    fr_text = ax.text(
        5, 5, f"{frameRate} FPS",
        color="white",
        fontsize=12,
        fontweight="bold",
        bbox=dict(facecolor="black", alpha=0.5, boxstyle="round,pad=0.2")
    )

    def update(i):
        frame = np.array(movie[i])
        im.set_data(frame)
        # no need to change fr_text; FPS is constant
        return im, fr_text

    ani = FuncAnimation(
        fig,
        update,
        frames=len(movie),
        interval=1000 / frameRate,  # ms per frame
        blit=False,                 # <- blit can cause "frozen" look in some setups
        repeat=True
    )
    # Prevent duplicate static figure from showing
    plt.close(fig)

    return HTML(ani.to_jshtml())