# # 1. 딕셔너리 만들기
# lunch = {
#     '중국집':'02-123-123',
#     '양식집':'054-123-123',
#     '한식집':'031-123-123',
# }

# dinner = dict(중국집='02-123-123')

# # 2. 딕셔너리에 내용 추가하기
# lunch['분식집'] = '053-123-123'

# # 3. 딕셔너리 내용 가져오기
# # print(lunch['중국집']) #=> '02-123-123'
# idol = {
#     'bts': {
#         '지민':24,
#         'RM':25
#     }
# }
# idol['bts'] #=> { '지민':24, 'RM':25 }
# idol['bts']['RM'] #=> 25

# # 4. 딕셔너리 반복문 활용하기
# # 기본 활용
# for key in lunch:
#     print(key) #-> key
#     print(lunch[key]) #-> value

# # key 만 가져오기 : .keys()
# for key in lunch.keys():
#     print(key)

# # value 만 가져오기 : .values()
# for value in lunch.values():
#     print(value)

# # item(key, value) 가져오기 : .items()
# # lunch.items() #=> [('중식,'02-123-123'), ...]
# for key, value in lunch.items():
#     print(key, value)

# # 2개 = 자료형(list, tuble ...) 길이 2
# a, b, c = (1, 2, 3)
# print(a)
# print(b)

# # 문제
# score = {
#     '수학': 80,
#     '국어': 90,
#     '음악': 100
# }
# # 1. 이 학생의 평균을 구하시오.
# s = 0
# for value in score.values():
#     s += value
# print(s / len(score))

# total_score = sum(score.values())
# avg = total_score / len(score)
# print(avg)

# 2. 반 평균을 구하시오
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 70
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# scorelist = list(scores.values())
# s = 0
# a = 0
# for i in range(len(scorelist)):
#     s += sum(scorelist[i].values())
#     a += len(scorelist[i])
# avg = s / a
# print(avg)

# total_score = 0
# count = 0

# for person_score in scores.values():
#     for subject_score in person_score.values():
#         total_score += subject_score
#         count += 1

# avg_score = total_score / count
# print(avg_score)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 6],
    '대전': [-3, -6, 2],
    '광주': [0, -2, 10],
    '구미': [2, -2, 9]
}
# 3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''
for name, temp in city.items():
    print(f'{name} : {round(sum(temp) / len(temp),1)}')