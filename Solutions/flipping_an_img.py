class Solution:
    def flipAndInvertImage(self, A: [[int]]) -> [[int]]:
        if not A:
            return 0
        if A:
            listone = []
            listtwo = []
            for i in A:
                for j in range(len(i)):
                    listone.append(i[-1-j])
                for k in range(len(listone)):
                    if listone[k] == 0:
                        listone[k] = 1
                    elif listone[k] == 1:
                        listone[k] = 0                      
                listtwo.append(listone)
                listone = []
        return listtwo