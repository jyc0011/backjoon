def date_calc(today):
    y,m,d=map(int,today.split("."))
    return (y-2000)*12*28+m*28+d

def solution(today, terms, privacies):
    answer = []
    day=date_calc(today)
    term_dict={}
    
    for term in terms:
        alp,num=term.split()
        term_dict[alp]=int(num)*28
        
    for i in range(len(privacies)):
        priv_day, alp= privacies[i].split()
        term_length = term_dict.get(alp, 0)
        if day >=date_calc(priv_day)+term_length:
            answer.append(i+1)
    return answer