# AND = para ser true tudo tem q ser true
# OR = para ser true apenas um tem q ser true   


print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_Especial = True

exp = saldo >= saque and saque <= limite or conta_Especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_Especial and saldo >= saque)
print(exp_2)

conta_Normal_Com_Saldo_Suficiente = saldo >= saque and saque <= limite 
conta_Especial_Com_Saldo_Suficiente = conta_Especial and saldo >= saque

exp_3 = conta_Normal_Com_Saldo_Suficiente or conta_Especial_Com_Saldo_Suficiente
print(exp_3)
