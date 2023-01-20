# from collections import Counter

# def solution(k, tangerine):
#     answer = 0
#     sum = 0
#     tan = Counter(tangerine).most_common()
    
#     for t in tan:
#         sum += t[1]
#         answer += 1
#         if sum >= k:
#             return answer
    
#     return answer


import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    # print(cnt)
    # Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1})
    # print(sorted(cnt.values(), reverse = True))
    # [2, 2, 2, 1, 1]
    

    for v in sorted(cnt.values(), reverse = True):
        print(v)
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer


from collections import Counter

def solution(k, tangerine):
    answer = 0
    # [1] 자료 변환 
    count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])
    # [2] 최소 종류 계산
    for key, value in count:
        if k <= 0: break
        k -= value
        answer += 1
    return answer


k = 6
tangerine = [1,3,2,5,4,5,2,3]
print(solution(k, tangerine))