# RM553521 - Rafael Cristofali

print('Bem-Vindo a Vinheria Agnello')

endereco = input('Digite seu endereço: ')
inputText = 'Digite seu ano de nascimento: '
ano = input(inputText)
while (not ano.isnumeric()):
    print('Necessário ser um número inteiro!')
    ano = input(inputText)
ano = int(ano)

if (2023 - ano < 18):
    print('Não é permitida a venda de bebidas alcoolicas para menores de idade!')
else:
    continuar = 'sim'
    valor_total = 0.00
    valor_frete = 15.00

    cod_vinho1 = '1'
    ds_vinho1 = 'Tinto'
    valor_vinho1 = 10.00
    qtd_vinho1 = 0

    cod_vinho2 = '2'
    ds_vinho2 = 'Rosè'
    valor_vinho2 = 15.00
    qtd_vinho2 = 0

    cod_vinho3 = '3'
    ds_vinho3 = 'Branco'
    valor_vinho3 = 20.00
    qtd_vinho3 = 0

    while (continuar == 'sim'):
        inputText = f'Digite o código do vinho que deseja:' \
                    f'\n{cod_vinho1}-{ds_vinho1} (R$ {valor_vinho1})' \
                    f'\n{cod_vinho2}-{ds_vinho2} (R$ {valor_vinho2})' \
                    f'\n{cod_vinho3}-{ds_vinho3} (R$ {valor_vinho3})\n'
        cod = input(inputText)
        while (cod != cod_vinho1 and cod != cod_vinho2 and cod != cod_vinho3):
            print('Código inválido!')
            cod = input(inputText)

        inputText = 'Quantas garrafas deseja? '
        qtd = input(inputText)
        while (not qtd.isnumeric()):
            print('Necessário ser um número inteiro!')
            qtd = input(inputText)
        qtd = int(qtd)
        if (cod == cod_vinho1):
            qtd_vinho1 += qtd
            valor_total += qtd * valor_vinho1
        elif (cod == cod_vinho2):
            qtd_vinho2 += qtd
            valor_total += qtd * valor_vinho2
        else:
            qtd_vinho3 += qtd
            valor_total += qtd * valor_vinho3

        inputText = 'Deseja continuar? (sim/não): '
        continuar = input(inputText)
        while (continuar != 'sim' and continuar != 'não'):
            print('Opção inválida!')
            continuar = input(inputText)

    if (valor_total > 500):
        print('\nVocê recebeu frete grátis!')
    else:
        print(f'\nVocê terá um frete no valor de R$ {valor_frete}')
        valor_total += valor_frete

    print('\nMuito obrigado pela sua compra!')
    print(f'Valor total do pedido: R$ {valor_total}')
    print(f'Quantidade de vinho {ds_vinho1}: {qtd_vinho1}')
    print(f'Quantidade de vinho {ds_vinho2}: {qtd_vinho2}')
    print(f'Quantidade de vinho {ds_vinho3}: {qtd_vinho3}')
    print(f'Endereço de entrega: {endereco}')
