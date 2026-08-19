class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0

        l=0
        r=x

        while l<=r:
            mid=(l+r)//2
            midSquare=mid*mid

            if midSquare>x:
                r=mid-1
            
            else :
                ans = mid
                l=mid+1

        return ans
        