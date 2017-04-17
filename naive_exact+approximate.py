

import wget
url = 'https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa'
filename = wget.download(url)


class match():

    def __init__(self): 
        global genome
        genome = ''
        with open(filename, 'r') as f:  
            for line in f:
                if not line[0] == '>':
                    genome += line.rstrip() 
        
    
    def naiveExact(self, pattern):  
        occurrence = []
        #Find the reverse complement of the pattern
        complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
        reverse_complement = ''
        for base in pattern:
            reverse_complement = complement[base] + reverse_complement    
        
        if pattern == reverse_complement:    
            p = [pattern] 
        else: 
            p = [pattern, reverse_complement]
        
        for k in p:
            for i in range(len(genome)-len(k)+1):
                match = True
                for j in range(len(k)):
                    if genome[i+j] != k[j]:
                        match =False
                        break
                if match:
                    occurrence.append(i)
        
        num = len(occurrence); 

        if num:
            left_most_occurrence = min(occurrence)
            string1 = ("The genome sequence has %d unique occurrences of the pattern %s or its reverse complement %s." %(num, pattern, reverse_complement))    
            string2 = ("The offset of the first occurrence of the pattern or its reverse complement in the genome is %d." %left_most_occurrence)
            return string1 + string2
        else:
            return ("No exact matches of the pattern and its reverse complement were found.")
    
    
    def naiveMismatch(self, pattern):
        identical_occur = []
        mismatch_index = []    
        max_mismatch = int(input('Enter the maximum number of allowed mismatches:'))
        for i in range(len(genome)-len(pattern)+1):       
            match = True
            mismatch = 0        
            for j in range(len(pattern)):
                if genome[i+j] != pattern[j]:               
                    mismatch +=1
                    match = False
                    
                    if mismatch >= (max_mismatch + 1):
                        break
                
            if  0 < mismatch < (max_mismatch + 1):
                mismatch_index.append(i)           
    
            if match:
                identical_occur.append(i)
        
        num = len(identical_occur); mismatch_num = len(mismatch_index)
        string1 = ("The genome sequence has %d exact matches of the pattern %s." %(num, pattern))    
        string2 = ("The genome sequence has %d approximate pattern match/s (up to %d mismatches) at offsets %s." %(mismatch_num, max_mismatch, mismatch_index))   
        result = string1 + string2       
       
        if identical_occur and mismatch_index: #check to make sure both lists are not empty
            left_most_occur = min(min(identical_occur), min(mismatch_index))
            string3 = ("The offset of the first occurrence of the pattern (with or without mismatches) in the genome is %s." %left_most_occur)
            result = string1 +  string2 +  string3
        
        return result
   