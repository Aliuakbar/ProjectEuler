
with open(r"C:\Users\aliua\Desktop\p022_names.txt", "r") as names:
    x = ""
    for name in names:
        x += name
    x = x.split(",")
    for i in range(len(x)):
        x[i] = x[i][1:-1]
    y = []
    for i in range(len(x)):
        temp = []
        for t in range(len(x[i])):
            temp.append(x[i][t])
        y.append(temp)
        
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for i in range(len(abc)):
    dic[abc[i]] = i + 1

result = []

y.sort()

for i in range(len(y)):
    namesum = 0
    for t in range(len(y[i])):
        namesum += dic[y[i][t]]
    result.append(namesum)
                   
for i in range(len(result)):
    result[i] *= i + 1
    
print(sum(result))
    

