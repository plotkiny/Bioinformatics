

file2 = 'file.txt'

import numpy as np

def consensus(file):

    consensus = []
    letters = ''
    global dictionary; dictionary = { 'A': 11.0, 'C':22.0, 'G':33.0, 'T':44.0 }
    global sequence; sequence = {}

    id_num = ''    
    with open(file) as f:
        for line in f:
            line = line.replace(' ','').strip()
            if line.startswith('>'):
                id_num += '0'
                sequence[id_num] = ''
            else:
                sequence[id_num] += line
        
        id_num = len(id_num)
        length = len(sequence['0'])
        array = np.zeros(shape=(id_num, length))

        for k,v in sequence.items():
            k = len(k)-1; v = [dictionary[x] for x in v]
            for j in range(length):
                array[k,j] = v[j]

        for j in range(length):
            occurrence = occurNumber(array[:,j])
            consensus.append(occurrence)
        
        for i in consensus:
            for k,v in dictionary.items():
                if i ==v:
                    letters += k 
        
    return letters
              
def occurNumber(array):
    (values,counts) = np.unique(array,return_counts=True)
    max_occur= np.argmax(counts)
 
    return values[max_occur]    
    
def maximum(d):
    m=max(d.values())
    M = str([k for k,v in d.items() if v==m][0])

    return M  
    
def main():
    
    t = consensus(file2)
    concensus_string = t

    with open("concensus_string.txt", "w") as text_file:
        text_file.write(concensus_string + "\n")
            
    text_file.close()
        
main()
    
    
    
    