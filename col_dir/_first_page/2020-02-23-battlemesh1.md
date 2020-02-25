---
title: "Battlemesh Part#1"
categories:
  - about
last_modified_at: 2020-02-24T23:25:00:00+09:00
toc: true
---

안녕하세요. Owl Kim 입니다.

이번 포스트는 Battlemesh에 관한 것입니다.

Battlemesh에 대한 설명과 2016년 직접 참여해서 느꼈던 점들을 적어보겠습니다.
(이번 주제는 3번으로 나누어서 진행하겠습니다.)

## Battlemesh란?
Battlemesh는 2009년에 파리에서 첫 행사가 있었고, 매년 1번씩 유럽에서 개최되고 있습니다.

첫 시작은 3개의 Mesh Routing Protocol(BATMAN, BABEL, OLSR) 팀이 모여 서로 우열을 가리기 위해서 모였습니다.

2020년 2월 기준으로 12번의 행사가 진행이 되었고 제가 참석했었던 9회 기준으로 약 20개의 커뮤니티와 100명 정도가 참석하는 큰 행사로 바뀌었습니다.

현재는 초기와 같이 BATMAN(batman_adv, BMX6), BABEL, OLSR, 802.11s와 같은 프로토콜 성능 비교 및
각 커뮤니티 정보 공유, OpenSource 운영 방법 논의 등 서로를 돕는 행사로 발전하였습니다.

네트워크를 조금이라도 다루어 보신 분들이라면 대부분 아시는 OpenWrt도 매년 행사를 참가하고 있습니다.

정리하면 현재는 Mesh Network Community보다는 Network OpenSource Community에 굉장히 가까워 졌습니다.

[battlemesh URL](https://battlemesh.org/)

![poster1](/assets/images/first_page/battlemesh_poster1.png)

![poster2](/assets/images/first_page/battlemesh_poster2.png)


## 참관기
저는 2016년에 개최한 9번째 battlemesh에 참가하였습니다.

한국에서는 모바일 네트워크 기반이 매우 잘 되어있어서 mesh network에 관심도가 낮았고 따라서 이와 관련된 정보를 얻기 힘들었습니다.

우연히 이러한 행사가 있다는 것을 알게 되었고, 등록 기간이 지났지만 운영진에 연락하여 뒤늦게 참가 신청을 하게되었습니다.

2016년 5월 1일부터 7일까지 포르투갈 포르토에서 진행되었고, 주 실험 및 세미나는 Faculty of Engineering, University of Proto에서 진행되었습니다.

![name_tag](/assets/images/first_page/name_tag.jpeg)

![people1](/assets/images/first_page/people1.JPG)

![people2](/assets/images/first_page/people2.JPG)

![router](/assets/images/first_page/router.JPG)

### 일정
![agenda](/assets/images/first_page/WBMv9_Agenda.png)

위와 같이 스케쥴이 정해져 있었고, Collaborative work 시간에는 서로서로 궁금한 점들을 묻고 답하는 친목의 시간이었습니다.

혹시 이 시간에 자신이 하고 있는 프로젝트에 대해서 발표를 하고 싶다면 언제든지 발표를 할 수 있었습니다.

또한 각 프로토콜 테스트를 준비하는 시간이었고, 50대가 넘는 공유기에 직접 프로토콜 구현체를 올리는 작업도 진행하였습니다.

발표 내용에 대해서는 다음 프스트에서 다루겠습니다.

Free Time에는 삼삼오오 모여 맥주를 마시거나 밤새 서로의 코드를 보며 같이 디버깅도 하고 서로의 지식을 나누는 시간이었습니다.

### 숙소
2016년 Battlemesh의 경우 100명이 넘는 사람들이 참가를 하여 주최측에서 2개의 Hostel을 대여하였습니다.

+ Rivoli Cinema Hostel
  + 도시 중심에 있으며, 이동시 Contact Point
  + Early bird들은 대부분 이 곳에서 숙박
+ Porto Spot Hostel
  + 도시 중심과는 조금 떨어져 있으며, 다른 일반 투숙객과 함께 생활
  + 시설은 Cinema보다 좋고 넓음
  + 바로 옆에 사창가가 있어 밤 늦게 돌아다니는 건 위험

저는 늦게 신청을 하였기 때문에 Proto Spot Hostel에서 지냈고, 총 숙박비는 150 EUR였습니다.
(주체측에서 사전 계약 - 150 EUR(Early bird는 125 EUR))

### 식사
아침밥은 각 Hostel에서 제공해주는데 아직도 그 빵 맛을 잊을 수가 없습니다.
간단하게 빵과 잼 쥬스/우유/커피가 제공되었습니다.
![breakfirst](/assets/images/first_page/breakfirst1.JPG)

대부분의 점심은 대학교 학생 식당에서 먹었고, 맛은 그냥 그랬습니다.
![lunch1](/assets/images/first_page/lunch1.JPG) 

![lunch2](/assets/images/first_page/lunch2.JPG)

저녁은 단체로 음식점을 빌려서 먹거나 시내에서 사먹었는데 해산물요리와 맥주는 원없이 먹었습니다.
![dinner1](/assets/images/first_page/dinner1.JPG)

![dinner2](/assets/images/first_page/dinner2.JPG)

![dinner3](/assets/images/first_page/dinner3.JPG)

신기했던 점을 정리해보면
1. 포르투갈은 저녁을 9시에 먹기 시작한다.
2. 유럽인들은 엄마 젖을 떼면 바로 맥주를 먹는다는 얘기(?)가 있다. -> 세미나를 진행하면서도 물 대신 맥주를 마셨다.

## 참여 방법
참여 방법은 간단합니다.

매년 행사를 진행하면서 다음 년도 행사 위치와 날짜를 정합니다.

정해진 장소와 날짜는 battlemesh 홈페이지에 올라오고 온라인으로 신청할 수 있습니다.

한가지 특별한 점은 Travel Scholarship이라는 프로그램이 존재합니다.

혹시 행사에 꼭 참여하고 싶은데 재정적으로 어려우시다면 해당 프로그램에 지원해 보는 것도 좋은 방법일 것입니다.

아래 글은 battlemesh 홈페이지 Travel Scholarship 관련 내용입니다.
```
Thanks to our sponsors, we have the opportunity to provide s
ome Travel Scholarships to cover the costs of a long distance flight to Paris and back. 
If you want to apply, please explicitly tell us so in the registration email. 
Please also provide the location from which you will be coming from, 
an estimation of the travel costs (flight to Paris and back), 
and whether you absolutely need us to cover the full amount of your ticket to be able to participate.

You need to prepare a short video (2 to 5 minutes) in which you briefly present yourself, 
your community and your interests, especially related to the Battlemesh event. 
It should be in either English or French, 
but if you are not fluent enough you can speak in your native language and add English subtitles. 
If you have no easy mean to share large files, 
tell us in your email and we will provide a link to upload your video.
```

혹시 참여하고 싶은데 도움이 필요하시면 언제든지 연락주세요. 제가 도움을 드리도록 하겠습니다.

감사합니다.