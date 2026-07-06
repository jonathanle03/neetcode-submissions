class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.time_map[key]) - 1
        time_idx = -1

        while right >= left:
            mid = (left + right) // 2
            
            if self.time_map[key][mid][0] < timestamp:
                time_idx = mid
                left = mid + 1
            elif self.time_map[key][mid][0] > timestamp:
                right = mid - 1
            else:
                time_idx = mid
                break

        if time_idx == -1:
            return ""
        
        return self.time_map[key][time_idx][1]
        

