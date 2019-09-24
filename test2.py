with open('input/carbrandname.txt', 'r',encoding='utf-8') as f:
    data = f.readlines()
newdata = []
for item in data:
    newdata.append(item.replace('\n',"|"))
with open('input/car.txt', 'w',encoding='utf-8') as f:
    for i in range(2):
        f.write(''.join(newdata[i*165:i*165+165]))
        f.write('\n')
# print(newdata)