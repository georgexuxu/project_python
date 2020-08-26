import math
from tkinter import *
import tkinter as tk
root = tk.Tk()

root.title('BST sistema')
root.iconbitmap()
root.geometry('500x350')
root.config(bg = 'gray',  borderwidth = 0)

def todos_calcuos():
    for i in range(30):
        if i*1.4 < altura :
            pass
        else :
            qnt_lona = i
            sobra = round((i*1.4)- altura,2)
            total_lona =round(largura*qnt_lona,1)
            break
#metragem para a vulcanização
    v_lar = round((largura * 4) + ((qnt_lona-1)*largura),2)
    v_alt = round(altura * 2,2)
    v_total = round(v_alt + v_lar,2)

    #tubo e sarrafo 
    #preciso da metragem e quantidade

    for i in range(3,7):
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

    preco_lona = 25 #metroquadrado
    preco_sarrafo = 9 #metro
    preco_vulcanização = 3.5 #metro
    preco_lona_pedido = round(preco_lona * total_lona,2) 
    preco_vulcanização_pedido = round(v_total * preco_vulcanização,2)
    preco_sarrafo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
    preco_tubo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
    preco_total = round(preco_lona_pedido +preco_vulcanização_pedido+preco_sarrafo_pedido+preco_tubo_pedido,2)
    lucro = 1.5
    preco_venda_lona = round(preco_lona_pedido *lucro,2)
    preco_venda_vulcanização= round(preco_vulcanização_pedido *lucro,2)
    preco_venda_sarrafo = round(preco_sarrafo_pedido * lucro,2)
    preco_venda_total = round(preco_total * lucro,2)

def orcamento_completo() :
    altura = float(altura_input.get())
    largura = float(largura_input.get())
    #quantidade de lona
    for i in range(30):
        if i*1.4 < altura :
            pass
        else :
            qnt_lona = i 
            sobra = round((i*1.4)- altura,2)
            total_lona =round(largura*qnt_lona,1)
            break
