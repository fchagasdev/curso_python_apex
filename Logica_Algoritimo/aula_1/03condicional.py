# Condicional simples
idade = 16

if idade >= 17:
    print("Pode obeter CNH")
else:
    print("NAo pode obeter CNH")

# Condicional aninhada
    
    media = 8.5

    if media == 10:
        print("Nota maxima! Parabens")
    elif media >= 9:
        print("Ótimo")
    elif media >= 7:
        print("Na Media")
    elif media >= 5:
        print("em exame")
    else:
        print("Reprovado")


        valor = 84
        if valor >= 0 and valor <=100:
            print("o valor esta entre 0 e 100")
        else:
            print("o valor nao esta entre 0 e 100")

            total = 400
            formaPagamento ="a vista"

            if valor >= 100 and formaPagamento == "a vista":
                print("valor a pagar R$ " + str(total *.9))
            else:
                print("valor a pagar R$ " + str(total)) 