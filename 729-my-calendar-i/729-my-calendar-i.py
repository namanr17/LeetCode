class MyCalendar:
    def __init__(self):
        # self.calendar = []
		# Use Linked List instead, much more faster
        self.calendar = collections.deque()

    def book(self, start: int, end: int) -> bool:
        right = len(self.calendar)
        if right == 0:
            self.calendar.append((start, end))
            return True

        left = 0
        while left < right:
            mid = int(left + (right - left)/2)
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == 0:
            if self.calendar[left][0] >= end:
                self.calendar.insert(0, (start, end))
                return True
            else:
                return False
        elif left == len(self.calendar):
            if self.calendar[left - 1][0] <= start:
                self.calendar.append((start, end))
                return True
            else:
                return False
                
        if left - 1 >= 0 and self.calendar[left - 1][1] <= start and self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True
            
        return False