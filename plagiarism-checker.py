import itertools
def define_plagiat(A,B):
    A = A.split()
    B = B.split()
    plag = set()
    for i, j in itertools.product(range(len(A)), range(len(B))):
        L = [u for u,v in itertools.takewhile(lambda u_v : u_v[0]==u_v[1], zip(A[i:], B[j:]))]
        if len(L)>=2:
            plag.update([' '.join(L)])
    return list(plag)
