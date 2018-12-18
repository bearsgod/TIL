import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response,'html.parser')
result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')
for item in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one(' .ah_k').text
    print(f'{rank} / {keyword}')


# for item in result:
#     st = item.text.strip().split('\n')
#     print(f'{st[0]}위는 \'{st[1]}\' 입니다')

# rank = soup.select('.ah_l > .ah_item > .ah_a > .ah_r')
# name = soup.select('.ah_l > .ah_item > .ah_a > .ah_k')

# for i in range(20):
#     r = rank[i]
#     n = name[i]
#     print(f'{r.text}위는 \'{n.text}\' 입니다')