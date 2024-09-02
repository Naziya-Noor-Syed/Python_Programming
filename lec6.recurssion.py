#recurssive method

def show(n):
    if(n==0):
        return
    print(n, end=" ")
    show(n-1)
show(5)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)