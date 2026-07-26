class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set()
        visited = set()
        for num in deadends:
            dead.add(num)
        q = deque()
        if "0000" in dead:
            return -1
        q.append(('0000',0))
        up = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9","9":"0"}
        down = {"0":"9","1":"0","2":"1","3":"2","4":"3","5":"4","6":"5","7":"6","8":"7","9":"8"}
        while q:
            cur,count = q.popleft()
            for i in range(4):
                temp = cur
                temp = temp[:i] + up[temp[i]] + temp[i+1:]
                if temp == target:
                    return count + 1
                if temp not in dead and temp not in visited:
                    visited.add(temp)
                    q.append((temp,count+1))
                temp = cur
                temp = temp[:i] + down[temp[i]] + temp[i+1:]
                if temp == target:
                    return count + 1
                if temp not in dead and temp not in visited:
                    visited.add(temp)
                    q.append((temp,count+1))
        return -1
