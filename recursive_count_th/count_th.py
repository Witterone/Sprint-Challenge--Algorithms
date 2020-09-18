'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
   l = list(word)
   new_word = None
   counter = 0
   
   if len(l)>=2:
       
       if l[0] == 't' and l[1] == 'h':
           counter +=1
       else:
           counter = counter
       jnr = ""
       
       new_word = jnr.join(l[1:])
       print(new_word, counter)
       
       count_th(new_word)
       
   return counter


print(count_th('math'))