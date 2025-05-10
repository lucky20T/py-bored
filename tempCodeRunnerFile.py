#program to display a message.
#ms=input("enter the message:")
#print(ms)
#Wap in python to take three number as input from user compute average.
'''n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))
n3=int(input("enter the number 3:"))
av=(n1+n2+n3)/3
print("the average:",av)'''
#inputs = input("Enter multiple values separated by space: ").split()

# Printing the inputs
#print("You entered:", inputs)
#4.	Wap in python to check weather the input number is 0,1 or even or odd.
'''n=int(input("enter any number:"))
if n==0:
    print("the number is zero.")
elif n==1:
    print("the number is one.")
elif n%2==0:
    print("the number is even.")
else:
    print("the number is odd.")'''

#Wap in python to print a table of input number using by loop.
'''n=int(input("enter the number:"))
for i in range(1,11):
    print(i,"*",n,"=",i*n)'''
'''import matplotlib.pyplot as plt

# Data for the graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the graph
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = 2x')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')

# Adding a legend
plt.legend()

# Displaying the graph
plt.show()'''
'''#Wap in python to print the  pyramid  of order “n” using for loop.
n=int(input("enter the order n :"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))'''
#Wap in python to initialize a list, add “n” elements in it, sort the list.
l1=[10,20,40,50,90]
n=int(input("enter the number of elements:"))
for i in range(n):
    app=int(input("the element:"))
    l1.append(app)
print("original list:",l1)
l1.sort()
print("sorted list:",l1)
	