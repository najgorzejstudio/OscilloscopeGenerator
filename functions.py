import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator
from scipy import signal


def format_time(x, pos):
    # x is in seconds
    abs_x = abs(x)

    if abs_x < 1e-12:
        return "0 µs"

    if abs_x >= 1:
        return f"{x:.3g} s"
    elif abs_x >= 1e-3:
        return f"{x * 1e3:.3g}ms"
    elif abs_x >= 1e-6:
        return f"{x * 1e6:.3g}µs"
    else:
        return f"{x * 1e9:.3g}ns"


def format_voltage(v, pos):
    # v is in volts
    if abs(v) >= 1:
        return f"{v:.3g} V"
    elif abs(v) >= 1e-3:
        return f"{v*1e3:.3g} mV"
    elif abs(v) >= 1e-6:
        return f"{v*1e6:.3g} µV"
    else:
        return f"{v*1e9:.3g} nV"


def format_freq(f):
    if f >= 1e6:
        return f"{f/1e6:.3g} MHz"
    elif f >= 1e3:
        return f"{f/1e3:.3g} kHz"
    elif f >= 1e6:
        return f"{f / 1e6:.2f} MHz"
    return f"{f:.3g} Hz"


def format_time_div(val):
    if val >= 1e-3:
        return f"{val*1e3:.3g} ms/div"
    elif val >= 1e-6:
        return f"{val*1e6:.3g} µs/div"
    elif val >= 1e-9:
        return f"{val*1e9:.3g} ns/div"
    return f"{val:.3g} s/div"


def set_colorscheme(scheme, fig, ax, t, y, dict):
    match(scheme):
        case "white":
            plt.grid(color='black', linestyle='--', linewidth=0.5)
            ax.set_facecolor('white')  # plot background
            fig.patch.set_facecolor('white')  # figure background
            plt.plot(t, y, color = "#1f77b4")
            ax.xaxis.set_minor_locator(MultipleLocator(0.2))
            ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.3, alpha=0.5)
        case "oscilloscope-digital":
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            ax.set_facecolor('black')  # plot background
            fig.patch.set_facecolor('green')  # figure background
            plt.plot(t, y, color="yellow")
        case "oscilloscope-analog":
            plt.grid(color='black', linestyle='-', linewidth=0.7)
            ax.set_facecolor('#257296')  # plot background
            fig.patch.set_facecolor('#257296')  # figure background
            plt.plot(t, y, color="#22ff05")
        case "custom":
            plt.grid(color=dict["grid"], linestyle='--', linewidth=0.7)
            ax.set_facecolor(dict["plot"])  # plot background
            fig.patch.set_facecolor(dict["bg"])  # figure background
            plt.plot(t, y, color=dict["line"])
        case _:
            plt.grid(color='black', linestyle='--', linewidth=0.5)
            ax.set_facecolor('white')  # plot background
            fig.patch.set_facecolor('white')  # figure background
            plt.plot(t, y, color="#1f77b4")


def trigger_index(signal, level, slope):
    if slope == 'rising':
        idx = np.where((signal[:-1] < level) & (signal[1:] >= level))[0]
    else:  # falling
        idx = np.where((signal[:-1] > level) & (signal[1:] <= level))[0]
    return idx[0] if len(idx) > 0 else 0