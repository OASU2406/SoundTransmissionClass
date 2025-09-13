
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

with open("stc.txt", "w", encoding="utf-8") as file:
    file.write(f"TL_dB: {result['tl_dB']}\n")
    file.write(f"Graph: {result['graph']}\n")
    file.write(f"Result STC: {result['stc']}\n")