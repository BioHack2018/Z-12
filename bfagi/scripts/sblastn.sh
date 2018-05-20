#!/bin/bash

echo $1


echo "Run Nucleotide aligning query sequences"

python seqn.py /Users/mdylag/workspaces/biohackathon/p1.fasta /Users/mdylag/workspaces/biohackathon/genemark_suite_macosx/gmsuite/gmsn.pl
python seqn.py /Users/mdylag/workspaces/biohackathon/mh179470.fasta /Users/mdylag/workspaces/biohackathon/genemark_suite_macosx/gmsuite/gmsn.pl

#/Users/mdylag/workspaces/biohackathon/genemark_suite_macosx/gmsuite/gmsn.pl --phage --faa /Users/mdylag/workspaces/biohackathon/p1.fasta
