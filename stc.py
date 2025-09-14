import matplotlib.pyplot as plt

class StcCalculator: 
    contour = [16, 13, 10, 7, 4, 1, 0, -1, -2, -3, -4, -4, -4, -4, -4, -4] 

    def __init__(self, s, r):  
        self.s = list(s) 
        self.r = list(r) 
        self.tl_dB = [s[i] - r[i] for i in range(16)] 
        self.tl_contour = [(self.tl_dB[i] + StcCalculator.contour[i]) for i in range(16)] 
    
    def test_value(self):  
        for t in range(1, 76):
            rules = [max(0, t - self.tl_contour[i]) for i in range(16)]
            if sum(rules) <= 32 and max(rules) <= 8:
                self.stc_value = t
            else:break
        return self.stc_value
                    
    def show_stc(self):
        if self.stc_value is None:
            raise ValueError('Have to be Used Method test_value()') 
        return {
            "tl_dB": self.tl_dB,
            "graph": [self.stc_value - c for c in StcCalculator.contour],
            "stc": self.stc_value
        }
            
s = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] # Source 
r = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60] # Receiver 

# Input Source and Receiver 125 - 4000dB
stc = StcCalculator(s, r) 
stc.test_value()
result = stc.show_stc()

# พล็อตกราฟ
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

