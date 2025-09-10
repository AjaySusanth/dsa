# https://leetcode.com/problems/sum-of-subarray-minimums/submissions/1759723321/

class Solution(object):
    def find_nse(self,arr):
        n = len(arr)
        nse = [0]*n
        st=[]
  
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            nse[i] = st[-1] if st else n
            st.append(i)
        return nse

    def find_pse(self,arr):
        n = len(arr)
        nse = [0]*n
        st=[]

        for i in range(0,n):
            while st and arr[st[-1]]> arr[i]:
                st.pop()
            nse[i] = st[-1] if st else -1
            st.append(i)
        return nse
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        nse = self.find_nse(arr)
        pse = self.find_pse(arr)
        n = len(arr)
        total=0
        for i in range(0,n):
            left = i - pse[i] 
            right = nse[i] - i
            total =(total + left*right*arr[i]) % MOD
        return total
        