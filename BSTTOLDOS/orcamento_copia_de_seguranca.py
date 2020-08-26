
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
v_lar = (largura * 4) + ((qnt_lona-1)*largura)
v_alt = altura * 2
v_total = v_alt + v_lar
print('vulcanização necessária na vertical: '+str(v_alt))
print('vulcanização necessária na horizonta: '+str(v_lar))
print('vulcanização total: '+ str(v_total))

#tubo e sarrafo 
#preciso da metragem e quantidade

if largura%6 == 0 :
        qnt_sarrafo = largura/6
        tam_sarrafo = 6
    
elif largura %5 == 0:
        qnt_sarrafo = largura/5
        tam_sarrafo = 5

elif largura %4 == 0 :
        qnt_sarrafo = largura/4
        tam_sarrafo = 6
elif largura == 3 :
        qnt_sarrafo = 1
        tam_sarrafo = 3
else:
    if largura %6 <3 :
        qnt_sarrafo = round(largura/6,0) 
        tam_sarrafo = 6
        print('+1 sarrafo de 3 para completar')
        sobra_sarrafo = largura - (qnt_sarrafo*tam_sarrafo)
        

    elif largura%5 < 3 :
        qnt_sarrafo = round(largura/5,0) 
        tam_sarrafo = 6
        sobra_sarrafo = largura - (qnt_sarrafo*tam_sarrafo)
            
    elif largura%4<3 :
        qnt_sarrafo = round(largura/4,0) 
        tam_sarrafo = 5
        sobra_sarrafo = largura - (qnt_sarrafo*tam_sarrafo)
    elif largura%3<3:
        qnt_sarrafo = round(largura/3,0)  
        tam_sarrafo = 4
        sobra_sarrafo = largura - (qnt_sarrafo*tam_sarrafo)
print('quantidade de sarrafos: ', qnt_sarrafo)
print('tamanho do sarrafo: ', tam_sarrafo)
print('quantidade de tubos: ', qnt_sarrafo)
print('tamanho do tubos: ', tam_sarrafo)
print('sobra de sarrafo: ', sobra_sarrafo)

