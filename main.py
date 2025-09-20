from stc import *
s = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] # Source 
r = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60] # Receiver 

# Input Source and Receiver 125 - 4000dB
stc = StcCalculator(s, r)  
stc.test_value() # stc test
result = stc.show_stc() # result

# graph
freq = [125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000]
STC = result['graph'] # data 1
TL_dB = result['tl_dB'] # data 2


plt.plot(range(16), TL_dB, color="gray", label="Transmission Loss (dB)", marker=".")
plt.plot(range(16), STC, color="orange", linestyle="--", label=f"STC{result['stc']}", marker="")

plt.title(f'ASTM-E413') # title
plt.xlabel("Frequency (Hz)") # name Axis x
plt.ylabel("Sound Prssure Level dB") # name Axis y

plt.ylim(0, 75) # range data tldB

plt.xticks(ticks=range(16), labels=freq, rotation=20) # Frequency Hz 125-4000Hz

plt.legend() # name data
plt.grid(True, linestyle="-", alpha=0.4) # grid
plt.show() # showgraph