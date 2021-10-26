vowels=['a','e','i','o','u']
word='ghuntee'
dictionary = {
    "bhunno" : ["fry"],
    "mange" : ["want","ask","need","desire"],
    "waqt" : ["time"],
    "kar" : ["do"],
    "hai" : ["exist","it's"],
    "yeh" : ["this","it"],
    "masala" : ["spices"],
    "jub" : ["when"],
    "ki" : ["belong"],
    "ghanti" : ["bell","alarm"],
    "baji" : ["ring"]
}
consonant_priority = 1
vowel_priority = 0.1
class tree:
    def __init__(self):
        self.branch={}
        self.value=None
    def add(self,i):
        if len(i)!=0:
            if not i[0] in self.branch:
                self.branch[i[0]] = tree()
            self.branch[i[0]].add(i[1:])
    def preorder(self):
        for i in self.branch.keys():
            print(i)
            self.branch[i].preorder()
            
t=tree()
for i in dictionary.keys():
    t.add(i)
t.preorder()
    
for i in range(len(word)):
    consonant = not word[i] in vowels
