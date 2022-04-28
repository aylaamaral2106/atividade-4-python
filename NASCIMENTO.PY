nome = input("Digite seu primeiro nome: ")

primeiraletra = nome[0:1].upper()
restantenome = nome[1:10].lower()

nome = primeiraletra + restantenome

dia = input("Dia do nascimento: ")
mes = input("Mes do nascimento: ")
ano = input("ano do nascimento: ")


print("{} nasceu no dia: {}/{}/{}".format(nome, dia, mes, ano))




