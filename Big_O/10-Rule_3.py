def compress_boxes_twice(boxes, boxes_2):
    for box in boxes: 
        print(box)

    for box in boxes_2: 
        print(box)

boxes = ["box1", "box2", "box3"]
boxes_2 = ["box4", "box5", "box5"]

compress_boxes_twice(boxes, boxes_2)
"""
We have two different inputs!
O(N + M)
"""