
alpha = list(input())

# 알파벳 문자열을 정렬한다
# 정렬된 list를 앞에서 부터 하나씩 확인하며서 각각의 list에 집어넣는다
# 만들어진 이중 list를 순회하며 len를 구하며 odd를 count한다
# 만약 odd > 1이면 I'm sorry Hansoo를 출력한다
# 만약 odd =< 1 이면 펠린드롬을 제작한다
#       odd list가 있다면 해당 list를 제외하고 각각 배열의 절반을 가져온다
#               절반을 result list에 append하고 odd를 append한 뒤 절반 result를 역순으로 append한다
#       odd list가 없다면 각각 배열의 절반을 가져온다
#               절반을 result list에 apeend하고 뒤집어서 한번 더 append해준다

sorted_alpha = sorted(alpha)

divided_alpha = []


odd_count = 0
odd_list = []
even_list = []

# 정렬된 알파뱃 list 각 요소별로 이중리스트 분류
for item in sorted_alpha:
    found = False
    for sublist in divided_alpha:
        if item in sublist:
            sublist.append(item)
            found = True
            break
    if not found:
        divided_alpha.append([item])
# print(divided_alpha)

flag = False
# odd count하고 1초과 시 I'm sorry Hansoo 출력
for sublist in divided_alpha:
    if len(sublist) % 2 != 0:
        odd_count += 1
        if odd_count > 1:
            flag = True
            print("I'm Sorry Hansoo")
            break
        odd_list.append(sublist)
    else:
        even_list.append(sublist)
# print(even_list, odd_list)

result = ""
half_even = ""
half_odd = ""

if not flag:
    # odd가 1개일 경우
    if odd_count == 1:
        for sublist in even_list:
            half_index = len(sublist) // 2
            half_even += "".join(map(str, sublist[:half_index]))
        for sublist in odd_list:
            half_index = len(sublist) // 2
            half_odd += "".join(map(str, sublist[:half_index]))

        result = "".join(map(str, sorted(half_even + half_odd)))
        reverse_result = result[::-1]
        result += "".join(odd_list[0][0])
        result += "".join(reverse_result)
        print(result)
    # odd가 0개일 경우
    else:
        for sublist in even_list:
            half_index = len(sublist) // 2
            half = sublist[:half_index]
            result += "".join(half)
        reverse_result = result[::-1]
        result += "".join(reverse_result)
        print(result)
