 #A program which repeatedly reads numbers until the user enters "done". Once 
 #"done" is entered, print out the total, count, and average of the numbers. If
 #the user enters anything other than a number, detect their mistake using try
 #and except and print an error message and skip to the next number.

count = 0
total = 0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + number

print("All Done")
print(count, total, total/count)
