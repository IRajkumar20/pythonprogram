nums=int(input())
answer=[]
while (nums>0):
    digit=nums%2
    answer.append(digit)
    nums=nums//2
answer.reverse()

for i in answer:
    print(i,end="")

