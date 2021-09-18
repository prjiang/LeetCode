'''
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.

Input: arr = [0,0,0,0]
Output: "00:00"

Input: arr = [0,0,1,0]
Output: "10:00"

Constraints:
    arr.length == 4
    0 <= arr[i] <= 9
'''
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if(sum(arr)==0):
            return "00:00"
        li = ['0','0']
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if(i != j and i != k and i != l and j != k and j != l and k != l):
                            h = str(arr[i]) + str(arr[j])
                            m = str(arr[k]) + str(arr[l])
                            if(int(h) < 24 and int(m) < 60):
                                if(int(h) > int(li[0]) or (int(h) == int(li[0]) and int(m) > int(li[1]))):
                                    li = [h,m]
        if ((int(li[0]) + int(li[1])) == 0):
            return ""
        else:
            return li[0] + ':' + li[1]