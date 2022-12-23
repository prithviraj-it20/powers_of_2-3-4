Problem link 1 (power of 2): https://leetcode.com/problems/power-of-two/ 
Problem link 2 (power of 3) : https://leetcode.com/problems/power-of-three/
Problem link 3 (power of 4): https://leetcode.com/problems/power-of-four/


Solution for problem1:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<1):
            return 0
        else:
            while(n!=1):
                if(n%2==0):
                    n=n//2
                else:
                    return 0
            return 1
      
      
Solution for problem2:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<1):
            return 0
        else:
            while(n!=1):
                if(n%3==0):
                    n=n//3
                else:
                    return 0
            return 1
        
Solution for problem3:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<1):
            return 0
        else:
            while(n!=1):
                if(n%4==0):
                    n=n//4
                else:
                    return 0
            return 1
      
      
