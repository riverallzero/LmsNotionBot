# < 2022 Final Project >
## LMS로 강의를 들을 때 놓치는 영상, 레포트, 퀴즈를 알려주기위한 알림 봇 🤖

<li>프로젝트 명: Lms Notion
<li>프로젝트 기간: 2022-05-23~2022-06-10

***
  
### Information
  
이 프로젝트는 텔레그램 봇(@LmsNotion_bot)에 ‘할 일’이라고 보내면 강의영상, 레포트, 퀴즈의 리스트를 자동으로 탐색한다. 셀레니움을 통해 정보를 가져오고, 봇을 이용해 하지 않은 것들은 제목과 함께 링크를 첨부하며 하라고 알려주고, 모두 했으면 완료했다고 메세지를 보내준다.
  
***
  
### Description
#### [ 코드를 사용하기 위해 변경해야할 것 ]
#### 1. lecfinder.py
 - 강의의 고유한 group_id를 주소창에서 찾아 groupid_lec에 입력해야한다.
   group_id 주소창 제일 마지막에 5자리 숫자로 존재한다.
 - 본인의 LMS 아이디와 비밀번호를 입력해야한다.
```swift
self.groupid_lec1 = 강의 group_id(5자리수)
self.groupid_lec2 = 강의 group_id(5자리수)

self.lms_id = 'LMS 로그인 아이디'
self.lms_pw = 'LMS 로그인 비밀번호'
```
#### 2. notiontelegrambot.py
  - 본인의 텔레그램 채팅 아이디를 입력해야한다.
  ```swift
  self.telegramid = '텔레그램 채팅 아이디'
  ```

***
  
### Result
1. 먼저 봇을 검색해 '할일'이라고 치면 Selenium이 실행될 동안 '로딩중'이라는 메세지가 발송된다.
2. 탐색을 마치면, 결과를 사용자에게 보낸다. 
   해야할 일이 남았다면 그 카테고리의 이름과 기한, 링크를 첨부해 메세지를 보내고, 다 했다면 각 카테고리 별로 완료라는 메세지를 보낸다.

<img src="https://user-images.githubusercontent.com/93754504/172797318-4e0d7af0-8833-4814-90a9-2509c5ab0ea7.png"  width="570" height="600"/>

#### 시연 동영상
<li>텔레그램 봇 시연: https://user-images.githubusercontent.com/93754504/172798687-c3c27d34-8102-448d-a7bc-cab8e86bbf4d.mp4
<li>셀레니움 시연: https://user-images.githubusercontent.com/93754504/172567138-5b5005f5-4d11-4b4b-94df-f422c5d5bc4a.mp4

***

### Source
<li>텔레그램 봇 만들기 참고<br>
- https://py-son.tistory.com/8
<li>크롤링 참고<br>
- https://yeo0.github.io/data/2018/09/24/5.-%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%9D%B4-%ED%95%84%EC%9A%94%ED%95%9C-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%97%90%EC%84%9C%EC%9D%98-%ED%81%AC%EB%A1%A4%EB%A7%81/ <br>
- https://hi-guten-tag.tistory.com/11?category=1256065
<li>Html Xpath 참고<br>
- https://velog.io/@mjhuh263/TIL-23-HTML-XPATH-%EB%AC%B8%EB%B2%95%EA%B3%BC-selenium%EC%97%90-XPATH-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0
<li>Html Css Selector 참고<br>
- https://www.nextree.co.kr/p8468/
<li>isinstance 함수 참고<br>
- https://blockdmask.tistory.com/536
