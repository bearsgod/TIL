class Grid():
    time=0
    right=None
    left=None
    up=None
    down=None
    readed=False
    
    def __init__(self,vitality):
        self.vitality=vitality

class Container():
    def __init__(self,x):
        self.population=0
        self.start=Grid(x[0][0])
        if self.start.vitality!=0:
            self.population+=1
        center=self.start
        pre=center
        for first_garo in range(1,m):
            now=Grid(x[0][first_garo])
            if now.vitality!=0:
                self.population+=1
            pre.right=now
            now.left=pre
            pre=now
        for sero in range(1,n):
            for garo in range(m):
                now=Grid(x[sero][garo])
                if now.vitality!=0:
                    self.population+=1
                if garo==0:
                    center.down=now
                    now.up=center
                    center=now
                    pre=now
                else:
                    pre.right=now
                    now.left=pre
                    pre=now
    
    def die(self,x,sec):
        if sec-x.time==x.vitality*2:
            self.population-=1

    def splits(self,x,sec):
        if sec-x.time==x.vitality+1:
            if x.right==None or x.right.time==sec:
                spr=Grid(x.vitality)
                x.right==spr.left
                

for T in range(int(input())):
    n,m,k=list(map(int,input().split()))
    case=[]
    for column in range(n):
        case.append(list(map(int,input().split())))
    casemap=Container(case)