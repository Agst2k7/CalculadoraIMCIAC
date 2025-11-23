def analyze_mean(mean_values, m):
    value = 0
    if m <1: value = mean_values["0-0.99"]
    elif m <2 : value = mean_values["1-1.99"]
    elif m <3 : value = mean_values["2-2.99"]
    elif m <4 : value = mean_values["3-3.99"]
    elif m <5 : value = mean_values["4-4.99"]
    elif m <6 : value = mean_values["5-5.99"]
    elif m <7 : value = mean_values["6-6.99"]
    elif m <8 : value = mean_values["7-7.99"]
    elif m <9 : value = mean_values["8-8.99"]
    else: value = mean_values["9-10"]
    return value
        
        
        
def calcular_ganhos(mean_grades_list, mean_values, total):
    
    for m in mean_grades_list:
        value = analyze_mean(mean_values, m)
        total += value
    return total


mean_values = {"0-0.99": -30, "1-1.99": -30, "2-2.99": -30, "3-3.99": -30, "4-4.99": -20, "5-5.99": -10, "6-6.99": 0, "7-7.99": 10, "8-8.99": 20, "9-10": 30}
total = 0
mean_grades_list = [7, 9, 8]



total = calcular_ganhos(mean_grades_list, mean_values, total)

print(total)