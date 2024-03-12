while True:
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    
    media = (nota1 + nota2) / 2

    print('A média entre {:.2f} é {:.2f} é igual a {:.2f}'.format(nota1, nota2, media))

    if 7 > media >=5:
        print('Aluno de RECUPERAÇÃO')
    elif media <5:
        print('Aluno REPROVADO')
    elif media >=7:
        print('Aluno APROVADO')
