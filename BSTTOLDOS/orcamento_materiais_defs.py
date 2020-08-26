altura = float(input('altura desejada: '))
largura = float(input('largura desejada: '))

def lona ():
  for i in range(30):
    if i*1.4 < altura :
      pass
    else :
      qnt_lona = i
      sobra = i%1.4 
      total_lona = altura * largura /1.4
      print('quantas lonas: '+str(qnt_lona))
      print('quanto sobra por lona: '+str(sobra))
      print('metragem total de lonas: '+str(total_lona))
      return qnt_lona , sobra , total_lona

def vulcan (lona,qnt_lona):
  v_lar = (largura * 4) + ((qnt_lona-1)*largura)
  print('qq t acontecendo'+str(qnt_lona))
  v_alt = altura * 2
  v_total = v_alt + v_lar
  print('vulcanização necessária na vertical: '+str(v_alt))
  print('vulcanização necessária na horizonta: '+str(v_lar))
  print('vulcanização total: '+ str(v_total))
  return v_alt , v_lar , v_total

  def tubos_e_sarrafos():
    for i in range(3,7):
        #menor que 6 metros
        if i >= largura and 6 - largura>=0:
            qnt_sarrafo = 1
            tam_sarrafo = i
            print('qnt_sarrafo: ',qnt_sarrafo)
            print('tam_sarrafo: ',tam_sarrafo)
            break
        elif largura - 6 -i <= 0 :
            qnt_sarrafo = 2
            tam_sarrafo = i
            print('qnt_sarrafo: ',qnt_sarrafo)
            print('1 sarrafo de 6, outro de : ',tam_sarrafo )
            break
tubos_e_sarrafos()
