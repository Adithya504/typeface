class Solution:
   def solve(self, n):
      n = abs(n)
      if n < 3:
         return str(n)
      s = ''
      while n != 0:
         s = str(n%3) + s
         n = n//3
      return s
ob = Solution()
x=int(input())
print(ob.solve(x))
