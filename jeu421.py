from random import randint
from time import sleep
class Dee:
    
    def __init__(self):
        self.value=randint(1,6)
        
    def __repr__(self):
        return self.value
        
class Lancer:
    
    def __init__(self):
        
        a=[Dee().value,Dee().value,Dee().value]
        d={}
        
        for c in a:
            if d.get(c)==None:
                d[c]=1
            else:
                d[c]+=1
            
        self.value=d
        self.v2=sorted(a)
    

def estsuite(r1):
        a=tuple(r1.v2)
        if a in [(1,2,3),(2,3,4),(3,4,5),(4,5,6)]:
            return True
        else:
            return False
        
class Compareinplayer:
   
    
    def __init__(self,r1):
        if 4 in r1.value.keys() and 2 in r1.value.keys() and 1 in r1.value.keys():
            self.type=0
            self.token=10
        elif len(r1.value)==1 and r1.value=={1:3}:
            self.type=1
            self.token=7
        elif len(r1.value)==2 and r1.value=={2:2,1:1}:
            self.type=5
            self.token=2
        elif len(r1.value)==1:
            self.type=3
            self.token=r1.v2[0]
        elif len(r1.value)==2:
            self.type=2
            self.token=min(r1.v2)
        elif estsuite(r1):
            self.type=4
            self.token=2
        else:
            self.type=6
            self.token=1
    
    
    def __repr__ (self):
        
        return self.type
    
     
        
class Joueur:
    def __init__(self,nom):
        self.nom=nom
        self.lancer=0
        self.type=-1
        self.token=0
        self.tokenM=0
    def nlancer(self):
        self.lancer=Lancer()
        self.type=Compareinplayer(self.lancer).type
        self.tokenM=Compareinplayer(self.lancer).token

class Comparemanche:
    def __init__(self, j1 ,j2):
        if Compareinplayer(j1.lancer).type < Compareinplayer(j2.lancer).type:
            self.winmanche=j1.nom
        elif Compareinplayer(j1.lancer).type > Compareinplayer(j2.lancer).type:
            self.winmanche=j2.nom
        else:
            if sum(j1.lancer.v2)>sum(j2.lancer.v2):
                self.winmanche=j1.nom
            elif sum(j1.lancer.v2)==sum(j2.lancer.v2):
                self.winmanche=None 
            else:
                self.winmanche=j2.nom
            
def verif21(j1,j2,decharge):
    if decharge.token<0:
        if j1.token<j2.token:
            j1.token+=abs(decharge.token)
            j2.token-=abs(decharge.token)
        else:
            j2.token+=abs(decharge.token)
            j1.token-=abs(decharge.token)
    else:
        pass
    
class Manche:
    def __init__(self,j1,j2):
        nom1=['421','Triple As','Fiches','Baraques','Suites','nénette','autres']
        self.token=21
        print('La Charge')
        while  self.token>=0:
            j1.nlancer()
            j2.nlancer()
            sleep(1)
            if Comparemanche(j1,j2).winmanche==j1.nom:
                j2.token+=j1.tokenM
                self.token=self.token-j1.tokenM
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
            elif Comparemanche(j1,j2).winmanche==j2.nom:
                j1.token+=j2.tokenM
                self.token=self.token-j2.tokenM
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
            elif Comparemanche(j1,j2).winmanche==None:
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
            verif21(j1,j2,self)
        print('La décharge')
        while j1.token>0 and j2.token>0:
            j1.nlancer()
            j2.nlancer()
            sleep(1)
            if Comparemanche(j1,j2).winmanche==j1.nom:
                j2.token+=j1.tokenM
                j1.token-=j1.tokenM
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
            elif Comparemanche(j1,j2).winmanche==j2.nom:
                j1.token+=j2.tokenM
                j2.token-=j2.tokenM
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
            elif Comparemanche(j1,j2).winmanche==None:
                print(str((nom1[j1.type],j1.lancer.v2)) ,str((nom1[j2.type],j2.lancer.v2)))
        if j1.token<=0:
            self.winner=j1.nom
            j1.token=0
            j2.token=21
        else:
            self.winner=j2.nom
            j1.token=21
            j2.token=0
    


class Jeu:
    def __init__(self,n1,n2):
        self.player=[n1,n2]
        self.gagnant=''
    
    def parti(self):
        self.gagnant=Manche(self.player[0],self.player[1]).winner
    def __repr__(self):
        return f"Le gagnant est {self.gagnant} un grand gg à lui"
    
    
def lancer_le_jeu(j1,j2):
    assert type(j1) == str and type(j2) == str, 'coup dur'
    a=Joueur(j1)
    b=Joueur(j2)
    game=Jeu(a,b)
    game.parti()
    return game