# str="sivani  des Unbou"
# # count=0
# # for i in str:
# #     if i==" ":
# #         count=count+1
# # print(count)

# ls=[i for i in str if i==" "]
# print(len(ls))

# str="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# letters=[letter for letter in str if letter not in "'a','e','i','o','u',' '"]
# print(letters)
sent="i am 18 and 4"
word=sent.split()
number=[num for num in word if  not num.isalpha()]
print(number)