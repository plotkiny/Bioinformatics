
"""
Pseudocode: import_file function
   --> Download the kmer_index, boyer_moore_preprocessing and human_chromosome files into the local directory
"""

local_directory = 'C:/fake_path'

kmer_index = 'https://d28rh4a8wq0iu5.cloudfront.net/ads1/code/kmer_index.py' 
boyer_moore_preprocessing = 'http://d28rh4a8wq0iu5.cloudfront.net/ads1/code/bm_preproc.py'
human_chromosome = 'http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/chr1.GRCh38.excerpt.fasta'

from definitions import import_file
import_file(kmer_index,boyer_moore_preprocessing,human_chromosome,local_directory) #downloading and importing the file into the local directory


"""
Read the genome of the downloaded human_chromosome file 
"""

chromosome = human_chromosome.split('/')[-1]
def readGenome(chromosome): 
    global genome
    genome = ''
    with open(chromosome, 'r') as f:  #indicates that we are opening a file for reading, 'w' indicates writing
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()


"""
Pattern matching with Boyer Moore (pre-processing the pattern)
"""

from bm_preproc import BoyerMoore
p_bm = BoyerMoore(pattern)

def boyer_moore(pattern, p_bm, genome):
    i = 0
    occurrences = []
    character_match = 0; character_mismatch = 0; num_alignments = 0    
    
    while i < len(genome) - len(pattern) + 1:  #loop through all the positions in t where p can start
        shift = 1  #how much we can move after character comparison
        mismatched = False
        num_alignments +=1        
        
        for j in range(len(pattern)-1, -1, -1): #loop through the pattern p from the end to the beginning
            if pattern[j] != genome[i+j]:
                skip_bc = p_bm.bad_character_rule(j, genome[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                character_mismatch += 1
                mismatched = True
                break
            if pattern[j] == genome[i+j]:
                character_match += 1
                
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip() # if perfect match, special instance of good suffix rule
            shift = max(shift, skip_gs)
        i += shift  #update position by shift
        char_comparison = character_mismatch+character_match
        
    alignments = ("The number of alignments is %d " %num_alignments + "\n")
    char_compar = ("The number of character comparisons performed %d " %char_comparison + "\n")
    occurrences = ("The pattern occurs in the genome at %s " %occurrences + "\n")   
    
    return alignments + char_compar + occurrences


    
"""
Approximate matching with Boyer Moore (using the pigeon-hole principle)
"""

from kmer_index import *  #importing file for building a k-mer_index (inside the local directory)
from bm_preproc import BoyerMoore

index = kmer_index.Index(genome,8)
queryIndex = kmer_index.queryIndex(p,genome,index)
 
#Divide p into n+1 segments and one of those should match exactly
def approximate_match(p,t,n):
    segment_length = int(round(len(p)/(n+1)))
    all_matches = set() #create a set to fill all the indices where matches were found
    for i in range(n+1): #calculate the bounds of p for the segment we are searching for
        start = i*segment_length
        #p might not be a perfect multiple of n+1 so we resize the last segment accordingly
        end = min((i+1)*segment_length, len(p)) #take minimum to not run past end of p 
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT') #preprocessing of the pattern
        matches = boyer_moore(p[start:end], p_bm, t)
        
        for m in matches:
            if m < start or m-start+len(p) > len(t): #test if location does not let p run off
                continue
            mismatches = 0
            #test part of pattern p before the segment that we just compared (and that was an exact match)          
            for j in range(0, start): #compare number of mismatches
                if not p[j] == t[m-start+j]:
                    mismatches +=1
                    if mismatches > n:
                        break
           #compare the suffix after the segment
            for j in range(end, len(p)):
               if not p[j] == t[m-start+j]:
                   mismatches +=1
                   if mismatches > n:
                       break
            if mismatches <= n: #double check if the number of mismatches is no more than n      
                all_matches.add(m-start) #want the beginning of the pattern (not the beginning of the subpattern)

    return list(all_matches)
    
p = 'AACTTG'
t = 'CACTTAATTTG'
print(approximate_match(p,t,2))
                   











