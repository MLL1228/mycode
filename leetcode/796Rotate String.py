class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A) != len(B):
            print('111')
            return False

        if not A and not B:
            print(111)
            return True

        for i in range(len(A)):
            if A[i] == B[0]:
                flag = True
                for j in range(len(B)):
                    if j <= len(A)-1-i:
                        if B[j] != A[i+j]:
                            flag = False
                            break
                    else:
                        if B[j] != A[j - (len(A)-1-i) + 1]:
                            # print(B[j], A[len(A)-1-i])

                            break
                if flag:
                    return True

        return False


s = Solution()
A=''
B=''
print(s.rotateString(A,B))







