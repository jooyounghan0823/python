

#target = "onetwothreefourfivesixseveneightnine"
#numList = ['zero','one','two','three','four','five','six','seven','eight','nine']
#for index,item in enumerate(numList):
    #if item in target:
        #target = target.replace(item, str(index))
#print(target)



target = "onetwothreefourfivesixseveneightnine"
numList = ['zero','four','five','six','seven','eight','nine']
for index,item in enumerate(numList):
    if item in target:
        target = target.replace(item, str(index))
print(target)


