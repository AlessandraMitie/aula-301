import datetime

dia_de_nasc = datetime.date(day=2, year=1990, month=2)

def calcular_dias_de_vida(data):
# a função recebe um parâmetro data
    if data is None:
        error = 'ops'
        return error

    hoje = datetime.date.today()
    dias_de_vida = hoje - data
    return dias_de_vida

calcular_dias_de_vida(dia_de_nasc)

print(calcular_dias_de_vida(dia_de_nasc))