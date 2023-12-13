def lenPalindromeOdd(idx, text):
    count = 1
    while((idx-count >= 0) and (idx+count < len(text)) and (text[idx-count] == text[idx+count])):
        count += 1
    return 2*(count-1)+1

def lenPalindromeEven(idx, text):
    count = 0
    while((idx-count >= 0) and (idx+1+count < len(text)) and (text[idx-count] == text[idx+1+count])):
        count += 1
    return (2*count)

text = input()

palindrome = 0
for i in range(len(text)):

    odd = lenPalindromeOdd(i, text)
    even = lenPalindromeEven(i, text)

    if (palindrome < odd):
        palindrome = odd

    if (palindrome < even):
        palindrome = even

print(palindrome)