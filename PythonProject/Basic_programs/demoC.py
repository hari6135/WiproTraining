import A

class C(A,B):
    def __init__(self,n1,n2):
        A.__init__(self,n1,n2)
        B.__init__(self,msg)

    def display(self):
        print('Done!')

    def final(self):
        A.display(self)
        B.display(self)