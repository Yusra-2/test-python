"""aq="abaacb"
a=input("enter ur answer")
mark=0
if(len(a) == 6):
    for x in a:
        if(x == aq in a [0]):
            mark +=1
            print(mark,"/6")
        print("")
else:
    print("enter the correct num of answers!")

#correct answer
mark=0
answer="abaacbb"
a_user=input("enter ur answer")
for i in range(len(answer)):
    if(a_user[i] == answer[i]):
        mark +=1
    else:
        print(i+1, end=" ")
print()
print(mark, "out of 7")"""

def grade_exam(q_num, marks):
    q_ans=input("enter the answer of {} qs".format(q_num))
    ans=input("enter the answers")
    for i in range(len(q_ans)):
        if(ans[i] == q_ans[i]):
            mark= q_num*marks
        else:
            print("Q", i+1)
    print(mark, "out of 12")
grade_exam(12,2)