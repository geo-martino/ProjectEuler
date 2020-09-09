# Find the sum of all the multiples of 3 or 5 below 1000

# Generate variables to sum multiples 3 and 5
# Generate variable to detract duplicate variables
def main():
    sum3 = 0
    sum5 = 0
    sumsub = 0

    # Add multiples to respective variable
    for n in range(3, 1000, 3): # All multiples of 3
        #print(n)
        sum3 += n
    print("sum3 =",sum3)

    for n in range(5, 1000, 5): # All multiples of 5
        #print(n)
        sum5 += n
    print("sum5 =",sum5)

    for n in range(15, 1000, 15):   # All duplicate multiples
        #print(n)
        sumsub += n
    print("sumsub =",sumsub)

    # Sum  = 3multiples + 5multiples - duplicate multiples
    # Return answer
    sum = sum3 + sum5 - sumsub
    print("sum =",sum)

if __name__ == "__main__":
	main()

"""Model solution"""
numbers = 0
for i in range(1000):
    if i%3 == 0:
        numbers += i
    elif i%5 == 0:
        numbers += i
print(numbers)