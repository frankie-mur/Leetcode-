class MovingAverage:

    def __init__(self, size: int):
        self.track = deque([])
        self.cur = 0
        self.window = size

    def next(self, val: int) -> float:
        self.track.append(val)
        self.cur += val
        if len(self.track) > self.window:
            self.cur -= self.track.popleft()
        
        return self.cur / len(self.track)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)