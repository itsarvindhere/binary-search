class SnapshotArray:
    def __init__(self, length: int):
        # At each index, we have a list. And that list will have a pair/tuple with two values -> (snapId, value)
        self.arr = []
        for i in range (length): self.arr.append([(-1, 0)])

        # This is to track the snapId
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snapId, val))
        
    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1
        
    def get(self, index: int, snap_id: int) -> int:
        # The list is sorted already based on the snap_Id
        # So to search for the value at a given index at that time we took snapshot with snap_id
        # we can use Binary Search
        searchList = self.arr[index]
        start = 0
        end = len(searchList) - 1
        index = -1
        
        # We want the rightmost value at an index at which snap_id is <= the snap_id passed in get()
        while start <= end:
            mid = start + (end - start) // 2
            
            # If at mid index, the list has same snap_id as we are looking for
            # It is one possible solution
            # But we want the rightmost value so we keep searching on right side of mid
            if searchList[mid][0] <= snap_id:
                index = mid
                start = mid + 1
            else: end = mid - 1

        
        return 0 if index == -1 else searchList[index][1]


snapshotArr = SnapshotArray(3)

snapshotArr.set(0,5)
snapshotArr.snap();
snapshotArr.set(0,6)
print(snapshotArr.get(0,0))