moedasTop = [2,1,0.5,0.2,0.1,0.05,0.01]

def arranjaTroco(val):
    moeda = {}
    while val>0:
        val = round(float(val),2)
        for m in moedasTop:
            if val>=m:
                if m not in moeda:
                    moeda[m]=0
                moeda[m]+=1
                val-=m
                break
    result = ""
    for m in moedasTop:
        if m in moeda:
            if m>=1:
                result += f" {moeda[m]}x {m}e,"
            else:
                result += f" {moeda[m]}x {int(m*100)}c,"
    result = result[:-1]
    result += "."
    return result

print(arranjaTroco(2.17))