
alpha = list(input())

# 첫번째 알파뱃과 두번재 알파뱃이 같은지 확인한다
#       같다면 insert, append로 result배열에 넣는다
#       그리고 index를 +2 증가시켜 다음을 확인한다

# 첫번째 알파뱃과 두번째 알파뱃이 같지 않다면
#       두번째 알파뱃과 세번째 알파뱃이 같은지 확인한다
#               같다면 insert, append로 result배열에 넣는다
#               그리고 index를 +3 증가시켜 다음을 확인한다
#               첫번째 알파뱃을 odd_alpha에 append한다
#               만약 len(odd_alpha) > 1이라면 I'm Sorry Hansoo를 출력한다
#       두번째 알파뱃과 세번째 알파뱃이 같지 않다면
#               I'm Sorry Hansoo를 출력한다

sorted_alpha = sorted(alpha, reverse=True)

odd_alpha = []
index = 2
result = []

while index <= len(sorted_alpha):
    if sorted_alpha[index - 2] == sorted_alpha[index - 1]:
        result.insert(0, sorted_alpha[index - 2])
        result.append(sorted_alpha[index - 1])
        index += 2
    else:
        if sorted_alpha[index - 1] == sorted_alpha[index]:
            result.insert(0, sorted_alpha[index - 1])
            result.append(sorted_alpha[index])
            odd_alpha.append(sorted_alpha[index - 2])
            index += 3
            if len(odd_alpha) > 1:
                print("I'm Sorry Hansoo")
                break
        else:
            print("I'm Sorry Hansoo")
            break

if len(odd_alpha) > 0:
    middle_index = len(result) // 2  # 가운데 인덱스 계산
    result.insert(middle_index, odd_alpha[0])

final = ''.join(map(str, result))

print(final)
