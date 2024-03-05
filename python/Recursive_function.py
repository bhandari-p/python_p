# foctorial using recursive function

a=int(input("Enter a number:"))

def fact(a):
  if a==0 or a==1:
    return 1

  else:
    return a * fact(a-1)

# # fibonacci seres 
# # Python program to display the Fibonacci sequence

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))

  
