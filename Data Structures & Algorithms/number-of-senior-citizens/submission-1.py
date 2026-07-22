class Solution:
    def countSeniors(self, details: List[str]) -> int:
        k=0
        for i in details:
            if int(i[11:13])>60:
                k+=1 
        return k 