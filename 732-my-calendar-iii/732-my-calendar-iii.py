from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.events = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1 
        
        ret = curr = 0
        for val in self.events.values():
            curr += val
            ret = max(ret, curr)
            
        return ret

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)