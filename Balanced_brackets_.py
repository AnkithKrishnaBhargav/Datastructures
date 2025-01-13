
def isBalanced(s):
    
    stack=[]
    pairs={'(':')','{':'}','[':']'}
    for char in s:
        if char in list(pairs.keys()):
            stack.append(char)
        elif char in list(pairs.values()):
            if not stack or pairs[stack.pop()]!=char:
                return "NO"
    return "YES" if not stack else "NO"
    
number=int(input())
for strings in range(number):
    s=input()
    print(isBalanced(s))
    