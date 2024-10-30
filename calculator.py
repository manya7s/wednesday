#addition
a = 5
b = 8

# my turn 
from method import evaluate_exp

ans = evaluate_exp('5+8')
print(ans)


# mhmmhm, I have ran out of comments

input_exp = str(input("\nEnter numerical expression (involving only + , - , * and /): "))
print(evaluate_exp(input_exp))