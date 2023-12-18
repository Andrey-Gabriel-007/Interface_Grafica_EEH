import functools
from tkinter import *
import numpy as np
from EEH import EEH 

med_tensao = np.zeros(34, dtype=int)
med_corrente = np.zeros(66, dtype=int)

def estimar_button(root,C):
    btn = Button(C, text='Estimar!', width=10,
    height=1, bd='5', command=root.destroy, bg='#151', fg='#fff')
    btn.place(x=950, y=580)

def click(event,C):

    if (event.num == 3): #definir as cores dependendo do click do mouse, 3 é o botão direito
        cor_med_tensao = '#ddd'   #cinza
        cor_med_corrente = '#aaa' #cinza
        operacao = 0
    elif(event.num == 1):  #definir as cores dependendo do click do mouse, 1 é o botão esquerdo
        cor_med_tensao = 'black'
        cor_med_corrente = 'yellow'
        operacao = 1

    for i in range(34):
        if(event.x >= vets_x0y0[i,0] and event.x <= vets_x0y0[i,0]+10 and event.y >= vets_x0y0[i,1] and event.y <=  vets_x0y0[i,1]+10):
            C.create_rectangle(vets_x0y0[i,0],vets_x0y0[i,1],vets_x0y0[i,0]+10,vets_x0y0[i,1]+10,fill=cor_med_tensao,outline='gray')
            med_tensao[i] = operacao
                    
            

    for i in range(34):
    
        if( (vets_x0y0[i,0]-30 <=event.x and vets_x0y0[i,0]+35 >= event.x) and (vets_x0y0[i,1]-15 <=event.y and vets_x0y0[i,1]+25 >= event.y)):
            #Verifica se na barra também existe medidor de tensão, ja que o de corrente só pode ser alocado caso exista... além de ver se é 1 o vetor medidor de corrente
            j=0
            while(j<66):
                
                if((vets_corrente_x0y0[j,2] == 1) ):
                    if(event.x >= vets_corrente_x0y0[j,0] and event.x <= vets_corrente_x0y0[j,0]+10 and event.y >= vets_corrente_x0y0[j,1]-10 and event.y <=  vets_corrente_x0y0[j,1]):
                        C.create_oval(vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]-10,vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1],fill=cor_med_corrente,  outline='#aaa')
                        med_corrente[j] = operacao

                
                elif((vets_corrente_x0y0[j,2] == 2) ):
                    if(event.x >= vets_corrente_x0y0[j,0]+10 and event.x <= vets_corrente_x0y0[j,0]+20 and event.y >= vets_corrente_x0y0[j,1] and event.y <=  vets_corrente_x0y0[j,1]+10):
                        C.create_oval(vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1],vets_corrente_x0y0[j,0]+20,vets_corrente_x0y0[j,1]+10,fill=cor_med_corrente,  outline='#aaa')
                        med_corrente[j] = operacao


                elif((vets_corrente_x0y0[j,2] == 3) ):
                    if(event.x >= vets_corrente_x0y0[j,0] and event.x <= vets_corrente_x0y0[j,0]+10 and event.y >= vets_corrente_x0y0[j,1]+10 and event.y <=  vets_corrente_x0y0[j,1]+20):
                        C.create_oval(vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]+10,vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1]+20,fill=cor_med_corrente,  outline='#aaa')
                        med_corrente[j] = operacao


                elif((vets_corrente_x0y0[j,2] == 4)):
                    if(event.x >= vets_corrente_x0y0[j,0]-10 and event.x <= vets_corrente_x0y0[j,0] and event.y >= vets_corrente_x0y0[j,1] and event.y <=  vets_corrente_x0y0[j,1]+10):
                        C.create_oval(vets_corrente_x0y0[j,0]-10,vets_corrente_x0y0[j,1],vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]+10,fill=cor_med_corrente,  outline='#aaa')
                        med_corrente[j] = operacao

                j+=1
    

    print(med_tensao,med_corrente)

    return event.x,event.y

def mostrar_num_tensao(event,C):   
    for i in range(0,34):
        C.text_med_tensao = C.create_text(vets_x0y0[i,0]-8,vets_x0y0[i,1]-2,text=i+1,fill='black', tag="medidores_tensao")
        if(event.state!=8 and event.state!=10): 
            # C.create_text(vets_x0y0[i,0]-5,vets_x0y0[i,1]-2,text=i+1,fill='white')
            # C.itemconfig(C.text_med_tensao, fill='#fff')
            C.delete("medidores_tensao")




