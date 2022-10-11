# TODO
## Allmänt:

# Stats

kombinera två dicts:
```
dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18, 'Rick': 20, 'Matt': 16}

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3

dict_3 = mergeDictionary(dict_1, dict_2)
print(dict_3)
 

Output

{'John': 15, 'Rick': [20, 10], 'Misa': 12, 'Bonnie': 18, 'Matt': 16}
```





## PPTX
* from pptx import Presentation
* gör någon supergenerell vanlig PP-presentation med rätt färger 
* hämta data från ett statistikobjekt 
* lägg allt i funktioner så den bara kör på en ren csv och sen producerar en pp
  
## Presentation
* kolla på den här tidslinjegrejen
* fundera på hur man gör med zonerna och avståndet till boll och spelare
