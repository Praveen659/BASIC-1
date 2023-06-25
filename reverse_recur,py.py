def reverse_digit(arr, l, n=0):
    if n == l:
        return arr
    else:
        arr[n], arr[-1*(n+1)] = arr[-1*(n+1)], arr[n]
    return reverse_digit(arr, l, n + 1)


num = 12345
arr = list(str(num))
print(arr)
arr = reverse_digit(arr, len(arr)//2)

s = ""
print(int(s.join(arr)))