def mostrar_num_corrente(event,C):
    
   
    for j in range(0,66):

        if((vets_corrente_x0y0[j,2] == 4)):
            C.text_med_tensao = C.create_text(vets_corrente_x0y0[j,0]-10+5,vets_corrente_x0y0[j,1]+5-10,text=j+35,fill='#FFBF00', tag="medidores_corrente")

        elif((vets_corrente_x0y0[j,2] == 2) ):
            C.text_med_tensao = C.create_text(vets_corrente_x0y0[j,0]+15,vets_corrente_x0y0[j,1]+5-10,text=j+35,fill='#FFBF00', tag="medidores_corrente")

        elif((vets_corrente_x0y0[j,2] == 1) ):
            C.text_med_tensao = C.create_text(vets_corrente_x0y0[j,0]-6,vets_corrente_x0y0[j,1]-10+5,text=j+35,fill='#FFBF00', tag="medidores_corrente")

        elif((vets_corrente_x0y0[j,2] == 3) ):
            C.text_med_tensao = C.create_text(vets_corrente_x0y0[j,0]-6,vets_corrente_x0y0[j,1]+10+5,text=j+35,fill='#FFBF00', tag="medidores_corrente")
        if(event.state!=8 and event.state!=10):
            # C.itemconfig(C.text_med_tensao, fill='#fff')
            C.delete("medidores_corrente")
    return event

        
def desenhar_todos_medidores(C):
    
    i=0
    while(i<34):
        # C.create_rectangle(vets_x0y0[i,0]+4,vets_x0y0[i,1]-25,vets_x0y0[i,0]+7,vets_x0y0[i,1]+35,fill='#0D0',outline='gray')
        C.create_rectangle(vets_x0y0[i,0],vets_x0y0[i,1],vets_x0y0[i,0]+10,vets_x0y0[i,1]+10,fill='#ddd',outline='#aaa')

        i+=1
       
    j=0
    while(j<66):
        if((vets_corrente_x0y0[j,2] == 4)):
            C.create_oval(vets_corrente_x0y0[j,0]-10,vets_corrente_x0y0[j,1],vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]+10,fill='#aaa',  outline='#aaa')

        elif((vets_corrente_x0y0[j,2] == 2) ):
            C.create_oval(vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1],vets_corrente_x0y0[j,0]+20,vets_corrente_x0y0[j,1]+10,fill='#aaa',  outline='#aaa')

        elif((vets_corrente_x0y0[j,2] == 1) ):
            C.create_oval(vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]-10,vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1],fill='#aaa',  outline='#aaa')

        elif((vets_corrente_x0y0[j,2] == 3) ):
            C.create_oval(vets_corrente_x0y0[j,0],vets_corrente_x0y0[j,1]+10,vets_corrente_x0y0[j,0]+10,vets_corrente_x0y0[j,1]+20,fill='#aaa',  outline='#aaa')

        j+=1





vets_x0y0 = np.load('vets_x0y0.npy')
vets_corrente_x0y0 = np.load('vets_corrente_x0y0.npy')

root = Tk()

root.title('Sistema 34 Barras IEEE')
root.geometry('1050x550')

root.state('zoomed')


C = Canvas(root, bg="white", height=750, width=1340, scrollregion=(0,0,1000,1000))

C.grid(row=0, column=0, sticky=EW)

C.python_image = PhotoImage(file='sistema_34_barras1.png')
C.create_image(470, -5, image=C.python_image, anchor=NW)  

scrollbar = Scrollbar(root,orient='vertical',command= C.yview)
scrollbar.grid(row=0, column=1, sticky=NS)
C['yscrollcommand'] = scrollbar.set

C.bind('<Button-1>', functools.partial(click, C=C));
C.bind('<Button-3>', functools.partial(click,C=C));
root.bind('c', functools.partial(mostrar_num_corrente,C=C));
root.bind('C', functools.partial(mostrar_num_corrente,C=C));
root.bind('t', functools.partial(mostrar_num_tensao,C=C));
root.bind('T', functools.partial(mostrar_num_tensao,C=C));
desenhar_todos_medidores(C)
# Button for closing 
estimar_button(root,C)
root.mainloop() 
######## cenario 5 TCC JÚLIA #########
med_tensao = [0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1]
med_corrente =[0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0
,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0]
########################################


EEH(med_tensao,med_corrente)

