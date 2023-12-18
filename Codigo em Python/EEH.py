
import numpy as np
import copy
import interface_resultados as interface

def EEH( med_tensao,   med_corrente):

    # matrizes_conf = np.array([
    #     [1.3368+1.3343j,   0.2101+0.5779j,   0.2130+0.5015j],
    #     [0.2101+0.5779j,   1.3238+1.3569j,   0.2066+0.4591j],
    #     [0.2130+0.5015j,   0.2066+0.4591j,   1.3294+1.3471j],
        
    #     [1.9300+1.4115j,   0.2327+0.6442j,   0.2359+0.5691j],
    #     [0.2327+0.6442j,   1.9157+1.4281j,   0.2288+0.5238j],
    #     [0.2359+0.5691j,   0.2288+0.5238j,   1.9219+1.4209j],

    #     [2.7995+1.4855j,   0.0000+0.0000j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j],

    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   2.7995+1.4855j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j],

    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   1.9217+1.4212j,   0.0000+0.0000j],
    #     [0.0000+0.0000j,   0.0000+0.0000j,   0.0000+0.0000j]
    # ])
    
        #num_barra_dobrado = np.array([32,34,64,66,96,102,192,198])
    #     todos_32 = np.array([
    #     [2580,		300,		1,		2],
    #     [1730,		300,		2,		3],
    #     [32230,		300,		3,		4],
    #     [5804,		303,		4,		5],
    #     [37500,		300,		4,		6],
    #     [29730,		300,		6,		7],
    #     [10,  		301,		7,		8],
    #     [310,     	301,		8,		9],
    #     [1710,		302,		9,		10],
    #     [10210,		301,		9,		13],
    #     [48150,		302,		10,		11],
    #     [13740,		302,		11,		12],
    #     [3030,		303,		13,		14],
    #     [28,          301,		13,		15],
    #     [20440,		301,		15,		16],
    #     [520,  	    301,		16,		17],
    #     [3616,		301,		17,		18],
    #     [23330,		303,		17,		34],
    #     [10,      	301,		18,		19],
    #     [4900,		301,		19,		20],
    #     [516,     	301,		20,		21],
    #     [1620,		302,		20,		31],
    #     [280,     	301,		21,		22],
    #     [2020,		301,		21,		26],
    #     [1350,		301,		22,		23],
    #     [3640,		301,		23,		24],
    #     [530,         301,		24,		25],
    #     [2680,		301,		26,		27],
    #     [26,      	301,		27,		28],
    #     [280,         301,		27,		29],
    #     [426,         304,		29,		30],
    #     [10560,		300,		23,		33]
    # ])

    # todos_dobrados = np.array([
    # [2580,		300,		1,		2],
    # [2580,		300,		2,		1],
    # [1730,		300,		2,		3],
    # [1730,		300,		3,		2],
    # [32230,		300,		3,		4],	
    # [32230,		300,		4,		3],
    # [5804,		303,		4,		5],
    # [37500,		300,		4,		6],
    # [5804,		303,		5,		4],
    # [37500,		300,		6,		4],
    # [29730,		300,		6,		7],
    # [29730,		300,		7,		6],
    # [10,	    	301,		7,		8],
    # [10,		    301,		8,		7],
    # [310,		    301,		8,		9],
    # [310,		    301,		9,		8],
    # [1710,		302,		9,		10],
    # [10210,		301,		9,		13],
    # [1710,		302,		10,		9],
    # [48150,		302,		10,		11],
    # [48150,		302,		11,		10],
    # [13740,		302,		11,		12],
    # [13740,		302,		12,		11],
    # [10210,		301,		13,		9],
    # [3030,		303,		13,		14],
    # [28,		    301,		13,		15],
    # [3030,		303,		14,		13],
    # [28,	    	301,		15,		13],
    # [20440,		301,		15,		16],
    # [20440,		301,		16,		15],
    # [520,		    301,		16,		17],
    # [520,		    301,		17,		16],
    # [3616,		301,        17,		18],
    # [23330,		303,		17,		34],
    # [3616,		301,		18,		17],
    # [10,		    301,		18,		19],
    # [10,	    	301,		19,		18],
    # [4900,		301,		19,		20],
    # [4900,		301,		20,		19],
    # [516,		    301,		20,		21],
    # [1620,		302,		20,		31],
    # [516,	    	301,		21,		20],
    # [280,		    301,		21,		22],
    # [2020,   		301,		21,		26],
    # [280,		    301,		22,		21],
    # [1350,		301,		22,		23],
    # [1350,		301,		23,		22],
    # [3640,		301,		23,		24],
    # [3640,		301,		24,		23],
    # [530,		    301,		24,		25],
    # [530,	    	301,		25,		24],
    # [2020,		301,		26, 	21],
    # [2680,		301,		26,		27],
    # [2680,		301,		27,		26],
    # [26,		    301,		27,		28],
    # [280,		    301,		27,		29],
    # [26,		    301,		28,		27],
    # [280,		    301,		29,		27],
    # [426,		    304,		29,		30],
    # [426,		    304,		30,		29],
    # [1620,		302,		31,		20],
    # [10560,		300,		32,		33],
    # [10560,		300,		33,		32],
    # [23330,		303, 	    34,		17]
    # ])

    # tipo_conf = np.array([300,301,302,303,304])
    # fundamental = np.array([
    # [800,1.0000,-0.0000,1.0000,-119.9999,1.0000,119.9999],
    # [802,0.9996,-0.0090,0.9994,-120.0061,0.9994,119.9841],
    # [806,0.9993,-0.0149,0.9990,-120.0102,0.9990,119.9736],
    # [808,0.9938,-0.1171,0.9917,-120.0785,0.9916,119.7826],
    # [810,0.9938,-0.1171,0.9917,-120.0788,0.9916,119.7826],
    # [812,0.9872,-0.2141,0.9830,-120.1347,0.9827,119.5770],
    # [814,0.9816,-0.2766,0.9758,-120.1644,0.9754,119.4224],
    # [850,0.9759,-0.9831,0.9702,-120.8463,0.9693,118.6958],
    # [816,0.9758,-0.9831,0.9701,-120.8460,0.9692,118.6947],
    # [818,0.9759,-0.9858,0.9701,-120.8460,0.9692,118.6947],
    # [820,0.9763,-1.0300,0.9701,-120.8460,0.9692,118.6947],
    # [822,0.9763,-1.0323,0.9701,-120.8460,0.9692,118.6947],
    # [824,0.9731,-0.9737,0.9668,-120.8329,0.9658,118.6579],
    # [826,0.9731,-0.9737,0.9668,-120.8329,0.9658,118.6579],
    # [828,0.9728,-0.9728,0.9665,-120.8316,0.9656,118.6549],
    # [830,0.9672,-0.9458,0.9598,-120.7966,0.9587,118.5865],
    # [854,0.9670,-0.9452,0.9597,-120.7957,0.9586,118.5855],
    # [852,0.9580,-0.8826,0.9483,-120.7033,0.9475,118.5250],
    # [832,0.9511,-1.5263,0.9416,-121.3572,0.9408,117.8761],
    # [858,0.9505,-1.5187,0.9408,-121.3454,0.9399,117.8754],
    # [834,0.9496,-1.5087,0.9397,-121.3305,0.9389,117.8750],
    # [842,0.9496,-1.5082,0.9397,-121.3299,0.9388,117.8750],
    # [844,0.9494,-1.5060,0.9395,-121.3267,0.9386,117.8751],
    # [846,0.9494,-1.5054,0.9394,-121.3256,0.9385,117.8751],
    # [848,0.9494,-1.5052,0.9394,-121.3254,0.9385,117.8751],
    # [860,0.9496,-1.5082,0.9397,-121.3299,0.9388,117.8749],
    # [836,0.9496,-1.5082,0.9397,-121.3299,0.9388,117.8748],
    # [840,0.9496,-1.5081,0.9397,-121.3298,0.9388,117.8748],
    # [862,0.9496,-1.5082,0.9397,-121.3299,0.9388,117.8748],
    # [838,0.9496,-1.5082,0.9397,-121.3301,0.9388,117.8748],
    # [864,0.9505,-1.5187,0.9408,-121.3454,0.9399,117.8754],
    # [888,0.9485,-1.8247,0.9391,-121.6607,0.9383,117.5769],
    # [890,0.9181,-2.0482,0.8990,-121.8001,0.9001,116.7424],
    # [856,0.9670,-0.9452,0.9597,-120.8004,0.9586,118.5855]
    # ])

    #  salva a matriz em um arquivo
    # np.save('fundamental', fundamental)
    
    #Carregar os arquivos com as matrizes
    matrizes_conf = np.load('matrizes_conf.npy')
    num_barra_dobrado = np.load('num_barra_dobrado.npy')
    todos_32 = np.load('todos_32.npy')
    todos_dobrados = np.load('todos_dobrados.npy')
    tipo_conf = np.load('tipo_conf.npy')
    fundamental = np.load('fundamental.npy')
    

    ## Cálculo da Matriz Admitância
    z_base = (24900**(2))/2500000

    ## Dados

    # Frequência
    frequencia = 60;

    [nl,nc] =np.shape(matrizes_conf)
    
    z_total = nl/3 #nº de linhas das matrizes de configuração das impedancias / 3 para a quantidade de tipos de conf.
    # Distâncias de cada uma das 32 linhas
    #generalizar
    distancia_ft = todos_32[:,0]
    # Distâncias de cada uma das "32 linhas" (dobrado para correntes)
    #generalizar
    distancia_ft_linha = todos_dobrados[:,0]
    # tipo de cada uma das 32 linhas
    tipo = todos_32[:,1]
    # tipo de cada uma das "32 linhas" (dobrado para correntes)
    #generalizar
    tipo_linha = todos_dobrados[:,1]

    distancia_miles = distancia_ft*0.000190 
    distancia_miles =np.around(distancia_miles,13) ##arredondar para ficar igual ao do matlab

    distancia_miles_linha =distancia_ft_linha*0.000190 
    distancia_miles_linha =np.around(distancia_miles_linha,13)##arredondar para ficar igual ao do matlab 

    #generalizar todos os seguintes comandos abaixo
    #generalizar os números apenas, os comandos são necessários
    
    Zfinal = calcular_Zfinal(num_barra_dobrado[0], tipo, tipo_conf,matrizes_conf,distancia_miles,z_base)
    Zfinal_linha = calcular_Zfinal(num_barra_dobrado[2], tipo_linha, tipo_conf,matrizes_conf,distancia_miles_linha,z_base)


    # Impedância das linhas
    #generalizar
    #mudar o 96 e 192 (generalizar p todos os arquivos) ? aqui deu errado,
    #voltar dps
    impedancias = np.zeros((96,5), dtype=np.cdouble);

    impedancias_linha = np.zeros((192,5),dtype=np.cdouble);

    

    linhas = todos_32[:,2:4]
    #generalizar
    linhas_linha = todos_dobrados [:,2:4]

    #generalizar todos os comandos abaixo (32 e 64)
    impedancias= mover_valores_de_linha(num_barra_dobrado[0],impedancias,linhas)

    impedancias_linha = mover_valores_de_linha(num_barra_dobrado[2],impedancias_linha,linhas_linha)	
    impedancias[:,2:5] = Zfinal; # matriz conexão + matriz matriz impedância das linhas


    

    impedancias_linha[:,2:5] = Zfinal_linha; # matriz conexão + matriz matriz impedância das linhas

    for ii in range(0,num_barra_dobrado[2]):
        #1:64
        if impedancias_linha[3*ii,0] > impedancias_linha[3*ii,1]:
            impedancias_linha[3*ii:3*ii+3,2:5] = -impedancias_linha[3*ii:3*ii+3,2:5]

    # Matriz impedância
    #generalizar os comandos abaixo (102, 32)
    z = np.zeros((num_barra_dobrado [5], num_barra_dobrado[5]),dtype=np.cdouble);
    # zeros(102,102);
    ########## DEBUGADO ATE AQUI MAIS OU MENOS ############
    for k in range(0,num_barra_dobrado[0]):
        #0:32
        l = impedancias[3*k,0];#sprimeiro termo de cada matriz 3x3
        j = impedancias[3*k,1];#segundo termo de cada matriz 3x3
        #-1 se deve a diferença do python e do matlab
        l = int(l)-1;j = int(j)-1
        z[3*l:3*l+3,3*j:3*j+3] = impedancias[3*k:3*k+3,2:5];
        z[3*j:3*j+3,3*l:3*l+3] = z[3*l:3*l+3,3*j:3*j+3];
    

        # Matriz impedância de linha
        #generalizar os comandos abaixo
    z_linha = np.zeros((num_barra_dobrado [6], num_barra_dobrado [5]),dtype=np.cdouble);
        #zeros(192,102);
    for k in range(0,num_barra_dobrado[2]):
        #0:32
        l = impedancias_linha[3*k,0];#primeiro termo de cada matriz 3x3
        j = impedancias_linha[3*k,1];#segundo termo de cada matriz 3x3
        #-1 se deve a diferença do python e do matlab
        l = int(l)-1;j = int(j)-1
        z_linha[3*k:3*k+3,3*l:3*l+3] = impedancias_linha[3*k:3*k+3,2:5];
        z_linha[3*k:3*k+3,3*j:3*j+3] = -z_linha[3*k:3*k+3,3*l:3*l+3];

    # Matriz admitância
    #generalizar os comandos (102, 34)
    y = np.zeros((num_barra_dobrado[5], num_barra_dobrado[5]), dtype=np.cdouble);
    #zeros(102,102);

    for e in range(0,num_barra_dobrado[5]):
    #1:102
        for f in  range(0,num_barra_dobrado[5]):
            #1:102
            if (z[e,f]== 0):
                y[e,f]= 0;
            else:
                y[e,f] = (-1)/(z[e,f]);
    
    for g in range(0,num_barra_dobrado[1]):
    #1:34
        y[3*g:3*g+3,3*g:3*g+3]=0;
        for h in range(0,13):
            if (h != g):
                y[3*g:3*g+3,3*g:3*g+3]=y[3*g:3*g+3,3*g:3*g+3]+y[3*g:3*g+3,3*h:3*h+3]; #ajustando o valor da diagonal

    # Matriz admitância de linha
    #generalizar os comandos abaixo (198, 102) 198? 
    y_linha = np.zeros((num_barra_dobrado [7], num_barra_dobrado [5]),dtype=np.cdouble);
    #zeros(198,102);
    for ee in range(0,num_barra_dobrado[6]):
    #1:192
        for ff in range(0,num_barra_dobrado[5]):
    #1:102
            if z_linha[ee,ff]== 0:
                y_linha[ee,ff]= 0;
            else:
                y_linha[ee,ff] = -1/(z_linha[ee,ff]);
    

    # Modelagem do transformador trifásico (dps)
    y[54:57,54:57]= y[54:57,54:57] + (1/(0.019+0.048j))*np.eye(3); 
    y[54:57,93:96]= y[54:57,93:96] + (-1/(0.019+0.048j))*np.eye(3);
    y[93:96,54:57]= y[93:96,54:57] + (-1/(0.019+0.048j))*np.eye(3);
    y[93:96,93:96]= y[93:96,93:96] + (1/(0.019+0.048j))*np.eye(3);  
        
    # y(55:57,55:57)= y(55:57,55:57) + (1/(0.019+0.048i))*eye(3); 
    # y(55:57,94:96)= y(55:57,94:96) + (-1/(0.019+0.048i))*eye(3);
    # y(94:96,55:57)= y(94:96,55:57) + (-1/(0.019+0.048i))*eye(3);
    # y(94:96,94:96)= y(94:96,94:96) + (1/(0.019+0.048i))*eye(3);  

    y_linha_2 = np.zeros((198,102), dtype=complex);
    y_linha_2[0:114,:] = y_linha[0:114,:];
    y_linha_2[114:117,54:57] = y[54:57,93:96];
    y_linha_2[114:117,93:96] = -y[54:57,93:96];
    y_linha_2[117:186,:] = y_linha[114:183,:];
    y_linha_2[186:189,93:96] = -y[54:57,93:96];
    y_linha_2[186:189,54:57] = y[54:57,93:96];
    y_linha_2[189:198,:] = y_linha[183:192,:];

    # Cálculo das Injeções de Corrente em cada Barra
    # generalizar o 34  
    pi = np.pi

    fundamental= np.concatenate( (fundamental, np.zeros((34,3),dtype=np.double)),axis=1)
    for b in range(0,num_barra_dobrado[1]):
        #1:34
        fundamental[b,7] = fundamental[b,2]*pi/180; #convertendo para radianos
        fundamental[b,8] = fundamental[b,4]*pi/180;
        fundamental[b,9] = fundamental[b,6]*pi/180;
    


    tensoes2 = fundamental;
    tensoes3 = np.zeros((102,1),dtype=np.cdouble);
    fundamental = copy.copy(fundamental)
    for s in range(0,num_barra_dobrado[1]):
    #1:34 % convertendo tensoes trifasicas de cada uma das 34 barras para valores complexos (3 linhas do vetor tensoes3)
        
        [x,q]= pol2cart(fundamental[s,7],fundamental[s,1]);
        tensoes2[s,1:3]=[x,q];
        tensoes3[3*s,0] = complex(tensoes2[s,1],tensoes2[s,2]);
        # print(type(fundamental[0,0]))
        [x,q]= pol2cart(fundamental[s,8],fundamental[s,3]);
        tensoes2[s,3:5]=[x,q];
        tensoes3[3*s+1,0] = complex(tensoes2[s,3],tensoes2[s,4]);
        

        [x,q]= pol2cart(fundamental[s,9],fundamental[s,5]);
        tensoes2[s,5:7]=[x,q];
        tensoes3[3*s+2,0] = complex(tensoes2[s,5],tensoes2[s,6]);
    
    # print(pol2cart(-0.0165,np.pi))
    # print(pol2cart(5,37*3.14/180))
    # print(cart2pol(-0.0165,0.9670))

    # print(pol2cart(5,37*np.pi/180)

    #generalizar o 102
    II = np.zeros((num_barra_dobrado [5],1),dtype=np.cdouble); #o número 1?
        #zeros (102,1);    
    II = np.matmul(y,tensoes3); # injeção = matriz admitância x vetor de tensão

    II2 = np.zeros((num_barra_dobrado [5],2)); 

    II3 = np.zeros((num_barra_dobrado [5],2)); 
    for h in range(0,num_barra_dobrado[5]):
        #1:102 % convertendo as correntes complexas para valores de amplitude e fase
        II2[h,0]=II[h,0].real;
        II2[h,1]=II[h,0].imag; 
    for o in range(0,num_barra_dobrado[5]):
        #1:102
        [xx,qq]= cart2pol(II2[o,0],II2[o,1]);
        II3[o,0:2]=[xx,qq];
    
    II3= np.c_[ II3, np.zeros((num_barra_dobrado [5],1)) ]
    for t in range(0,num_barra_dobrado[5]):
    #1:102
        II3[t,2] = II3[t,0]*180/np.pi;
    # print(y.shape, II2.shape, II.shape)
    # Cálculo das correntes de linha = matriz admitância de linha x vetor de tensão
    # II_linha = np.empty((198,1),dtype=np.cdouble)
    II_linha = np.matmul(y_linha_2, tensoes3)

    # for i in range(0,198):
    #     result = 0
    #     for j in range(0,102):
    #         result += y_linha_2[i,j]*tensoes3[j,0]
    #         # if( i ==169 and j == 101):

    #     II_linha[i,0] = result
    II_linha = np.around(II_linha,10)

    II2_linha = np.zeros((198,2),dtype=np.double);
    for hh in range(0,198): # convertendo as correntes complexas para valores de amplitude e fase
        II2_linha[hh,0]= np.real(II_linha[hh,0]);
        II2_linha[hh,1]= np.imag(II_linha[hh,0]);

    II3_linha = np.zeros((198,2),dtype=np.double);
    for oo in range(0,198):
        [xxx,qqq]= cart2pol(II2_linha[oo,0],II2_linha[oo,1]);
        II3_linha[oo,0:2]=[xxx,qqq];

    II3_linha= np.c_[(II3_linha, np.zeros((198,1),dtype=np.double))]
    for tt in range(0,198):
        II3_linha[tt,2] = II3_linha[tt,0]*180/np.pi;

    # Resposta esperada (primeiro todas as amplitude, depois todas as fases de
    # cada barra)
    #generalizar o tipo de resposta
    resposta_esperada = np.zeros((204,1),dtype=np.double);
    for barra in range(0,34): #?
        resposta_esperada[3*barra:3*barra+3,0] = [tensoes2[barra, 1], tensoes2[barra, 3], tensoes2[barra, 5]];
        resposta_esperada [3*barra+102:3*barra+3+102,0] = [tensoes2[barra, 2], tensoes2[barra, 4], tensoes2[barra, 6]];
    



    ## ALGORITMO AUTOMATIZADO ##
    ##Debug##
    # med_tensao =[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # med_corrente= [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # # #########
   

    n_med_tensao = np.sum(med_tensao);
    n_med_corrente = np.sum(med_corrente);
    n_sist = np.prod(np.shape(med_tensao));
    n_sist_corrente = np.prod(np.shape(med_corrente));
 
    m = 0;
    n = 0;

    # print((n_med_corrente))
    #generalizar os números apenas, os comandos são necessários 
    ordem_1 = np.zeros((int(n_sist-n_med_tensao),1),dtype=int);
    ordem_2 = np.zeros((n_med_tensao,1),dtype=int);
    # print (ordem_1.shape, ordem_2.shape)
   
    if n_med_tensao ==num_barra_dobrado[1]:
        ordem =range(0,num_barra_dobrado[1],1);
    
    if n_med_tensao== 0:
        ordem = np.zeros(num_barra_dobrado[1]);
    else:
        for k in range(0,n_sist):    
            if (med_tensao[k] == 0):
                ordem_1[m] = k;
                m = m+1;
            else:
                ordem_2[n] = k;	
                n = n+1;
        ordem = np.concatenate((ordem_2,ordem_1),axis=0);
    mm = 0;
    nn = 0;

    ordem_corrente_1 = np.zeros((n_sist_corrente-n_med_corrente,1),dtype=int);
    ordem_corrente_2 = np.zeros((n_med_corrente,1),dtype=int);
    # print(ordem_corrente_1.shape, ordem_corrente_2.shape)
    if n_med_corrente == num_barra_dobrado[2]:
        ordem_corrente =range[0:num_barra_dobrado[2],1];
    if n_med_corrente ==0:
        ordem_corrente = np.zeros(num_barra_dobrado[2]);
    else:
        for kk in range(0,n_sist_corrente):
            if med_corrente[kk] == 0:
                ordem_corrente_1[mm] = kk;
                mm = mm+1;
            else:
                ordem_corrente_2[nn] = kk;
                nn = nn+1;
        ordem_corrente =np.concatenate((ordem_corrente_2,ordem_corrente_1),axis=0);

    k = 0;
    
    y_linha_medida = np.zeros((0,102),dtype=complex);
    for j in range(0,n_sist_corrente):
        if (med_corrente[j] == 1):
            #Codigo necessario para ir criando o vetor y_linha_medida conforme for necessário.
            y_linha_medida = np.concatenate((y_linha_medida,np.zeros((3,102),dtype=complex)),axis=0)
            y_linha_medida[3*k:3*k+3,:] = y_linha_2[3*j:3*j+3,:];
            k = k+1;

    hr = np.zeros((3*(n_med_tensao+n_med_corrente),3*n_sist),dtype=np.double);

