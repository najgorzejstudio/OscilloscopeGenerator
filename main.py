import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy import signal
import functions as f
from functions import format_time, format_voltage

# ==== FILL THESE IN ====
waveform = "sine"         # "sine", "rect", "triangle", "sawtooth"
freq = 1000              # Hz
Vpp = 4              # peak-to-peak volts
time_per_div = 0.0001  # seconds per division s/div
V_div = 1                 # volts per division (optional, not needed for plot)
probe = 1                 # 1 if using 1x probe / 10 if using 10x probe
dc_offset = 0           # volts, positive shifts waveform up, negative down
duty_factor = 50        #fraction (or percent) of one period where the pulse is high, keep > 0

# Trigger parameters
use_trigger = False            # True/False
trigger_level = -3             # volts
slope = 'rising'              #rising/falling

# ==== GENERATED PARAMETERS ====
num_divs = 10                                   # typical oscilloscope screen width
total_time = time_per_div * num_divs            # span of horizontal axis
t = np.linspace(0, total_time, 2000)  # generate time axis
amp = (Vpp / 2) * probe

if waveform == "sine":
    y = amp * np.sin(2 * np.pi * freq * t) + dc_offset
elif waveform == "rect":
    y = amp * signal.square(2 * np.pi * freq * t, duty=duty_factor/100) + dc_offset
elif waveform == "triangle":
    y = amp * signal.sawtooth(2 * np.pi * freq * t, width=0.5) + dc_offset
elif waveform == "sawtooth":
    y = amp * signal.sawtooth(2 * np.pi * freq * t) + dc_offset
else:
    raise ValueError("Unknown waveform type. Use sine, square, triangle, or sawtooth.")


idx = f.trigger_index(y, trigger_level, slope)
y_trig = y[idx:idx+500]
t_trig = t[:len(y_trig)]
fig, ax = plt.subplots()

# ==== SET COLORSCHEME ====

f.set_colorscheme("white", fig, ax, t_trig if use_trigger else t, y_trig if use_trigger else y,
                  {"grid": "black", "plot": "white", "bg": "white",
                   "line": "#1f77b4"})  # white, oscilloscope-digital, oscilloscope-analog, custom


if use_trigger:
    plt.title(f"Trigger level: {trigger_level} V  |  Slope: {slope}  |  {f.format_freq(freq)}  "
              f"|  {Vpp} Vpp  |  {f.format_time_div(time_per_div)}")
else:
    plt.title(f"{waveform} wave |  {f.format_freq(freq)}  |  {Vpp} Vpp  |  {f.format_time_div(time_per_div)}")

plt.gca().xaxis.set_major_formatter(FuncFormatter(format_time))
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_voltage))
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()
