
import sys
sys.path.append("/fake_path")

 
from reverse_complement import informatic #import functions
from translation import rna_to_protein
 
def translate():
    file = 'test.txt'
    dna_sequences = {}

    #import the dna strand in the file    
    with open(file) as f:
        for line in f:
            line = line.replace(' ','').strip()
            if line.startswith('>'):
                id_seq = line[1:]
                dna_sequences[id_seq] = ''
            else:
                dna_sequences[id_seq] += line

    f.close()
    rc_class = informatic() #import the informatic class
        
    #find the reverse complement of the dna strand, add the sequence to the dictionary   
    id_seq_reverse = id_seq + '_reverse_complement'    
    dna_sequences[id_seq_reverse] = rc_class.reverse_compliment(dna_sequences[id_seq])
    
    #translate the dna sequences into rna using the informatic class and accounting for reading frames
    rna_sequences = {}    
    for k,v in dna_sequences.items():
        for i in range(3):
            key = k + '_rna_' + str(i)
            value = rc_class.transcribe(v[i:])
            rna_sequences[key] = value
        
    #translating rna into protein
    protein_sequences = []
    translation_class = rna_to_protein()
    for v in rna_sequences.values():
        proteins = translation_class.translation(v)
        protein_sequences += proteins
    
    protein_sequences = set(protein_sequences)    
    
    return protein_sequences
        
    
def main():
    
    t = translate()

    with open("open_reading_frame.txt", "w") as text_file:
        for i in t:       
            text_file.write(i + "\n")  
    text_file.close()
     
main()
