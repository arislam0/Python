n = input("Enter a text of number: ")
list = n.split()
sum =0

for num in list:
    sum = sum + int(num)
print(sum)
print()

numOfWords =0
numOfLetters =0
numOfDigits =0

text = input("Enter a text of numbers 2nd: ")
for x in text:
    x=x.lower()
    if x >= 'a' and x <='z':
        numOfLetters = numOfLetters+1
    elif x>='0' and x<='9':
        numOfDigits = numOfDigits+1
    elif x==' ':
        numOfWords = numOfWords+1

print(numOfWords+1)
print(numOfDigits)
print(numOfLetters)