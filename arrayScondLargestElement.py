def findSecondLargest(sequenceOfNumbers):
    if len(sequenceOfNumbers)<2:
        return -1
    first = float('-inf')
    second = float('-inf')
    for num in sequenceOfNumbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else -1

