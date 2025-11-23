import config as cfg

def take_grade():
        return input("Insira a nota: ").strip().replace(",", ".")

def add_grade_to_list(grades_list, temp_grade):
    try:
        grades_list.append(float(temp_grade))
    except ValueError:
        grades_list.append(str(temp_grade))


def add_grade_mean_to_list(mean_grades_list, mean):
    mean_grades_list.append(mean)
    
def calculate_period_grades_mean(grades_list):
    return sum(grades_list) / len(grades_list)
        
def calculate_grades_mean(grades_list, mean_grades_list, period_value):
    x=0
    while x < len(grades_list):
        grade = grades_list[x]
        try:
            mean = (float(grade)*10)/period_value
        except ValueError:
            mean = grade
        mean_grades_list.append(mean)
        x=x+1
            
    return mean_grades_list
                

def take_period_value():
    while True:
        try:
            v = float(input("Insira o valor do período:\n\n"))
            return v
        except ValueError:
            continue
   
def analyze_mean(m):
    # Se for letra, retorna diretamente
    if isinstance(m, str):
        if m in cfg.mean_values:
            return cfg.mean_values[m]
        else:
            raise ValueError(f"Nota desconhecida: {m}")

    # Se for número, percorre os intervalos
    ranges = [
        (1, "0-0.99"),
        (2, "1-1.99"),
        (3, "2-2.99"),
        (4, "3-3.99"),
        (5, "4-4.99"),
        (6, "5-5.99"),
        (7, "6-6.99"),
        (8, "7-7.99"),
        (9, "8-8.99")
    ]

    for limit, key in ranges:
        if m < limit:
            return cfg.mean_values[key]

    # Se for >= 9
    return cfg.mean_values["9-10"]
        
        
        
        
def calcular_ganhos(mean_grades_list, total):
    total = 0
    for m in mean_grades_list:
        value = analyze_mean(m)
        total += value
    return total




    