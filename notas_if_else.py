nota1 = int(input('Informe a nota 1º Bimeste (0-100): '))
nota2 = int(input('Informe a nota 2º Bimeste (0-100): '))
media = (nota1 + nota2) / 2
if media >= 60:
    print(f"Você foi aprovado com média {media}")
else:
    print(f"Você não foi aprovado, sua média é {media}")