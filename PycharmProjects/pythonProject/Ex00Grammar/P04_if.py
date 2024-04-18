'''
    if 조건:
        명령
'''
from tkinter import simpledialog

score = simpledialog.askinteger("Input", "Your score?", parent=None)
print(score)

if score >= 90:
    result = "A등급"
elif score >= 80:
    result = "B등급"
elif score >= 70:
    result = "C등급"
elif score >= 60:
    result = "D등급"
else:
    result = "F등급 이하"



def subGrade(score):
    result = '';
    if score < 100 and score >= 60 :
        if (score % 10 >= 7) : result = '+';
        elif(score % 10 >= 4) : result = '0';
        else : result = '-';


    elif (score == 100) :
        result = '+';
    return result;
print(("당신의 점수는 %d점 이고 학점은 %s%s입니다.\n" %(score, result, subGrade(score))));

