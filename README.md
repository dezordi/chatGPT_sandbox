# chatGPT_sandbox
Repository created to store scripts created with ChatGPT IA.


### Script 01_global_alignment.py

I asked to ChatGPT: *Could you write a script in python to perform a pairwise nucletide alignment using a global approach? the score matrix should be declared as a table inside the code, and the fasta with sequencies  should be parsed as a input fasta file using the click lib and read with seqIO method of biopython lib. The output should be a fasta file with the aligned sequences.*

Moreover, the IA explained how can I run the script:

```bash
python align_sequences.py --input_file sequences.fasta --output_file aligned_sequences.fasta
```

So, I asked: *Could you create a requirements.txt file with the dependencies of the aforementioned code that can be used with pip?* And that is! the requirements.txt was created!!

And tested with:

```bash
conda create -n "test_chat" python=3.9
conda activate test_chat
pip install -r requirements/01_requirements.txt
python 01_global_alignment.py --input_file test_files/01_input.fa --output_file test_files/01_output.fa
```

**PS**: This one is not the first code that ChatGPT returned, I made at least 4 attempts with the same question, the first fours returned codes that broke in different parts...