velocidade  = float(input("Digite a velocidade: "))
if velocidade > 80:
    multa = (velocidade - 80)*5 
    print('Você foi multado em R$ {:.2f}'.format(multa))
    