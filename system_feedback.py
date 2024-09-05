from control.matlab import *

H_1=tf (1 ,[1 ,2])
H_2=tf (1 ,[1 ,3])

H_parallel=parallel(H_1,H_2)
print('Parallel: ', H_parallel)

H_serie=series(H_1,H_2)
print('Serie:', H_serie)

negative_feedback = feedback(H_1,H_2, sign=-1) # H1 é o ramo direto e H2 é o ramo de realimentacao
print('Negative feedback:', negative_feedback)
print('dc gain:', dcgain(negative_feedback))

positive_feedback = feedback(H_1,H_2, sign=+1) # H1 é o ramo direto e H2 é o ramo de realimentacao
print('Positive feedback', positive_feedback)
print('dc gain:', dcgain(positive_feedback))