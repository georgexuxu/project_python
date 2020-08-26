import math
#inputs
altura = float(input('altura desejada: '))
largura = float(input('largura desejada: '))
#metragem para lona
for i in range(30):
    if i*1.4 < altura :
      pass
    else :
      qnt_lona = i
      sobra = round((i*1.4)- altura,2)
      total_lona =round(largura*qnt_lona,1)
      print('quantas lonas: '+str(qnt_lona))
      print('quanto sobra por lona: '+str(sobra))
      print('metragem para o pedido de lona: '+str(total_lona))
      break
#metragem para a vulcanização
v_lar = round((largura * 4) + ((qnt_lona-1)*largura),2)
v_alt = round(altura * 2,2)
v_total = round(v_alt + v_lar,2)
print('vulcanização necessária na vertical: '+str(v_alt))
print('vulcanização necessária na horizonta: '+str(v_lar))
print('vulcanização total: '+ str(v_total))

#tubo e sarrafo 
#preciso da metragem e quantidade

for i in range(3,7):

        #menor que 6 metros
    if  largura < 6 and i >= largura:
      qnt_sarrafo = 1
      tam_sarrafo = i
      tam_sarrafo_conta = i
      break
    elif  largura > 6 and largura - 6 -i <= 0 and largura<12 :
      qnt_sarrafo = 2
      tam_sarrafo = [6,math.ceil(largura-6)]
      tam_sarrafo_conta = tam_sarrafo[0]+tam_sarrafo[1]
      break
    elif largura > 12 and largura <18 and largura - 12 - i <=0 :
      qnt_sarrafo = 3
      tam_sarrafo = [6,6,math.ceil(largura-12)]
      tam_sarrafo_conta = tam_sarrafo[0]+tam_sarrafo[1]+tam_sarrafo[2]
      break
print('quantidade de sarrafos: ', qnt_sarrafo)
print('tamanho do sarrafo: ', tam_sarrafo)
print('quantidade de tubos: ', qnt_sarrafo)
print('tamanho do tubos: ', tam_sarrafo)


preco_lona = 25 #metroquadrado
preco_sarrafo = 7 #metro
preco_vulcanização = 3.5 #metro
print('--------------------------------------')
print('orçamento custo reduzido')
preco_lona_pedido = round(preco_lona * total_lona,2) 
preco_vulcanização_pedido = round(v_total * preco_vulcanização,2)
preco_sarrafo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
preco_tubo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
preco_total = round(preco_lona_pedido +preco_vulcanização_pedido+preco_sarrafo_pedido+preco_tubo_pedido,2)
print('valores ficticios')
print('preço da lona m²: ',preco_lona,'R$')
print( 'preço sarrafo/tubo o m: ',preco_sarrafo,'R$')
print('preço vulcanização metro linear: ',preco_vulcanização,'R$')
print('---------------------------------------------------')
print('custo dos materiais do pedido')
print('custo lona: ',preco_lona_pedido,'R$')
print('custo vulcanização: ',preco_vulcanização_pedido,'R$')
print('custo sarrafo: ',preco_sarrafo_pedido,'R$')
print('custo tubo: ',preco_sarrafo_pedido,'R$')

print('total: ',preco_total,'R$')

print('___________________________________________________________________________')
lucro = 1.5
print('lucro estipulado: 50%(1.5)')
preco_venda_lona = round(preco_lona_pedido *lucro,2)
preco_venda_vulcanização= round(preco_vulcanização_pedido *lucro,2)
preco_venda_sarrafo = round(preco_sarrafo_pedido * lucro,2)
preco_venda_total = round(preco_total * lucro,2)
print('preço de venda da lona: ' , preco_venda_lona, 'R$' )
print('preço de venda da vulcanização: ' , preco_venda_vulcanização, 'R$' )
print('preço de venda da sarrafo: ' , preco_venda_sarrafo, 'R$' )
print('preço de venda da total: ' , preco_venda_total, 'R$' )

