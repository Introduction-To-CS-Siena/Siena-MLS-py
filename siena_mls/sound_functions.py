from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .__init__ import JESSound  # type-only, no runtime import

def _show_waveform_plotly_and_play(snd: "JESSound") -> None:
    # Lazy import optional deps so importing this module doesn’t fail outside notebooks
    try:
        import numpy as np
        import plotly.graph_objects as go
        from IPython.display import Audio, display
    except ImportError as e:
        print(f"[waveform] Optional deps missing (Plotly/IPython): {e}. Skipping visualization.")
        return

    # Compute data
    samples = snd.samples
    sr = snd.sampleRate
    t = np.arange(len(samples)) / sr

    # Build figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t,
        y=samples,
        mode="lines",
        line=dict(width=1),
        hovertemplate="t = %{x:.3f}s<br>amp = %{y:.3f}"
    ))
    fig.update_layout(
        title=f"Waveform: {getattr(snd, 'filename', '')} (Sampling Rate: {sr} Hz)",
        xaxis_title="Time (s)",
        yaxis_title="Amplitude",
        height=300
    )

    try:
        display(fig)
    except Exception as e:
        print(f"[waveform] Failed to display Plotly figure: {e}")

    try:
        display(Audio(samples, rate=sr))
    except Exception as e:
        print(f"[waveform] Failed to play audio via IPython Audio: {e}")


def play(sound_file: "JESSound") -> None:
    """
    Play a sound file.

    Parameters:
    sound_file (JESSound): The sound file to be played.
    """
    _show_waveform_plotly_and_play(sound_file)
