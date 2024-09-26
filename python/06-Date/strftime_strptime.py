from datetime import datetime



data_hora_atual = datetime.now()
data_hora_str = "2024-09-25 10:20"
mascara_ptbr = '%d/%m/%y %a'
mascara_en = '%Y-%m-%d %H:%M'


print(data_hora_atual.strftime(mascara_ptbr))


data_converrtida = datetime.strptime(data_hora_str, mascara_en)

print(data_converrtida)
print(type(data_converrtida))