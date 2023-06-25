def palindrome(str):
    for i in range(len(str)):
        if str[i] !=str[len(str)-i-1]:
            return False
        return True
str="civic"
print(palindrome(str))
