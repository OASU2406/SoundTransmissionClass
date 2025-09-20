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

