'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word,counter=None):
    
   if counter is None:
       counter = 0 
       
   l = list(word)
   new_word = None 
      
   if len(l)>=2:
       
       if l[0] == 't' and l[1] == 'h':
           counter +=1
       
       jnr = ""
       
       new_word = jnr.join(l[1:])
      
       
       return count_th(new_word,counter)
       
   
   
   return counter

print(count_th('owithqebthwotheirfth'))