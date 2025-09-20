# Sound Transmisson Class With Not RT60
* How to use
* Note: SPL = Sound Pressure Level, TL = Transmission Loss
1. Input SPL, Source(s) and Receiver(r) at 125 - 4000kHz 1/3 Octave In class StcCalculator
    ```python
    stc = StcCalculator(s, r) # Example
    ```
2. Use Method test_value to find Result STC and STC graph 
    * Rules totalsum at 125-4000kHZ <= 32 and each Hz <= 8: = Result STC
    * In addition to this Not pass

3. Use Method show_stc for pass Reults

#### As I am a beginner, I would like to receive feedback to help me further develop myself. Thank you.