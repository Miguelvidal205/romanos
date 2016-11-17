class numeros_romano():
    def __init__(self, num):
        num=input("introduce un numero para ser convertido a romano")
        self.num=str(num)
        self.num_romano=""
        if(num==0):
            print ("Introduce un numero mayor que cero")
    def transformar(self):
        unidad={0:"",1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
        decena={0:"",10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC"}
        centena={0:"",100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM"}
        unidadMil={0:"",1000:"M",2000:"MM",3000:"MMM",4000:"IV"}
        
        cont=1

        for x in range(len(self.num), 0, -1):
            if cont == 1:
                self.num_romano = unidad[int(self.num[x-1])]
            elif cont == 2:
                self.num_romano = decena[int(self.num[x-1])*10]+self.num_romano
            elif cont == 3:
                self.num_romano = centena[int(self.num[x-1])*100]+self.num_romano
            elif cont == 4:
                self.num_romano = unidadMil[int(self.num[x-1])*1000]+self.num_romano
            cont +=1
    def visualizar(self):
        print (self.num_romano)

numrom=numeros_romano(0)
numrom.transformar()
numrom.visualizar()