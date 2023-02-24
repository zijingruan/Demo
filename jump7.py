#  应用find()方法查验是否包含7
for i in range(1, 101):
    include = str(i).find('7')
    if int(i) % 7 == 0 or include != -1:
        continue
    else:
        print(i)

# 另一种则是判断十位（i//10==7）和个位是否为7(i%10==7)
i = 0
while i < 100:
    i += 1
    if int(i) % 7 == 0 or i // 10 == 7 or i % 10 == 7:
        continue
    else:
        print(i)

