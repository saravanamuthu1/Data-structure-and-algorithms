import random
class Quickselect:
    def findKthelem(self,arr,k) -> None:
        self.arr = arr
        self.k = k
        return self.quick_select(0, len(self.arr)-1)
    def partition(self,low, high):
        partition_index = random.randint(low,high)
        pivot = self.arr[partition_index]
        self.arr[partition_index], self.arr[high] = self.arr[high], self.arr[partition_index]
        i = low
        for j in range(low, high):
            if self.arr[j] <= pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i = i+1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i
    def quick_select(self,low,high):
        if low == high:
            return self.arr[low]
        value = self.partition(low,high)
        if value == self.k:
            return self.arr[self.k]
        elif value > self.k:
            return self.partition(low,value-1)
        else:
            return self.partition(value+1,high)
if __name__ == "__main__":
    arr = [3,1,7,8,40,100,35,20,200]
    obj1 = Quickselect()
    print(obj1.findKthelem(arr,2))