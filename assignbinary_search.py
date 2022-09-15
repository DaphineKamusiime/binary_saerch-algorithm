def binary_search(array,value):
    first=0##index of the first value in the array
    last=len(array)-1##index of the last value in the array
    while first<=last:
        mid=int((first+last)/2)
        if value==array[mid]:
            return True
        elif value<array[mid]:
            last=mid-1
        else:
            first=mid+1
    return False
list=[31,41,59,26,41,58]
value1=55##value being searched for
print(binary_search(list,value1))
        