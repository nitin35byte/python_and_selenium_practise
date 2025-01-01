def def_position(arr, target):
    start_pos=-1
    end_pos=-1

    for i in range(len(arr)):
        if arr[i] == target:
            if start_pos ==-1:
                start_pos=i
            end_pos=i
    return start_pos , end_pos
target=5
arr = [11 , 12 , 14 , 15, 16, 17, 18]
arr1 = [1 , 2, 3 , 5 ,6  , 7 ,8 ,9]
print(def_position(arr1 , target))