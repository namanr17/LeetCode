class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        num_groups = 0
        
        reservedSeats = sorted(reservedSeats, key=lambda x: x[0])
        reservedSeats.append([n+1, 0])
        
        seats_2_to_5 = frozenset((2, 3, 4, 5))
        seats_4_to_7 = frozenset((4, 5, 6, 7))
        seats_6_to_9 = frozenset((6, 7, 8, 9))
        
        def process_seats(reserved_seats):
            if not (seats_2_to_5 | seats_6_to_9) & reserved_seats:
                return 2
            if not seats_2_to_5 & reserved_seats:
                return 1
            if not seats_4_to_7 & reserved_seats:
                return 1
            if not seats_6_to_9 & reserved_seats:
                return 1
            return 0
        
        last_row = 1
        reserved = set()
        
        for seats in reservedSeats:
            if seats[0] != last_row:
                num_groups += (seats[0] - last_row - 1) * 2
                num_groups += process_seats(reserved)
                # print(last_row, num_groups)
                reserved.clear()
                last_row = seats[0]
            reserved.add(seats[1])
        
        return num_groups