class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        res,i = 0,0
        while truckSize > 0:
            #print(i)
            boxes,units = sorted_box[i]
            #print(truckSize)
            #print(sorted_box)
            if truckSize >= boxes:
                res += (boxes * units)
                truckSize -= boxes
                i += 1
            else:
                res += (truckSize * units)
                truckSize = 0
            if i == len(sorted_box):
                break
            
        return res