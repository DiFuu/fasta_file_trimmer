# fasta_file_trimmer

The program incorporates an argument parser that accepts:

- An input file
- Number of nucleotides to remove from the 5' (from the beginning of the sequence)
- Number of nucleotides to remove from the 3' (from the end of the sequence)
- Ns eliminator (Only the N's in 5') (parameter without associated value)

The program uses Biopython to read the provided fasta file and
removes the 5' Ns if the parameter is included.

Subsequently, whether or not the Ns at the beginning are removed,
then remove start and end nucleotides as requested by the console.

Once the sequences have been processed, two files are created:

1. A file containing the name of the sequence, the original size and the finished size.
These three values must be separated by tabs and saved in a TSV file

2. A fasta file with the new sequences. The function SeqIO is used to create this file

The program to be invoked with -h must give a detailed help to be able to be used correctly
