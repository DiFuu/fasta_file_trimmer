#we import the necessary modules
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

#Function to remove the Ns in case it is requested
def eliminar(seq_dic):
    
    #We create two lists (lista2 later) where to store the sequences
    lista1 = []

    #Creamos diccionario donde guardar la secuencia final
    dic = {}
    
     #Remove the Ns and save in a new dictionary
     #Search within the list and if it finds an N it skips it until it finds
     #a nucleotide, from there it is saving
    for s in seq_dic:
        lista2 = []
        lista1 = seq_dic[s]
        i = 0
        for l in lista1:
            if l == "N" and i == 0:
                continue
            else:
                i = 1
                lista2.append(l)

        #We join all the values of the list into one just to be able to save it in the dictionary
        conector = ""
        lista = conector.join(lista2)
        
        #We keep it in the dictionary
        dic[s] = lista

    return dic

#We ask for all necessary arguments
#if we write -n, it is activated to delete Ns, deactivated by default
parser = argparse.ArgumentParser(
    description="Trimmer")
parser.add_argument(
                    '-in', 
                    action="store", 
                    dest="infile", 
                    help="Input file")
parser.add_argument(
                    '-b',
                    action="store",
                    dest="datob",
                    type=int,
                    help="Number of nucleotides to remove from 5'")

parser.add_argument(
                    '-e',
                    action="store",
                    dest="datoe",
                    type=int,
                    help="Number of nucleotides to remove from 3'")

parser.add_argument(
                    '-n',
                    action="store_true",
                    dest="eliminarN",
                    default=False,
                    help="-n to remove Ns from 5'")

#We pass the arguments to results and open the file
results = parser.parse_args()
iterator = SeqIO.parse(results.infile,"fasta")

#Dictionary to save the sequences and their name
seq = {}

for record in iterator:
    seq[record.id]=record.seq
    
#Variable n to know if we eliminate Ns or not
n = results.eliminarN


#We create a new dictionary
seq_mod_n = {}

#If we are asked to remove the Ns, we enter the remove function
if n == True:
    seq_n = eliminar(seq)
else:
    seq_n = seq
  
#b variable to remove nucleotides at the beginning
b = results.datob
#e variable to remove nucleotides at the end
e = results.datoe
#We create list to be able to modify the sequences
seq_list = []
#We create the new dictionary where to put the new sequences
seq_mod = {}

#For each value in the dictionary, we update the list, and save to the new dictionary
for q in seq_n:
    seq_list = seq_n[q]
    seq_mod[q] = seq_list[b:-e]

#We open the tsv file in read mode 
file1 = open("sequences.tsv","w")

#We print the name of the sequence, the original length and the final length
#in a tab-separated file (\t)
for s in seq_mod:
    file1.writelines(s + "\t" + str(len(seq[s])) + "\t" + str(len(seq_mod[s])) + "\n")

#To save the sequences in a new variable type Seq
seqs = []

for sq in seq_mod:
    simple_seq = SeqRecord(Seq(str(seq_mod[sq])), id=sq, description="")
    seqs.append(simple_seq)
      
#We print a .fasta file with the new sequences
SeqIO.write(seqs,"sequences.fasta","fasta")

#We close the files
file1.close()
