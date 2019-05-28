import sys 
import os 

sys.argv[1]
number_progs = int(sys.argv[1])
outfile = open("dataset2.txt", "w")

while (number_progs != 0 ):
    os.system("cd " +os.getcwd())
    os.system("python generator.py")
    
   
    with open('intermediate.txt','r') as f:
        for line in f:
            for word in line.split():
                outfile.write(str(word))
                #if (indexxx % 2 != 0 ):
                 #   outfile.write(".")

               
                outfile.write(" ")
                
                           
    #outfile.write("xxsasadasd")
    outfile.write('\t')
      

          
    os.system("python assem.py intermediate.txt")
    codess= 0 
    indxx = 0 
    with open('obcode.txt','r') as f:
        for line in f:
            for word in line.split():
                #outfile.write(str(word)+ " ")
                codess = codess+1
    
    codess = codess -1
    with open('obcode.txt','r') as f:
        for line in f:
            for word in line.split():
                outfile.write(str(word))
                if(codess != indxx):
                    outfile.write(" ")
                indxx = indxx +1 

    outfile.write("\n")            

		
    number_progs= number_progs-1 



