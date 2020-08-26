#inputs
altura = float(input('altura desejada: '))
largura = float(input('largura desejada: '))
#metragem para lona

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