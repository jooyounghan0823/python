#iphoneList = ['iphone13','iphone14','iphone15']
#iphonePriceList = [10,20,30]
#zip(지퍼)
#print(list(zip(iphoneList,iphonePriceList)))

#print([{'아이폰':phone,'가격': price} for phone, price in zip(iphoneList, iphonePriceList}])

#alpha = ['a','b','c','d','e']
#number = [1,2,3,4,5]

#print([{'알파벳':a,'순서':n} for a,n in zip(alpha,number) ])



text = "apple banana apple strawberry banna"
wordList = text.split()
wordLenList = list(map(lambda x:len(x), wordList))
print([{'단어':word,'글자 수':length} for word, length in zip(wordList,wordLenList)])




