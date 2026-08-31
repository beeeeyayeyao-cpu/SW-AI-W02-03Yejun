"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""


"""Hoare 기법에 따라 피벗을 기준으로 정렬하고, 반으로 쪼갤 기준이 되는 인덱스 반환"""
def partition(arr, low, high): 

    pivot = arr[(low + high) // 2] #피벗 정의 리스트의 가운데 값

#low(start) 가 high(end) 보다 같거나 작은동안 반복 (start와 end가 서로 교차되지 않은동안 반복)
    while (low <= high): 
        while(arr[low] < pivot): #low(start) 번지 값이 피벗보다 작은동안 오른쪽으로 계속 진행
            low += 1 
        while(arr[high] > pivot): #high(end) 번지 값이 피벗보다 큰동안 왼쪽으로 계속 진행
            high -= 1
        if (low <= high): #while 문을 빠져나온 시점. 피벗 하는 상태이므로 값 교체
            temp = arr[high]
            arr[high] = arr[low]
            arr[low] = temp
            low += 1
            high -= 1

    return low

"""재귀 호출로 퀵 정렬을 실행하는 함수"""
def quick_sort_helper(arr, low, high):
    pivotIndex = partition(arr, low, high) 
    if (pivotIndex-1 > low): #왼쪽으로 더 계산할 수 있는지 확인
        quick_sort_helper(arr, low, pivotIndex-1) #왼쪽 리스트 계산
    if (pivotIndex < high): #왼쪽 계산을 더 이상 못한다면 오른쪽으로 계산할 수 있는지 확인
        quick_sort_helper(arr, pivotIndex, high)  #오른쪽 리스트 계산

    

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")


