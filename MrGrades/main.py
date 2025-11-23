import utils as u 
import config as cfg

total =0
mean_grades_list = []
grades_list = []
mean_values = {"0-0.99": -30, "1-1.99": -30, "2-2.99": -30, "3-3.99": -30, }

       
period_value = u.take_period_value()



while True:
       temp_grade = u.take_grade()

       if temp_grade == "000":
              break

       u.add_grade_to_list(grades_list, temp_grade)

mean_grades_list = []
period_mean = u.calculate_period_grades_mean(grades_list)
u.calculate_grades_mean(grades_list, mean_grades_list, period_value)



for m in mean_grades_list:
    print(m)


u.calcular_ganhos(mean_grades_list)


print(f"{grades_list}\n")
print(total)
        

