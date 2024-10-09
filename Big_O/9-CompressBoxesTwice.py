def compress_boxes_twice(boxes):
    for box in boxes: # O(N)
        print(box)

    for box in boxes: # O(N)
        print(box)

boxes = ["box1", "box2", "box3"]
compress_boxes_twice(boxes)
 # N + N = 2N --> N