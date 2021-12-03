 # O programa tem como o âmbito de informar a integridade do pneu, com base na medida do sulco do pneu
 # A medida que o programa trabalha é milímetros, dessa forma para que seja possível o uso do programa, será obrigatório ao usuário informar os milímetros em questão
 # Utilizar sempre o ponto (.) para se referir a números decimais, vírgula (,) não é aceita
 # Com ferramentas de medidas, medir o sulco do pneu para haver informações necessárias para o funcionamento do programa
 # O resultado final obtido será o que falta para o total desgaste do pneu, sendo necessário trocar um pouco antes, variando com o modelo do pneu, fabricante, designação de uso, entre outros.
 

opcao = 0
while opcao != 2:
    print('Escolha o tipo de informação: [1] - porcentagem da medida do sulco do pneu, [2] - Sair')
    opcao = float(input('opcao 1 para obter informção da integridade do pneu e opcao 2 para sair do programa:'))

  
    if opcao == 1:
        print('Aqui você deve colocar a medida em milímetros do sulco do pneu que veio de fábrica')
        medida1 = float(input("digite a medida de origem do sulco:"))
        valor_medida_origem = float(medida1)
        
        print('Aqui você deve colocar a medida em milímetros no momento em que está sendo medido o sulco do pneu')
        medida2 = float(input("digite a medida atual do sulco:"))
        valor_medida_atual = float(medida2)

        print('aqui está o valor da integridade do pneu em porcentagem, ou seja, o quanto ainda resta para que o sulco se nivele à superfície do pneu')
        medida_percentual_do_sulco = (valor_medida_atual/valor_medida_origem)*100
        print(str(medida_percentual_do_sulco) + ' % ' )
        
    elif opcao == 2:
        print('saindo do programa')

    else:
        print('Erro. Digite uma opção válida!')


 
  

    