#metragem para a vulcanização
    v_lar = round((largura * 4) + ((qnt_lona-1)*largura),2)
    v_alt = round(altura * 2,2)
    v_total = round(v_alt + v_lar,2)

    #tubo e sarrafo 
    #preciso da metragem e quantidade

    for i in range(3,7):
        for i in range(3,7):
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
    preco_mao_de_obra = 200
    preco_lona = 25 #metroquadrado
    preco_sarrafo = 9 #metro
    preco_vulcanização = 3.5 #metro
    preco_lona_pedido = round(preco_lona * total_lona,2) 
    preco_vulcanização_pedido = round(v_total * preco_vulcanização,2)
    preco_sarrafo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
    preco_tubo_pedido = round(preco_sarrafo *tam_sarrafo_conta,2)
    preco_total = round(preco_lona_pedido +preco_vulcanização_pedido+preco_sarrafo_pedido+preco_tubo_pedido+preco_mao_de_obra,2)
    lucro = 2.3
    preco_venda_lona = round(preco_lona_pedido *lucro,2)
    preco_venda_vulcanização= round(preco_vulcanização_pedido *lucro,2)
    preco_venda_sarrafo = round(preco_sarrafo_pedido * lucro,2)
    preco_venda_total = round(preco_total * lucro,2)
    win_orcamento = tk.Tk()
    win_orcamento.title('ORÇAMENTO')
    win_orcamento.iconbitmap()
    win_orcamento.geometry('850x370')
    win_orcamento.config(bg = 'lightgray',  borderwidth = 0)
    #materiais labels
    header_materiais = Label(win_orcamento,text = 'Materiais necessários',bg = 'grey')
    header_materiais.grid(padx = 5, pady = 5,sticky="W",column = 0, row = 0)
    text_altura = 'altura desejada: '+ str(altura)
    altura_label = Label(win_orcamento, text = text_altura,bg = 'lightgrey')
    altura_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 1)
    text_largura = 'largura desejada: '+ str(largura)
    largura_label = Label(win_orcamento, text = text_largura,bg = 'lightgrey')
    largura_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 2)
    text_qnt_lonas = 'quantidade de lonas que será necessário: '+ str(qnt_lona)
    qnt_lonas_label = Label(win_orcamento, text = text_qnt_lonas,bg = 'lightgrey')
    qnt_lonas_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 3)
    text_total_lona = 'metragem para o pedido de lona: '+ str(total_lona)
    total_lona_label = Label(win_orcamento, text = text_total_lona,bg = 'lightgrey')
    total_lona_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 4)
    text_v_total = 'vulcanização total desejada: '+ str(v_total)
    v_total_label = Label(win_orcamento, text = text_v_total,bg = 'lightgrey')
    v_total_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 5)
    text_qnt_sarrafo = 'quantidade necessária de sarrafos: '+ str(qnt_sarrafo)
    qnt_sarrafo_label = Label(win_orcamento, text = text_qnt_sarrafo,bg = 'lightgrey')
    qnt_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 6)
    text_tam_sarrafo = 'tamanho do sarrafo: '+ str(tam_sarrafo)
    tam_sarrafo_label = Label(win_orcamento, text = text_tam_sarrafo,bg = 'lightgrey')
    tam_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 7)
    text_qnt_sarrafo = 'quantos tubos será necessário: '+ str(qnt_sarrafo)
    qnt_sarrafo_label = Label(win_orcamento, text = text_qnt_sarrafo,bg = 'lightgrey')
    qnt_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 8)
    text_tam_sarrafo = 'tamanho do tubo : '+ str(tam_sarrafo)
    tam_sarrafo_label = Label(win_orcamento, text = text_tam_sarrafo,bg = 'lightgrey')
    tam_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =0 , row = 9)
    #custos
    header_custo = Label(win_orcamento,text = 'custos',bg = 'grey')
    header_custo.grid(padx = 5, pady = 5,column = 1, row = 0)
    #
    text_preco_lona = 'custo referente ao m² de lona: '+ str(preco_lona) +'R$'
    preco_lona_label = Label(win_orcamento, text = text_preco_lona,bg = 'lightgrey')
    preco_lona_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 1)
    text_preco_sarrafo = 'custo referente ao m do sarrafo: '+ str(preco_sarrafo)+'R$'
    preco_sarrafo_label = Label(win_orcamento, text = text_preco_sarrafo,bg = 'lightgrey')
    preco_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 2)
    text_preco_vulcanização = 'custo referente ao m da vulcanização: '+ str(preco_vulcanização)+'R$'
    preco_vulcanização_label = Label(win_orcamento, text = text_preco_vulcanização,bg = 'lightgrey')
    preco_vulcanização_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 3)
    text_preco_lona_pedido = 'Custo de lona total do pedido: '+ str(preco_lona_pedido)+'R$'
    preco_lona_pedido_label = Label(win_orcamento, text = text_preco_lona_pedido,bg = 'lightgrey')
    preco_lona_pedido_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 4)
    text_preco_vulcanização_pedido = 'custo de vulcanização total do pedido: '+ str(preco_vulcanização_pedido)+'R$'
    preco_vulcanização_pedido_label = Label(win_orcamento, text = text_preco_vulcanização_pedido,bg = 'lightgrey')
    preco_vulcanização_pedido_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 5)
    text_preco_sarrafo_pedido = 'custo de sarrafo total do pedido: '+ str(preco_sarrafo_pedido)+'R$'
    preco_sarrafo_pedido_label = Label(win_orcamento, text = text_preco_sarrafo_pedido,bg = 'lightgrey')
    preco_sarrafo_pedido_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 6)
    text_preco_sarrafo_pedido = 'custo de tubos total do pedido: '+ str(preco_sarrafo_pedido)+'R$'
    preco_sarrafo_pedido_label = Label(win_orcamento, text = text_preco_sarrafo_pedido,bg = 'lightgrey')
    preco_sarrafo_pedido_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 7)
    text_preco_mao_de_obra = 'custo referente à mão de obra: '+ str(preco_mao_de_obra) +'R$'
    preco_mao_de_obra_label = Label(win_orcamento, text = text_preco_mao_de_obra,bg = 'lightgrey')
    preco_mao_de_obra_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 8)
    text_preco_total = 'custo total do pedido: '+ str(preco_total)+'R$'
    preco_total_label = Label(win_orcamento, text = text_preco_total,bg = 'lightgrey')
    preco_total_label.grid(padx = 5, pady = 5,sticky="W",column =1 , row = 9)
    #preço para o cliente
    header_preco = Label(win_orcamento,text = 'preço de venda', bg = 'grey',)
    header_preco.grid(padx = 5, pady = 5,sticky="W",column = 2, row = 0)
    #
    text_lucro = 'lucro previso na venda '+ str(lucro)
    lucro_label = Label(win_orcamento, text = text_lucro,bg = 'lightgrey')
    lucro_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 1)
    text_preco_venda_lona = 'preço de venda referente ao m² de lona: '+ str(preco_venda_lona)+'R$'
    preco_venda_lona_label = Label(win_orcamento, text = text_preco_venda_lona,bg = 'lightgrey')
    preco_venda_lona_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 2)
    text_preco_venda_sarrafo = 'preço de venda referente ao m do sarrafo: '+ str(preco_venda_sarrafo)+'R$'
    preco_venda_sarrafo_label = Label(win_orcamento, text = text_preco_venda_sarrafo,bg = 'lightgrey')
    preco_venda_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 3)
    text_preco_venda_sarrafo = 'preço de venda referente ao m do tubo: '+ str(preco_venda_sarrafo)+'R$'
    preco_venda_sarrafo_label = Label(win_orcamento, text = text_preco_venda_sarrafo,bg = 'lightgrey')
    preco_venda_sarrafo_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 4)
    text_preco_venda_vulcanização = 'preço de venda referente ao m da vulcanização: '+ str(preco_venda_vulcanização)+'R$'
    preco_venda_vulcanização_label = Label(win_orcamento, text = text_preco_venda_vulcanização,bg = 'lightgrey')
    preco_venda_vulcanização_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 5)
    text_mao_de_obra = 'preço da mão de obra: '+ str(preco_mao_de_obra)+'R$'
    mao_de_obra_label = Label(win_orcamento, text = text_mao_de_obra,bg = 'lightgrey')
    mao_de_obra_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 6)
    text_preco_venda_total = 'preço de venda total do pedido: '+ str(preco_venda_total)+'R$'
    preco_venda_total_label = Label(win_orcamento, text = text_preco_venda_total,bg = 'lightgrey')
    preco_venda_total_label.grid(padx = 5, pady = 5,sticky="W",column =2 , row = 7)

    







altura_label = Label(text='altura')
altura_label.grid(column = 0 , row = 0)
altura_input = Entry(root)
altura_input.grid(column = 0 , row = 1)
altura = altura_input.get()
largura_label = Label(text = 'Largura')
largura_label.grid(column = 2, row = 0, padx = 20)
largura_input = Entry(root)
largura_input.grid(column = 2 , row = 1)
largura = largura_input.get()

orcamento = Button(text = 'orçamento',command = orcamento_completo)
orcamento.grid(column = 1, row = 2)
root.mainloop()