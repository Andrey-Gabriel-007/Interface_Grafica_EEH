import functools
# import os
from tkinter import *
import numpy as np

# from PIL import ImageTk
vet_x0=  np.zeros(34)
vet_y0=  np.zeros(34)
vet_corrente_x0=  np.zeros(66)
vet_corrente_y0=  np.zeros(66)
vet_corrente_position=  np.zeros(66)
vets_x0y0 = np.load('vets_x0y0.npy')
vets_corrente_x0y0 = np.load('vets_corrente_x0y0.npy')

# def open_main(event,root,C):
#     # if(event.x<= 950-100 and event.x >=950+100 and event.y<= 580-20 and event.x >=580+20):
#         C.destroy
#         root.destroy
#         os.system('python main.py')
    


# def reset_button(root,C):
#     reiniciar_btn = Button(C, text='Reiniciar', width=10,
#     height=1, bd='5', command=root.bind('<Button-1>', functools.partial(open_main,root=root, C=C)), bg='#000', fg='#fff')
#     reiniciar_btn.place(x=950, y=580)

def mostrar_num_tensao(event,C):   
    for i in range(0,34):
        if(C.med_tensao[i]==1):
            C.text_med_tensao = C.create_text(vets_x0y0[i,0]-8,vets_x0y0[i,1]-2,text=i+1,fill='black', tag="medidores_tensao")
            if(event.state!=8 and event.state!=10): 
                # C.create_text(vets_x0y0[i,0]-5,vets_x0y0[i,1]-2,text=i+1,fill='white')
                # C.itemconfig(C.text_med_tensao, fill='#fff')
                C.delete("medidores_tensao")


    # desenhar_todos_medidores(C)  


def mostrar_num_corrente(event,C):
    
    for j in range(0,66):
        if(C.med_corrente[j]==1):
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

    # desenhar_todos_medidores(C)  
    return event
def barras(C,x0,y0,posicao):
        i=C.count_medidor_tensao
        if(posicao== 'h' ):
             # if( C.ERRO[i*3:i*3+3].any == 0 and C.ERRO[i*3+102:i*3+3+102].any == 0):
            if( C.ERRO[i*3] == 0 and C.ERRO[i*3+1] == 0  and C.ERRO[i*3+2] == 0 and ( C.ERRO[i*3+102] == 0 and C.ERRO[i*3+1+102] == 0  and C.ERRO[i*3+2+102] == 0) ):
                C.create_rectangle(x0+4,y0-25,x0+7,y0+35,fill='#0D0',outline='gray')#Cria barra Verde
            else: 
                C.create_rectangle(x0+4,y0-25,x0+7,y0+35,fill='#F00',outline='gray')#Cria barra Verde

        elif(posicao== 'v' ):
            if( C.ERRO[i*3] == 0 and C.ERRO[i*3+1] == 0  and C.ERRO[i*3+2] == 0 and ( C.ERRO[i*3+102] == 0 and C.ERRO[i*3+1+102] == 0  and C.ERRO[i*3+2+102] == 0)):
                C.create_rectangle(x0-25,y0+4,x0+35,y0+7,fill='#0D0',outline='gray') #Cria barra verde
            else: 
                C.create_rectangle(x0-25,y0+4,x0+35,y0+7,fill='#F00',outline='gray') #Cria barra Vermelha


def medidor(C,x0,y0,posicao):
    barras(C,x0,y0,posicao) 
    if(C.med_tensao[C.count_medidor_tensao] == 1):
        vet_x0[C.count_medidor_tensao] = x0
        vet_y0[C.count_medidor_tensao] = y0

        
        C.create_rectangle(x0,y0,x0+10,y0+10,fill='black',outline='gray') #Cria Medidor de tensao

    C.count_medidor_tensao+=1
    return C

def medidor_corrente(C,x0,y0,somente):
    vet_corrente_x0[C.count_medidor_corrente] = x0
    vet_corrente_y0[C.count_medidor_corrente] = y0
    if(somente == 'c'):
        vet_corrente_position[C.count_medidor_corrente]= 1
    if(somente == 'd'):
        vet_corrente_position[C.count_medidor_corrente]= 2
    if(somente == 'b'):
        vet_corrente_position[C.count_medidor_corrente]= 3
    if(somente == 'e'):
        vet_corrente_position[C.count_medidor_corrente]= 4
    i=0;
    while(i<34):
        if( (vet_x0[i]-30 <=x0 and vet_x0[i]+35 >= x0) and (vet_y0[i]-15 <=y0 and vet_y0[i]+25 >= y0)  and C.med_corrente[C.count_medidor_corrente] == 1):
            #Verifica se na barra também existe medidor de tensão, ja que o de corrente só pode ser alocado caso exista... além de ver se é 1 o vetor medidor de corrente
                if((somente == 'e') and somente != 'ed'):
                    C.create_oval(x0-10,y0,x0,y0+10,fill='yellow',  outline='gray')
                elif((somente == 'd') and somente != 'ed'):
                    C.create_oval(x0+10,y0,x0+20,y0+10,fill='yellow',  outline='gray')
                if((somente == 'c') and somente != 'cb'):
                    C.create_oval(x0,y0-10,x0+10,y0,fill='yellow',  outline='gray')
                elif((somente == 'b') and somente != 'cb'):
                    C.create_oval(x0,y0+10,x0+10,y0+19,fill='yellow',  outline='gray')
        i+=1
    C.count_medidor_corrente+=1



