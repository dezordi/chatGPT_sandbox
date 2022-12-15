import click
from Bio import SeqIO
from Bio.pairwise2 import align
from Bio.SubsMat import MatrixInfo as matlist

@click.command()
@click.option('--input_file', required=True, type=click.Path(), help='The input fasta file with the sequences to align.')
@click.option('--output_file', required=True, type=click.Path(), help='The output fasta file with the aligned sequences.')
def main(input_file, output_file):
    # Read the input sequences from the input fasta file
    sequences = [seq for seq in SeqIO.parse(input_file, 'fasta')]
    # Define the scoring matrix to use for the alignment
    scoring_matrix = matlist.blosum62
    # Perform the global alignment of the sequences
    alignment = align.globalds(sequences[0].seq, sequences[1].seq, scoring_matrix, -10, -0.5)[0]
    # Write the aligned sequences to the output fasta file
    with open(output_file, 'w') as f:
        f.write(f'>{sequences[0].id}\n{alignment[0]}\n')
        f.write(f'>{sequences[1].id}\n{alignment[1]}\n')

if __name__ == '__main__':
    main()