#############################################################,<-Virgula sem saber oq faz
    hr[0:3*n_med_tensao,0:3*n_sist] = np.concatenate((np.eye(3*n_med_tensao),np.zeros((3*n_med_tensao,3*(n_sist-n_med_tensao)))),axis=1);
    for oi in range(0,n_med_corrente):
        hr[3*n_med_tensao+(3*oi):3*n_med_tensao+(3*oi+3),:] = np.real(y_linha_medida[(3*oi):(3*oi+3),:]);

    hr_2 = np.zeros((3*(n_med_tensao+n_med_corrente),3*n_sist),dtype=np.double);
    # ("%d\n",range(3*n_med_tensao+1,3*(n_med_tensao+n_med_corrente)))
    hr_2[0:3*n_med_tensao,:] = hr[0:3*n_med_tensao,:]; 
    for r in range(0,n_sist):
        hr_2[3*n_med_tensao:3*(n_med_tensao+n_med_corrente),3*r:3*r+3] = hr[3*n_med_tensao:3*(n_med_tensao+n_med_corrente),3*ordem[r,0]:3*ordem[r,0]+3];
    

    hi = np.zeros((3*(n_med_tensao+n_med_corrente),3*n_sist));
   
    for io in range(0,n_med_corrente):
        hi[3*n_med_tensao+(3*io):3*n_med_tensao+(3*io+3),:] = np.imag(y_linha_medida[(3*io):(3*io+3),:]);
    

    hi_2 = np.zeros((3*(n_med_tensao+n_med_corrente),3*n_sist));
    
    # hr_2 = np.around(hr_2,8)

    for r in range(0,n_sist):
        hi_2[:,3*r:3*r+3] = hi[:,3*ordem[r,0]:3*ordem[r,0]+3];
    # hi_2 = np.around(hi_2,8)

    H = np.concatenate( (hr_2,(-hi_2)), axis=1)
    aux = np.concatenate( (hi_2,hr_2), axis=1)
    H = np.concatenate( (H,aux), axis=0)
    # print(H[96:100,81:84])
    # VALor =  np.array([[121.8563,179.0473,224.3705],
    #            [179.0473,121.1199,252.7915],
    #            [224.3705,252.7915,121.4421],
    #            [121.8563,179.0473,224.3705]])
    # u,s,v = np.linalg.svd(H[96:100,81:84], full_matrices=True)    
    # u[:,1] = u[:,1]*-1 
    # print('U:',v)
    # Solução por SVD
    H = np.around(H,10)
    U,S,V =  np.linalg.svd(H,full_matrices=False);
    V = V.T
    # U[:,1] = U[:,1]*-1 
    # print('Documentação: ',np.allclose(H, np.dot(U[:, :204] * S, V))) # repeti o que estava na documentação/ retornou True
    S= np.diag(S)

    [nl,nc] = U.shape
    [nl2,nc2] = S.shape
    S = np.concatenate((S,np.zeros((nc2-nl2,nc))),axis=0) #Concatenando a matriz S para conseguir o shape necessario de [288,204], com 0 nas diagonais excedentes.
    # V = Zerar_Se(V,1e-8);
    # U = Zerar_Se(U,1e-8);
    # S = Zerar_Se(S,1e-8);

    U = U.T  

    vetor_medidas = np.zeros((2*3*(n_med_tensao+n_med_corrente),1));
    for iii in range(0,n_med_tensao):
        vetor_medidas[3*iii] = tensoes2[ordem[iii],1];
        vetor_medidas[3*iii+1] = tensoes2[ordem[iii],3];
        vetor_medidas[3*iii+2] = tensoes2[ordem[iii],5];

    for ioo in range(0,n_med_corrente):
        vetor_medidas[3*n_med_tensao + 3*ioo] = II2_linha[3*ordem_corrente[ioo],0];
        vetor_medidas[3*n_med_tensao + 3*ioo+1] = II2_linha[3*ordem_corrente[ioo]+1,0];
        vetor_medidas[3*n_med_tensao + 3*ioo+2] = II2_linha[3*ordem_corrente[ioo]+2,0];
    
    for ioi in range(0,n_med_tensao):
        vetor_medidas[3*(n_med_tensao + n_med_corrente) + 3*ioi] = tensoes2[ordem[ioi],2];
        vetor_medidas[3*(n_med_tensao + n_med_corrente) + 3*ioi+1] = tensoes2[ordem[ioi],4];
        vetor_medidas[3*(n_med_tensao + n_med_corrente) + 3*ioi+2] = tensoes2[ordem[ioi],6];
    
    for iio in range(0,n_med_corrente):
        vetor_medidas[3*(2*n_med_tensao + n_med_corrente) + 3*iio] = II2_linha[3*ordem_corrente[iio],1];
        vetor_medidas[3*(2*n_med_tensao + n_med_corrente) + 3*iio+1] = II2_linha[3*ordem_corrente[iio]+1,1];
        vetor_medidas[3*(2*n_med_tensao + n_med_corrente) + 3*iio+2] = II2_linha[3*ordem_corrente[iio]+2,1];

    # resposta = V * pinv(S'*S)* S' * U' * vetor_medidas;  
  
    
    # resposta = V @ np.linalg.pinv(S) @ U.T @ vetor_medidas;
    mult1 = np.matmul(V,np.linalg.pinv(S))


    # print(mult1.shape, (U).shape)
    mult2 = np.matmul(mult1,U)
    resposta = np.matmul(mult2, vetor_medidas);



    resposta = Zerar_Se(resposta,1e-8);


    ordem_vetor_medidas = np.zeros((n_sist),dtype=int);
    for kkk in range(0,n_sist):
        for k in range(0,n_sist):
            if (ordem[k] == kkk):
                ordem_vetor_medidas[kkk] = k;
    # compare_matrix(ordem_vetor_medidas,0.005)
    resposta_organizada = np.zeros((2*3*n_sist,1),dtype=np.double); 
    for rr in range(0,n_sist):
        resposta_organizada[3*rr:3*rr+3] = resposta[3*ordem_vetor_medidas[rr]:3*ordem_vetor_medidas[rr]+3]; 
        resposta_organizada[3*rr+3*n_sist:3*rr+3+3*n_sist] = resposta[3*ordem_vetor_medidas[rr] + 3*n_sist : 3*ordem_vetor_medidas[rr]+3+3*n_sist];

    
    ERRO = resposta_organizada - resposta_esperada;
    #Transformando o SVD EM Objeto para poder ser utilizado depois
    class SVD:
        def __init__(self, U, S, V):
            self.U = U
            self.S = S
            self.V = V
    valores_singulares = SVD(U,S,V)

    # S= np.diag(S)
    # S = np.concatenate((S,np.zeros((84,204))),axis=0) #Concatenando a matriz S para conseguir o shape necessario de [288,204], com 0 nas diagonais excedentes.
    ERRO = Zerar_Se(ERRO,1e-8)
    # for  i in range(0,204):
    #     print('%f' % (ERRO[i]**5))
    print(ERRO)
    interface.interface_resultados(med_tensao, med_corrente,ERRO)
    return ERRO, valores_singulares, n_med_tensao

