# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

#Resumen Ejecutivo:
"""
Los tipos int y float en Python se usan para representar números. El tipo int se utiliza para números 
enteros, es decir, sin decimales, como 5 o -3. Por otro lado, el tipo float se usa para números con 
decimales, como 3.14 o -0.001. La principal diferencia es que los float pueden representar valores 
con decimales, mientras que los int no. Un booleano en Python es un tipo de dato que solo puede tener 
dos valores: True o False. Estos valores resultan de una comparación, como verificar si 5 > 3, lo cual 
devolvería True. Comparaciones como ==, !=, <, >, <=, >= generan valores booleanos. Es importante 
validar rangos y evitar la división entre cero porque, si no se valida un rango, un valor fuera de lo 
esperado podría generar resultados incorrectos. Además, la división entre cero provoca un error de 
ejecución, interrumpiendo el programa, por lo que es esencial evitarla con validaciones previas.

En este documento, se aplicarán fórmulas de conversión, validación de entradas y lógica condicional 
para evaluar situaciones como descuentos o préstamos. Se calcularán estadísticas básicas (suma, promedio, 
verificación de números pares) y se realizarán cálculos financieros de pago y horas extra. También se 
calculará el índice de masa corporal (IMC) y se interpretarán los resultados según las categorías correspondientes.
"""

# Problem 1: Temperature converter and range flag
"""
Description:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina un valor 
booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 y 
false en caso contrario.

Inputs:
- temp_c (float; temperatura en °C).

Outputs:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validations:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Operaciones clave sugeridas:
- Conversión: temp_f = temp_c * 9 / 5 + 32
- Conversión: temp_k = temp_c + 273.15
- Comparación: is_high_temperature = (temp_c >= 30.0)

Test cases:
1) Normal: 
2) Border: 
3) Error: 

"""
# Código
temp_c = float(input("Ingresa la temperatura en Celcius:"))
temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
is_high_temperature = (temp_c >= 30.0)

print( "Fahrenheit:", temp_f)
print("Kelvin:", temp_k)
print("High temperature:", is_high_temperature)


# Problem 2: Work hours and overtime payment
"""
Description:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime 
que indique si el trabajador hizo horas extra.

Inputs:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Outputs:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validations:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de min() y max() para separar horas regulares y extra.
- Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
- Booleano: has_overtime = (hours_worked > 40)


Test cases:
1) Normal: 
2) Border: 
3) Error: 

"""
# Código
try:
    hours_worked = float(input("Ingresa las horas trabajadas en la semana: "))
    if hours_worked < 0 :
        print("Error: invalid input")
    else:
        hourly_rate =float(input("Ingresa el pago por hora: "))
        if hourly_rate < 0:
            print("Error: invalid input")
        else:
            regular_hours = min(hours_worked, 40)
            regular_pay = (regular_hours * hourly_rate)
            overtime_hours = max(hours_worked - 40, 0)
            overtime_pay = (overtime_hours * hourly_rate * 1.5)
            total_pay = regular_pay + overtime_pay
            has_overtime = (hours_worked > 40)
            print("Regular pay:", regular_pay)
            print("Overtime pay:", overtime_pay)
            print("Total pay:", total_pay)
            print("Has overtime:", has_overtime)
except:
        print("Error: invalid character")

# Problem 3: Discount eligibility with booleans
"""
Description:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Inputs:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Outputs:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validations:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Conversión a bool por comparación de strings.
- Booleanos: discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
- Cálculo: final_total = purchase_total * 0.9 si discount_eligible es true, si no, el mismo purchase_total.

Test cases:
1) Normal: 
Ingrese el total de la compra: 1200
¿Es estudiante? (YES/NO): yes
¿Es mayor de edad? (YES/NO): no
Discount eligible: True
Final total: 1080.00

2) Border: 
Ingrese el total de la compra: 1000
¿Es estudiante? (YES/NO): yes
¿Es mayor de edad? (YES/NO): yes
Discount eligible: True
Final total: 900.00

3) Error: 
Ingrese el total de la compra: 1350
¿Es estudiante? (YES/NO): 5
¿Es mayor de edad? (YES/NO): yes
Error: invalid input

"""
# Código
purchase_total = float(input("Ingrese el total de la compra: "))
is_student_text = input("¿Es estudiante? (YES/NO): ").strip().upper()
is_senior_text = input("¿Es mayor de edad? (YES/NO): ").strip().upper()

