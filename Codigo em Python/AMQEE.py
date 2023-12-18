#  =========================================================================
#  ALOCAÇÃO DE MEDIDORES DE QUALIDADE DE ENERGIA ELÉTRICA (AMQEE)
#  =========================================================================
import random
import numpy as np

def  AMQEE(tamPopulacao, taxaCross, taxaMutacao, iteracaoTotal):
    
    #  =====================================================================
    #  Configuracoes iniciais
    tamCromossomo = 100; #34 para tensão e 66 para corrente
    iteracaoAtual = 1;

    #  PASSO 1 - GERAR A POPULACAO INICIAL
    #  =====================================================================
    #  Inicializar populacao
    random.seed() # srand() em C
    populacao = np.random.randint(2, size=(tamPopulacao,tamCromossomo));
    populacao = np.array([[1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1
                ,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0
                ,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0]
                ,[0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1
                ,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1
                ,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1]
                ,[1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0
                ,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1
                ,0,0,0,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1]
                ,[0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0
                ,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0
                ,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0]
                ,[0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0
                ,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1
                ,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1]
                ,[1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1
                ,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0
                ,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,0]
                ,[1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1
                ,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0
                ,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0]
                ,[0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0
                ,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0
                ,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0]
                ,[1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0
                ,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0
                ,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0]
                ,[0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0
                ,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1,1,0
                ,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0]])
    [iPopulacao,jPopulacao] = np.shape(populacao);
    print( iPopulacao,jPopulacao)
    for k in range(0,iPopulacao):
            #Ajuste de acordo com a matriz de conexão
            if (populacao[k,0]==0): 
                populacao[k,34]=0; 
            
            if (populacao[k,1]==0): 
                populacao[k,35]=0 ;  
                populacao[k,36]=0 ; 
            
            if (populacao[k,2]==0):
                populacao[k,37]=0;
                populacao[k,38]=0;
             
            if (populacao[k,3]==0):
                populacao[k,39]=0;
                populacao[k,40]=0;
                populacao[k,41]=0;
            
            if (populacao[k,4]==0): 
                populacao[k,42]=0;
            
            if (populacao[k,5]==0): 
                populacao[k,43]=0;
                populacao[k,44]=0;
            
            if (populacao[k,6]==0): 
                populacao[k,45]=0;
                populacao[k,46]=0;
            
            if (populacao[k,7]==0):
                populacao[k,47]=0;
                populacao[k,48]=0;
            
            if (populacao[k,8]==0): 
                populacao[k,49]=0;
                populacao[k,50]=0;
                populacao[k,51]=0;
            
            if (populacao[k,9]==0): 
                populacao[k,52]=0;
                populacao[k,53]=0;
            
            if (populacao[k,10]==0):
                populacao[k,54]=0;
                populacao[k,55]=0;
            
            if (populacao[k,11]==0): 
                populacao[k,56]=0;
            
            if (populacao[k,12]==0): 
                populacao[k,57]=0;
                populacao[k,58]=0;
                populacao[k,59]=0;

            if (populacao[k,13]==0):
                populacao[k,60]=0;
            
            if (populacao[k,14]==0): 
                populacao[k,61]=0;
                populacao[k,62]=0;
            
            if (populacao[k,15]==0):
                populacao[k,63]=0;
                populacao[k,64]=0;
            
            if (populacao[k,16]==0): 
                populacao[k,65]=0;
                populacao[k,66]=0;
                populacao[k,67]=0;
            
            if (populacao[k,17]==0):
                populacao[k,68]=0;
                populacao[k,69]=0;
            
            if (populacao[k,18]==0): 
                populacao[k,70]=0;
                populacao[k,71]=0;
                populacao[k,72]=0;
            
            if (populacao[k,19]==0): 
                populacao[k,73]=0;
                populacao[k,74]=0;
                populacao[k,75]=0;
            
            if (populacao[k,20]==0):
                populacao[k,76]=0 ;
                populacao[k,77]=0 ;
                populacao[k,78]=0 ;
            
            if (populacao[k,21]==0):
                populacao[k,79]=0 ;
                populacao[k,80]=0 ;
            
            if (populacao[k,22]==0):
                populacao[k,81]=0 ;
                populacao[k,82]=0 ;
            
            if (populacao[k,23]==0):
                populacao[k,83]=0 ;
                populacao[k,84]=0 ;
            
            if (populacao[k,24]==0):
                populacao[k,85]=0 ;
            
            if (populacao[k,25]==0):
                populacao[k,86]=0;
                populacao[k,87]=0;
            
            if (populacao[k,26]==0):
                populacao[k,88]=0;
                populacao[k,89]=0;
                populacao[k,90]=0;
                
            if (populacao[k,27]==0):
                populacao[k,91]=0;

            if (populacao[k,28]==0):
                populacao[k,92]=0;
                populacao[k,93]=0;

            if (populacao[k,29]==0):
                populacao[k,94]=0;

            if (populacao[k,30]==0):
                populacao[k,95]=0;
            
            if (populacao[k,31]==0):
                populacao[k,96]=0;
                populacao[k,97]=0;

            if (populacao[k,32]==0):
                populacao[k,98]=0;
            
            if (populacao[k,33]==0):
                populacao[k,99]=0;
            
            
            #Inserção dos Pontos Estratégicos
            populacao[k,0] = 1 ; #barra 800
            populacao[k,2] = 1 ; #barra 806
            populacao[k,4] = 1 ; #barra 810   
            populacao[k,6] = 1 ; #barra 814 
    
    compare_matrix(populacao,0) 

    # random.seed()
    # print(np.random.randint(35,37) )

    # Restrição na Limitação de Canais
    if (populacao[k,1]==1):
        populacao[k,35]=0; populacao[k,36]=0;
        random.seed()
        populacao[k,np.random.randint(35,37)]=1;               

    if (populacao[k,2]==1):
        populacao[k,37]=0; populacao[k,38]=0;
        random.seed()
        populacao[k,np.random.randint(37,39)]=1;               
    
    if (populacao[k,3]==1):
        populacao[k,39]=0; populacao[k,40]=0; populacao[k,41]=0;
        random.seed()
        populacao[k,np.random.randint(39,42)]=1;               
    
    if (populacao[k,5]==1):
        populacao[k,43]=0; populacao[k,44]=0;
        random.seed()
        populacao[k,np.random.randint(43,45)]=1;               
    
    if (populacao[k,6]==1):
        populacao[k,45]=0; populacao[k,46]=0;
        random.seed()
        populacao[k,np.random.randint(45,47)]=1;               
    
    if (populacao[k,7]==1):
        populacao[k,47]=0; populacao[k,48]=0;
        random.seed()
        populacao[k,np.random.randint(47,49)]=1;               
    
    if (populacao[k,8]==1):
        populacao[k,49]=0; populacao[k,50]=0; populacao[k,51]=0;
        random.seed()
        populacao[k,np.random.randint(49,52)]=1;               
    
    if (populacao[k,9]==1):
        populacao[k,52]=0; populacao[k,53]=0;
        random.seed()
        populacao[k,np.random.randint(52,54)]=1;               
    
    if (populacao[k,10]==1):
        populacao[k,54]=0; populacao[k,55]=0;
        random.seed()
        populacao[k,np.random.randint(54,56)]=1;               
    
    if (populacao[k,12]==1):
        populacao[k,57]=0; populacao[k,58]=0; populacao[k,59]=0;
        random.seed()
        populacao[k,np.random.randint(57,60)]=1;               
    
    if (populacao[k,14]==1):
        populacao[k,61]=0; populacao[k,62]=0;
        random.seed()
        populacao[k,np.random.randint(61,63)]=1;               
    
    if (populacao[k,15]==1):
        populacao[k,63]=0; populacao[k,64]=0;
        random.seed()
        populacao[k,np.random.randint(63,65)]=1;               
    
    if (populacao[k,16]==1):
        populacao[k,65]=0; populacao[k,66]=0; populacao[k,67]=0;
        random.seed()
        populacao[k,np.random.randint(65,68)]=1;               
    
    if (populacao[k,17]==1):
        populacao[k,68]=0; populacao[k,69]=0;
        random.seed()
        populacao[k,np.random.randint(68,70)]=1;               
    
    if (populacao[k,18]==1):
        populacao[k,70]=0; populacao[k,71]=0; populacao[k,72]=0;
        random.seed()
        populacao[k,np.random.randint(70,73)]=1;               
    
    if (populacao[k,19]==1):
        populacao[k,73]=0; populacao[k,74]=0; populacao[k,75]=0;
        random.seed()
        populacao[k,np.random.randint(73,76)]=1;               
    
    if (populacao[k,20]==1):
        populacao[k,76]=0; populacao[k,77]=0; populacao[k,78]=0;
        random.seed()
        populacao[k,np.random.randint(76,79)]=1;               
    
    if (populacao[k,21]==1):
        populacao[k,79]=0; populacao[k,80]=0;
        random.seed()
        populacao[k,np.random.randint(79,81)]=1;               
    
    if (populacao[k,22]==1):
        populacao[k,81]=0; populacao[k,82]=0;
        random.seed()
        populacao[k,np.random.randint(81,83)]=1;               
    
    if (populacao[k,23]==1):
        populacao[k,83]=0; populacao[k,84]=0;
        random.seed()
        populacao[k,np.random.randint(83,85)]=1;               
    
    if (populacao[k,25]==1):
        populacao[k,86]=0; populacao[k,87]=0;
        random.seed()
        populacao[k,np.random.randint(86,88)]=1;               
    
    if (populacao[k,26]==1):
        populacao[k,88]=0; populacao[k,89]=0; populacao[k,90]=0;
        random.seed()
        populacao[k,np.random.randint(88,91)]=1;               
    
    if (populacao[k,28]==1):
        populacao[k,92]=0; populacao[k,93]=0;
        random.seed()
        populacao[k,np.random.randint(92,94)]=1;               
    
    if (populacao[k,31]==1):
        populacao[k,96]=0; populacao[k,97]=0;
        random.seed()
        populacao[k,np.random.randint(96,98)]=1;               
    

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
        # if(matrix_1[0,i] < 0.001): matrix_1[0,i] = 0
        # if(matriz_[0,i] < 0.001): matriz_[0,i] = 0
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


AMQEE(10, 0.8, 0.1, 100)
