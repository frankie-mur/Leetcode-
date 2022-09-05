class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         #sort by unitsPbox / numBox'es
#         def calc_units_per_box(num_boxes, boxes_per_unit):
#             return boxes_per_unit / num_boxes
        
#         sorted_ = []
#         for num, units in boxTypes:
#             sorted_.append((calc_units_per_box(num, units), (num, units)))
        
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        max_units = 0
        for boxes, units in boxTypes:
            # boxes, units = truck
            sub = min(boxes, truckSize)
            max_units += (units * sub)
            truckSize -= sub
            if truckSize == 0:
                break
        
        return max_units
            
            
            
            