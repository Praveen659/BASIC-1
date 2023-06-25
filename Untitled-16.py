def palindrome(str):
    for i in range(len(str)-1):
        if str[i] !=str[len(str)-i-1]:
            return False
        return True
str="civical"
print(palindrome(str))