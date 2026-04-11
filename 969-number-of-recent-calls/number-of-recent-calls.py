class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        time = [t-3000,t]
        self.q.append(t)
        while self.q and self.q[0] < time[0]:
                self.q.popleft()
        return len(self.q)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)