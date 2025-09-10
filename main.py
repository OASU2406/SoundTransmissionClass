def input_spl(splS, splR):
    # dB 125 - 4000Hz
    stc_contour = [16, 13, 10, 7, 4, 1, 0, -1, -2, -3, -4, -4, -4, -4, -4, -4]
    source = list(splS) 
    receiver = list(splR)
    tl = []
    for i in range(16):
        tl.append((source[i] - receiver[i]) + stc_contour[i])
    return tl


def stc_test(tl):
    stc_check = []
    test = 0
    log = []
    for main in range(75):
        test += 1
        for i in range(16):
            check = (test - tl[i])
            if check > 0:
                if check <= 8:
                    log.append(check)
            else: log.append(0)
            
        if sum(log) < 32:
            log.clear()
            stc_check.append(1)
        elif sum(log) > 32:
            continue
    return stc_check


def stc_contour(result):
    contour = [16, 13, 10, 7, 4, 1, 0, -1, -2, -3, -4, -4, -4, -4, -4, -4]
    stc_ = result
    graph = []
    for i in range(0, 16):
        graph.append(len(stc_) - (contour[i]))
    return graph

def return_all(tl_dB, graph, stc_result):
    result = [tl_dB, graph, stc_result ]    
    return result


# s = Source r = Receiver 125 - 4000Hz
s = (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
r = (50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50)

tl_dB = input_spl(s, r)
stc_result = stc_test(tl_dB)
graph = stc_contour(stc_result)
result = return_all(tl_dB, graph, stc_result)


print(
    f'TL_dB : {result[0]}\n',
    f'STC : {result[1]}\n',
    f'Result STC : {len(result[2])}'
)
