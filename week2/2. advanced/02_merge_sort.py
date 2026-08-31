"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""

"""(개념적으로)두개의 배열의 인덱스 값을 서로 비교하면서 작은 순대로 배열에 등록"""
def merge(arr, left, mid, right):
    temp = arr.copy() #새로운 배열 생성, 값이 같이 변하면 안되므로

    party1 = left #왼쪽 배열의 현제 인덱스
    party2 = mid+1 #오른쪽 배열의 현제 인덱스
    index = left #값이 등록될 배열의 현제 인덱스

    #첫번째나 두번째 배열의 인덱스를 모두 서치 못한 동안 반복 
    while (party1 <= mid and party2 <= right):
        #두 배열의 현제 인덱스의 값을 비교해서 첫번째 배열의 값이 더 작다면
        if (temp[party1] <= temp[party2]):
            arr[index] = temp[party1] #첫번째 배열의 현제 인덱스 값을 등록 
            party1+=1
        else:
            arr[index] = temp[party2] #두번째 배열의 현제 인덱스 값을 등록
            party2+=1
        index += 1

    #위에서 등록을 못한 값들을 모두 등록
    for i in range(0, mid - party1 + 1): 
        arr[index] = temp[party1 + i]
        index+=1
    for i in range(0, right - party2 + 1):
        arr[index] = temp[party2 + i]
        index+=1

"""재귀호출로 머지 정렬을 실행하는 함수"""
def merge_sort_helper(arr, left, right):

    if (left < right): #시작 인덱스가 끝 인덱스보다 작으면(현제 배열의 크기가 1보다 크다면)
        mid = (left + right) // 2 #중간 인덱스 구하기
        merge_sort_helper(arr, left, mid) #왼쪽 배열 생성하는 재귀함수 호출
        merge_sort_helper(arr, mid + 1, right) #오른쪽 배열 생성하는 재귀함수 호출
        merge(arr, left, mid, right) 


def merge_sort(arr):
    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")