#---------------------------------------------
#FUNÇÃO DE DEBUG
def compare_matrix(matrix_1,erro):  
    ##Ferramentas necessarias 
    f = open("..\Codigo antigo em MatLab\AG_34\myFile.txt", "r")
    matriz_= f.read()
    matriz_ = matriz_.replace('i','j')
    matriz_ = np.matrix(matriz_)
    f.close()
    [nl,nc] = np.shape(matrix_1)    
    matrix_1 = (matrix_1).reshape(1,nl*nc)
   
    for i in range(0,nl*nc):
        if(matrix_1[0,i] <0): matrix_1[0,i] = abs(matrix_1[0,i])
        if(matriz_[0,i] <0): matriz_[0,i] = abs(matriz_[0,i]) 
        variacao_min =  (matriz_[0,i] - (matriz_[0,i]*erro))
        variacao_max = (matriz_[0,i] + (matriz_[0,i]*erro));
        if(matrix_1.shape != matriz_.shape):
            print('Shapes diferentes', matrix_1.shape,matriz_.shape)
            return False
        if( variacao_min <= matrix_1[0,i] and variacao_max >= matrix_1[0,i]  ):
            continue
        else:
            print('Entre:',variacao_min, ' E: ', variacao_max )
            print("False: ", matrix_1[0,i],matriz_[0,i],i)

            return False
    return print(True)
