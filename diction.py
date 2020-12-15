fruit = ["사과", "사과", "바나나", "바나나", "딸기", " 키위", "복숭아", "복숭아", "복숭아"]
print(fruit)
d = {}

for f in fruit:
  if f in d:
    d[f] = d[f] + 1
  else:
    d[f] = 1
print(d)
sd = sorted(d.items(),key=lambda x: x[1], reverse = True)

print(sd)
for x,y in sd:
  print(y)