import random

value1 = random.random()
print("Value using random.random() : ", value1)

value2 = random.randint(1000, 9999)
print("An int 4 digit value using random.randint(): ", value2)

inpList = [1, 23, 344, 268, 9809, 7]
value3 = random.choice(inpList)
print("random.choice() from list {} : ".format(inpList), value3)

value4 = random.sample(inpList, 4)
print("random.sample() from list {} for 4 values: ".format(inpList), value4)

print("List before shuffle : {} ".format(inpList))
random.shuffle(inpList) #shuffles original list
print("List after shuffle : {} ".format(inpList))
