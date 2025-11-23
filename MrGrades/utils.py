def take_grade():
        return input("Insira a nota: ")

def add_grade_to_list(grades_list, temp_grade):
    grades_list.append(float(temp_grade))

def add_grade_mean_to_list(mean_grades_list, mean):
    mean_grades_list.append(mean)
    
def calculate_period_grades_mean(grades_list):
    return sum(grades_list) / len(grades_list)
        
def calculate_grades_mean(grades_list, mean_grades_list, period_value):
    x=0
    while x < len(grades_list):
        grade = grades_list[x]
        mean = (grade*10)/period_value
        mean_grades_list.append(mean)
        x=x+1
            
    return mean_grades_list
                

def take_period_value():
    v = float(input("Insira o valor do período:\n\n"))
    return v
   
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
        
        
        
def calcular_ganhos(mean_grades_list, mean_values):
    total = 0
    for m in mean_grades_list:
        value = analyze_mean(mean_values, m)
        total += value
    return total

    