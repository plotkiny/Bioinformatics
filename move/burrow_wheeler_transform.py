
#string = 'panamabananas'

class bwt():
    
    def __init__(self):
        string = input('Please input the name of the string you would like to read: ').lower()  
        self.string = string + '$'  
        
    def transform(self):
        n = len(self.string)
        self.merge = ['']*n                
        self.cyclic = []
        characters = []    
        
        for i in range(n-1, -1, -1): #loop through the pattern p from the end to the beginning        
              characters.append(self.string[i])
            
        for j in range(n):
            new_string = characters[j] + self.string[:-1]
            self.cyclic.append(new_string)            
            self.string = new_string
              
        transform = []
        for i in sorted(self.cyclic):         
            last = i[-1:]
            transform.append(last)
            
        self.bwt = ''.join(transform)
        print("The Burrow-Wheeler Transform is %s " %self.bwt)    

        #Create 2-mer (first and last column)
        self.sorted_bwt = sorted(self.bwt)
        for j in range(0,len(self.string)):
            self.merge[j] = self.bwt[j] + self.sorted_bwt[j]
        self.merge = sorted(self.merge)         
        
        return n-2
       
    def invert(self, n): 

        if n == 0:
            return ('The orginal string was "%s" ' %self.merge[0][1:])  
        else:
            for j in range(0, len(self.string)):
                self.merge[j] = self.bwt[j] + self.merge[j]
            self.merge = sorted(self.merge)
            
            return self.invert(n-1)  #recursive function call            
        
           
def main():
    a = bwt()
    transform = a.transform()
    inversion = a.invert(transform)      
    
    return inversion
  
main()          
        
        
        

                
        
        