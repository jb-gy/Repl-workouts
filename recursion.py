#recursion
import time

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1) + Fibonacci(idx-2)



print("***** recursion ******")
rec1 = time.time() 
print(Fibonacci(8))
print(f"speed: {time.time()-rec1}")



