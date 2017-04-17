from functions import read_fasta
import numpy as np

class superstring():
        
    def substr_in_all(self,arr, part):
      for dna in arr:
        if part not in dna:
          return False
      return True
    
    def common_substr(self,arr, l):
      first = arr[0]
      for i in range(len(first)-l+1):
        part = first[i:i+l]
        if self.substr_in_all(arr, part):
          return part
      return ""
    
    def longest_common_substr(self,arr):
      l = 0; r = len(arr[0])
    
      while l+1<r:
        mid = (l+r) // 2
        if self.common_substr(arr, mid)!="":
          l=mid
        else:
          r=mid
    
      return self.common_substr(arr, l)


def main():       
    file = 'test.txt'
    seq_dict = read_fasta(file)
    array = np.chararray((1,0))
    for k,v in seq_dict.items():
        array = np.append(v,array)
    
    lcs = superstring()
    return lcs.longest_common_substr(array)
      
main()
      