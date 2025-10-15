def is_palindrome(N:int, left:int, right:int) ->bool:
  # Base case
  if left >= right:
    return True
  
  if N[left] != N[right]:
    return False
  
  # Recursive call for inner substring
  return is_palindrome(N, left + 1, right - 1)

Number1 = "523"
Number2 = "121"

print(f"{Number1} -> Palindrome ? {is_palindrome(Number1, 0, len(Number1)-1)}")
print(f"{Number2} -> Palindrome ? {is_palindrome(Number2, 0, len(Number2)-1)}")