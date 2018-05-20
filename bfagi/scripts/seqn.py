import subprocess
import argparse
import sys
import os

lox1="ATAACTTCGTATA"
lox2="TACCGTTCGTATA"

#/Users/mdylag/workspaces/biohackathon/p1.fasta
#Pierwszy argument do porgamu to plik fasrta, drugi argument to sciezka do
#Drugi argument do narzedzia GeneMarks (ORF)
print "Search for sequence in fasta file ", sys.argv[1] , sys.argv[2]

#Fuynkcja wyszukuje w pliku fasta zawiuerajacym sekwencje nukleotydowa sekwencji lox (lox1, lox2)
def blastn( seq ):
   if seq.find(lox1) != -1:
       return 1
   elif seq.find(lox2) != -1:
       return 2
   else:
       return 0;
   return

def orf():
   val=subprocess.call([sys.argv[2],"--phage","--faa",sys.argv[1]])
   print val;
   return

def blastp():
   (dirname, filename)=os.path.split(sys.argv[1]);
   filename = filename + ".faa";
   print "filename", filename;

   val=subprocess.call(["blastp","-query",filename,"-subject", "integraza.txt","-outfmt","6 ppos pident sseqid sseq"])

   print "val"
   print val
   return;

#lines = f.readlines()[1:]
#print genome;

f  = open(sys.argv[1], "r")
genome = f.read();

#Wywolanie funkcji blastn
vbn = blastn(genome);
f.close();

if vbn == 0:
#Jesli vbn jest rowne 0 to wykonaj tu
   print "Run gmsn.pl tool to generate amino acid sequences"
   orf();
   print "Run blastp"
   blastp();

else:
#Jesli vbn jest rozne 0 to wykonaj tu
   print "Lox found"