#---------------------------------------------
    

def Zerar_Se(V,zerar):
    [nl,nc] = V.shape
    result = 0
    for i in range(0,nl):
        for j in range(0,nc):
            if abs(V[i,j]) < zerar:
                V[i,j] = 0
                result = 1+result
    return V
def cart2pol(x, y):
    rho = (np.sqrt(x*x + y*y))
    phi = (np.arctan2(y , x))
    return(phi,rho)

def pol2cart(phi,rho):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def calcular_Zfinal(num_barra_dobrado, tipo_linha, tipo_conf,matrizes_conf,distancia_miles_linha,z_base):
    Zfinal_linha = np.zeros((num_barra_dobrado*3,3),dtype=np.cdouble)
    for ix in range(0,num_barra_dobrado):
        #1:64
        if(tipo_linha[ix] == tipo_conf [0]):
            VAR = matrizes_conf[0:3,:];
        if(tipo_linha[ix] == tipo_conf[1]):
            VAR = matrizes_conf[3:6,:];
        if(tipo_linha[ix] == tipo_conf[2]):
           VAR = matrizes_conf[6:9,:];  
        if(tipo_linha[ix] == tipo_conf[3]):
            VAR = matrizes_conf [9:12,:]
        if(tipo_linha[ix] == tipo_conf[4]):
           VAR = matrizes_conf[12:15,:];  
        Zfinal_linha[3*ix:3*ix+3,0:3] = distancia_miles_linha[ix]*VAR/z_base; # matriz impedância das linhas  
    return Zfinal_linha



def mover_valores_de_linha(num_barra_dobrado,impedancias,linhas):
    for iy in range(0,num_barra_dobrado):
        impedancias[3*iy, 0:2] = linhas[iy,:]
    return impedancias



# EEH(1,1)