# def barra(C,x0,y,posicao,somente):
#     C.create_rectangle(0,10,60,13,fill='green',outline='gray')
#     return C

# def Button(event):
#     for i in range(34):
#         if(event.x >= vet_x0[i]-10 and event.x <= vet_x0[i]+10 and event.y >= vet_y0[i]-13 and event.y <=  vet_y0[i]+13):
#             Canvas.create_rectangle(vet_x0[i],vet_y0[i],vet_x0[i]+10,vet_y0[i]+10,fill='green',outline='gray')

    # return event.x,event.y
def interface_resultados( med_tensao, med_corrente, ERRO):
    root = Tk()
   

    # root.resizable(False, TRUE)
    # root.title("Scrollbar Widget Example")
    # apply the grid layout
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    # root.widget1 = Frame(root)

    # root.msg = Label(root.widget1, text="Sistema 34 Barras IEEE")
    # root.msg["font"] = ("Verdana", "10", "italic", "bold")

    root.title('Sistema 34 Barras IEEE')
    root.geometry('1050x550')

    root.state('zoomed')


    # Label(root, image=root.python_image).pack
    # root.grid(row=0, column=0, sticky=EW)
    C = Canvas(root, bg="white", height=750, width=1340, scrollregion=(0,0,1000,1000))
    # C.create_window((2000,5000))
    # C.pack(expand=True, fill=BOTH)
    C.grid(row=0, column=0, sticky=EW)

    C.python_image = PhotoImage(file='sistema_34_barras1.png')
    C.create_image(470, -5, image=C.python_image, anchor=NW)  

    scrollbar = Scrollbar(root,orient='vertical',command= C.yview)
    scrollbar.grid(row=0, column=1, sticky=NS)
    C['yscrollcommand'] = scrollbar.set

    # med_tensao =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # med_corrente= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    C.count_medidor_tensao=0;
    C.count_medidor_corrente=0;

    C.med_tensao = med_tensao
    C.med_corrente = med_corrente
    C.ERRO = ERRO

    root.bind('c', functools.partial(mostrar_num_corrente, C=C));
    root.bind('C', functools.partial(mostrar_num_corrente, C=C));
    root.bind('t', functools.partial(mostrar_num_tensao, C=C));
    root.bind('T', functools.partial(mostrar_num_tensao, C=C));
    medidor(C,573,8,'v')    #800

    medidor(C,573,49,'v')   #802
    medidor(C,573,90,'v')   #806
    # C.create_rectangle(vet_x0[1]-30,vet_y0[1]-15,vet_x0[1]+35,vet_y0[1]+25,fill='black',outline='gray')

    medidor(C,573,132,'v')  #808
    medidor(C,484,161,'h')  #810 -> Sozinho
    medidor(C,573,172,'v')  #812
    medidor(C,573,213,'v')  #814
    medidor(C,573,269,'v')  #850
    medidor(C,573,310,'v')  #816

    medidor(C,660,283,'h')  #818
    medidor(C,706,283,'h')  #820
    medidor(C,752,283,'h')  #822

    medidor(C,573,352,'v')  #824 
    medidor(C,484,380,'h')  #826 -> Sozinho
    medidor(C,573,392,'v')  #828
    medidor(C,573,434,'v')  #830
    medidor(C,573,475,'v')  #854
    medidor(C,573,516,'v')  #852

    medidor(C,573,578,'v')  #832


    medidor(C,654,589,'h')  #858
    medidor(C,700,589,'h')  #834
    medidor(C,746,589,'h')  #842
    medidor(C,792,589,'h')  #844
    medidor(C,838,589,'h')  #846
    medidor(C,885,589,'h')  #848


    medidor(C,723,522,'v')  #860
    medidor(C,723,481,'v')  #836
    medidor(C,803,451,'h')  #840 -> Sozinho
    medidor(C,723,440,'v')  #862
    medidor(C,723,399,'v')  #838
    medidor(C,677,650,'v')  #864
    medidor(C,538,635,'v')  #888
    medidor(C,538,676,'v')  #890
    medidor(C,486,504,'h')  #856 -> Sozinho

    C.count_medidor_tensao=0;
    # vetore = np.zeros((34,2))
    # vetore[:,0] = vet_x0
    # vetore[:,1] = vet_y0
    # np.save('vets_x0y0', vetore)
    ## medidores de corrente
    medidor_corrente(C,573,8,'b')    #800 a 802
    medidor_corrente(C,573,49,'c')   #802 a 800
    medidor_corrente(C,573,49,'b')   #802 a 806
    medidor_corrente(C,573,90,'c')   #806 a 802
    medidor_corrente(C,573,90,'b')   #806 a 808
    medidor_corrente(C,573,132,'c')  #808 a 806
    medidor_corrente(C,551,128,'b')  #808 a 810 -> So corrente
    medidor_corrente(C,573,132,'b')  #808 a 812
    medidor_corrente(C,484,161,'d')  #810 a 808 -> Sozinho
    medidor_corrente(C,573,172,'c')  #812 a 808
    medidor_corrente(C,573,172,'b')  #812 a 814
    medidor_corrente(C,573,213,'c')  #814 a 812
    medidor_corrente(C,573,213,'b')  #814 a 850
    medidor_corrente(C,573,269,'c')  #850 a 814
    medidor_corrente(C,573,269,'b')  #850 a 816
    medidor_corrente(C,573,310,'c')  #816 a 850
    medidor_corrente(C,593,314,'c')  #816 a 818 -> So corrente
    medidor_corrente(C,573,310,'b')  #816 a 824

    medidor_corrente(C,660,283,'e')  #818 a 816
    medidor_corrente(C,660,283,'d')  #818 a 820
    medidor_corrente(C,706,283,'e')  #820 a 818
    medidor_corrente(C,706,283,'d')  #820 a 822
    medidor_corrente(C,752,283,'e')  #822 a 820

    medidor_corrente(C,573,352,'c')  #824 a 816
    medidor_corrente(C,550,348,'b') #824 a 826-> So corrente
    medidor_corrente(C,573,352,'b')  #824 a 828
    medidor_corrente(C,484,380,'d')  #826 a 824 -> Sozinho
    medidor_corrente(C,573,392,'c')  #828 a 824      
    medidor_corrente(C,573,392,'b')  #828 a 830
    medidor_corrente(C,573,434,'c')  #830 a 828
    medidor_corrente(C,573,434,'b')  #830 a 854
    medidor_corrente(C,573,475,'c')  #854 a 830
    medidor_corrente(C,573,475,'b')  #854 a 852
    medidor_corrente(C,552,471,'b') #854 a 856 -> So corrente
    medidor_corrente(C,573,516,'c')  #852 a 854
    medidor_corrente(C,573,516,'b')  #852 a 832

    medidor_corrente(C,573,578,'c')  #832 a 852
    medidor_corrente(C,600,574,'b') #832 a 858 -> So corrente
    medidor_corrente(C,547,574,'b') #832 a 888-> So corrente


    medidor_corrente(C,654,589,'e')  #858 a 832
    medidor_corrente(C,654,589,'d')  #858 a 834
    medidor_corrente(C,650,603,'d') #858 a 864 ->Só corrente

    medidor_corrente(C,700,589,'e')  #834 a 858
    medidor_corrente(C,700,589,'d')  #834 a 842
    medidor_corrente(C,696,572,'d')  #834 a 860-> Só corrente
    medidor_corrente(C,746,589,'e')  #842 a 834
    medidor_corrente(C,746,589,'d')  #842 a 844
    medidor_corrente(C,792,589,'e')  #844 a 842
    medidor_corrente(C,792,589,'d')  #844 a 846
    medidor_corrente(C,838,589,'e')  #846 a 844
    medidor_corrente(C,838,589,'d')  #846 a 848
    medidor_corrente(C,885,589,'e')  #848 a 846

    medidor_corrente(C,723,522,'b')  #860 a 834
    medidor_corrente(C,723,522,'c')  #860 a 836
    medidor_corrente(C,723,481,'b')  #836 a 860
    medidor_corrente(C,740,486,'c')  #836 a 840 -> So corrente
    medidor_corrente(C,723,481,'c')  #836 a 862
    medidor_corrente(C,803,451,'e')  #840 a 836 -> Sozinho
    medidor_corrente(C,723,440,'b')  #862 a 836
    medidor_corrente(C,723,440,'c')  #862 a 838
    medidor_corrente(C,723,399,'b')  #838 a 862
    medidor_corrente(C,677,650,'c')  #864 a 858
    medidor_corrente(C,538,635,'c')  #888 a 832
    medidor_corrente(C,538,635,'b')  #888 a 890
    medidor_corrente(C,538,676,'c')  #890 a 888
    medidor_corrente(C,486,504,'d')  #856 a 854 -> Sozinho
    # reset_button(root,C)

    root.mainloop() 

        # root.grid_columnconfigure(0, weight=1)
        # root.grid_rowconfigure(0, weight=1)
        # scrollbar.grid(row=0, column=1, sticky=tk.NS)




        # C.create_image(500, 500, anchor=NE, image='sistema.png')
        # img = PhotoImage(file='image.png') #transparent image
        # C.create_image(0,0,image=img,anchor='ne') 


#         # scrollbar = ttk.Scrollbar(container,orient='vertical',
#         # command=widget1.yview) greet= "Hello " + name.get()


# def desenhar_sistema_34_barras():
#     C = Canvas(App, bg="white", width=720, height=720)
#     medidor(C,355,100,'h')
#     # C.create_image(500, 500, anchor=NE, image='sistema.png')


    
# desenhar_sistema_34_barras()
# if __name__ == "__main__":
#     app = App()
#     app.mainloop() 