if purchase_total < 0.0:
    print("Error: invalid input")
else:
    if is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        
        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        
        if discount_eligible:
            final_total = purchase_total * 0.9  
        else:
            final_total = purchase_total
        
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total:.2f}")

# Problem 4: Basic statistics of three integers
"""
Description:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano 
all_even que indique si los tres números son pares.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validations:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Operaciones clave sugeridas:
- sum_value = n1 + n2 + n3
- average_value = sum_value / 3
- max(), min()
- all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

Test cases:
1) Normal: 
Ingrese el primer número: 2
Ingrese el segundo número: 8
Ingrese el tercer número: 10
Sum: 20
Average: 6.67
Max: 10
Min: 2
All even: True

2) Border: 
Ingrese el primer número: -9
Ingrese el segundo número: 10
Ingrese el tercer número: 5
Sum: 6
Average: 2.00
Max: 10
Min: -9
All even: False

3) Error: 
Ingrese el primer número: k
Ingrese el segundo número: 4
Ingrese el tercer número: 9
Error: invalid input

"""
# Código
n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")
n3 = input("Ingrese el tercer número: ")

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
except ValueError:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")

# Problem 5: Loan eligibility (income and debt ratio)
"""
Description:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Inputs:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validations:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de deuda relativa: debt_ratio = monthly_debt / monthly_income
- Booleano: eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

Test cases:
1) Normal:
Ingrese el ingreso mensual: 9000
Ingrese los pagos mensuales de deuda: 0
Ingrese el puntaje de crédito: 750
Debt ratio: 0.00
Eligible: True

2) Border:
Ingrese el ingreso mensual: 7500
Ingrese los pagos mensuales de deuda: 500
Ingrese el puntaje de crédito: 650
Debt ratio: 0.07
Eligible: False

3) Error:
Ingrese el ingreso mensual: 0
Ingrese los pagos mensuales de deuda: 0
Ingrese el puntaje de crédito: 650
Error: invalid input

"""
# Código
monthly_income = input("Ingrese el ingreso mensual: ")
monthly_debt = input("Ingrese los pagos mensuales de deuda: ")
credit_score = input("Ingrese el puntaje de crédito: ")

try:
    monthly_income = float(monthly_income)
    monthly_debt = float(monthly_debt)
    credit_score = int(credit_score)
except ValueError:
    print("Error: invalid input")
else:
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {eligible}")

# Problem 6: Body Mass Index (BMI) and category flag
"""

Description:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Inputs:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Outputs:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validations:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de bmi como float.
- Uso de round(bmi, 2) para mostrar 2 decimales.
- Evaluación de rangos con condiciones encadenadas.

Test cases:
1) Normal:
Ingrese el peso en kilogramos: 60
Ingrese la estatura en metros: 1.80
BMI: 18.52
Underweight: False
Normal: True
Overweight: False

2) Border:
Ingrese el peso en kilogramos: 100
Ingrese la estatura en metros: 1.75
BMI: 32.65
Underweight: False
Normal: False
Overweight: True

3) Error:
Ingrese el peso en kilogramos: ñ
Ingrese la estatura en metros: 1.65
Error: invalid input

"""
# Código
weight_kg = input("Ingrese el peso en kilogramos: ")
height_m = input("Ingrese la estatura en metros: ")

try:
    weight_kg = float(weight_kg)
    height_m = float(height_m)
except ValueError:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")

# Conclusiones
"""
Los enteros se usan para contar y los flotantes para cálculos más precisos, como el BMI. Usarlos juntos es clave para 
obtener resultados exactos. Las comparaciones generan booleanos que usamos en "if" para tomar decisiones, como saber 
si alguien está en un peso saludable. Validar rangos y evitar dividir por cero es importante para evitar errores y 
asegurarnos de que los cálculos sean correctos. Usar "and", "or" y "not" nos permite combinar condiciones y tomar decisiones 
más complejas, como verificar si alguien califica para un préstamo. Estos patrones se aplican en problemas comunes como nómina, 
descuentos o préstamos, donde necesitamos evaluar varias condiciones al mismo tiempo.

"""

# Referencias
"""
- https://www.geeksforgeeks.org/python/python-operators/
- https://docs.python.org/3/tutorial/introduction.html#operators
- https://docs.python.org/3/library/stdtypes.html#boolean-values
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- https://realpython.com/python-conditional-statements/
"""