# Day 02

## Git  설정

* `git config --global user.name 'ysw'`
* `git config --global user.email 'bearsgod@gmail.com'`

* `git init` : git 초기화, git으로 관리하겠다!
* `git remote add origin 주소` : 원격 저장소 등록
  * `git remote set-url origin 주소` : 원격 저장소 수정



## Git Commit & Push

* `git status` : 현재 폴더의 git의 상태
* `git add .` : 현재 폴더의 변경사항들을 commit하기 위해서 준비
* `git commit -m 'day 02입니다'` : commit, 변경 사항 저장, 메세지는 자유롭게 작성 가능
* `git push -u origin master` : remote로 등록된 원격 저장소(remote repository)
  * 이후에는 `git push` 만 입력해도 동작합니다.



* Markdown 기록할 것입니다.
  * typora or VSCode
* GitHub Student Developer Pack



## 파일 조작

```python
with open('파일 이름', 'r, w, a') as 변수:
    f.write('뭐시기뭐시기')
```

* day02 보고 알아보자
* list.reverse()는 원래 리스트 뒤집기, reversed(리스트)는 반환



## CSV

* csv 모듈 써서 엑셀 파일 마냥 쓸 수 있다
* write, read 할 때 csv 형식 파일에 대해 좀 더 쉽게 프로그래밍 가능



## 웹 크롤링

* request, bs4 모듈 사용
* request로 겟 못 받으면 헤더 딕셔너리 형식으로 끌고 와서 추가
* 태그, .클래스 등으로 셀렉터 설정
* 나눠서 하든 걍 하든 text로 태그 벗겨서 내용만 잘 써먹자