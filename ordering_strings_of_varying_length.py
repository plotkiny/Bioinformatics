
"""

Sample Dataset

D N A
3

"""

from itertools import product
import functions

file = 'test.txt'
def enumerate_k_mer(file):

    l = functions.read_line(file)           
    s = l[0]; n = int(l[1]);

    numbers = functions.factorial_numbers(n)    
    perm = []
    
    for i in numbers:
        perm.extend([''.join(x) for x in product(s, repeat=i) ]) #itertools.product(*['abc']*n)
    sorted_string = sorted(perm, key=lambda word: [s.index(c) for c in word])

    return sorted_string

def main():
    
    ordered_string = enumerate_k_mer(file)
      
    with open("file_name.txt", "w") as text_file:
        for i in ordered_string:
            text_file.write(i + "\n")
    text_file.close()
    
main()
                
