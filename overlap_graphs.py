
import sys
sys.path.append("/fake_path")

from itertools import permutations
import fasta_functions 

file = 'file.txt'

def naive_overlap_map(file):
    
    global seq_dict; seq_dict = fasta_functions.read_genome(file)  #reading FASTA sequence strings   
    global seq_dict_reversed; seq_dict_reversed = dict((v,k) for k,v in seq_dict.items())    
    
    global seq_list; seq_list = []    
    for k,v in seq_dict.items():
        seq_list.append(seq_dict[k])
        
    overlap = []
    for a,b in permutations(seq_list,2): #generating all permutations for pair of strings       
        overlap_length = fasta_functions.string_overlap(a,b, min_length = 3)  #implementing overlap function
        if overlap_length >= 3:
            one = seq_dict_reversed[a]
            two = seq_dict_reversed[b]
            overlap.append((one,two))
    
    
    print(len(overlap))
    print(len(set(overlap)))
            
    return overlap
    
def main():
    
    t = naive_overlap_map(file)
      
    with open("overlap_graph.txt", "w") as text_file:
        for i in t:       
            one = i[0]; two = i[1]
            text_file.write(one + ' ' + two + "\n")
    
    text_file.close()
    
    
main()
                
            
            
            
        
   