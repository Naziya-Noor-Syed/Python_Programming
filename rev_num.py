num = 12345
reverse_num = 0
while num!=0:
    digit = num%10
    reverse_num = reverse_num*10 +digit
    digit = num//10
print("reversed number:", reverse_num)