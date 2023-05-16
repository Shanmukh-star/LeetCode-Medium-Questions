class Solution(object):
    def reverse(self, x):
        y=str(abs(x))
        z=y[::-1]
        req=int(z)
        if x>0:
            req=req
        else:
            req=-req
        if req>0 and req<pow(2,31):
            return req
        elif req<=0 and req>=-1*pow(2,31):
            return req
        else:
            return 0;
