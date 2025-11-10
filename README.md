# Oscilloscope Waveform Simulator
##Description

This Python script simulates an oscilloscope display for common waveform types, including sine, rectangular, triangle, and sawtooth waves. It allows visualization of the waveform with typical oscilloscope settings such as V/div, time/div, DC offset, and optional trigger functionality. The display can be customized with different color schemes to mimic either a digital or analog oscilloscope.

###The program supports:
-Selecting waveform type (sine, rect, triangle, sawtooth)
-Setting frequency and amplitude (Vpp)
-Applying a DC offset
-Configuring rectangular wave duty cycle
-Optional trigger at a specific voltage level with rising or falling edge
-Customizable colors for waveform, background, grid, and axes

##How to Use

###Install dependencies (if not already installed):
```
pip install numpy matplotlib scipy
```
or 
```
pip install -r requirements.txt
```

###Configure waveform parameters in the script:
```
waveform = "sine"        # "sine", "rect", "triangle", "sawtooth"
freq = 1000              # Frequency in Hz
Vpp = 4                  # Peak-to-peak voltage
time_per_div = 0.0001    # Seconds per division
dc_offset = 0            # DC offset in volts
duty_factor = 50         # Only for rectangular waveform, percent of high pulse
probe = 1                # 1x or 10x probe
```

###Configure trigger (optional):
```
use_trigger = False      # Set True to enable trigger
trigger_level = -3       # Trigger voltage in volts
slope = 'rising'         # 'rising' or 'falling'
```

###Run the script:
```
python oscilloscope_sim.py
```

##Output:
-A Matplotlib window will open displaying the waveform.
-The title shows waveform type, frequency, amplitude, time/div, and trigger settings (if used).
-Grid, background, and waveform colors can be adjusted in the set_colorscheme function.
