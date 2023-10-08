class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        score = [0]*len(questions)
        for j in range(len(questions)):
            i=j

            while i< len(questions):
                score[j] = score[j] + questions[i][0]
                print(score, questions[i][0])
                i=i+questions[i][1]+1
                print(i)
        return max(score)
    

a=Solution()
l=[[20,4],[78,2],[74,1],[48,1],[38,1],[80,3]]
print(a.mostPoints(l))