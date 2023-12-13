import time
from datetime import datetime, timedelta

import requests

# 봇 토큰을 입력하세요. ⚠️유출 주의⚠️
bot_token = "5742885964:AAH2Wi0XvA_kRxoFSb1oz5mLTavqmXczN2g"
# 글특임시방
# 대상 채팅 ID를 입력하세요.
# chat_id_ny_7 = ['-805305317'] #-805305317 남영7 예배방 / -4031054537 메인 테스트방
# telegram room id where we reserve the mesages
chat_id_ny = ["-1001738071140"]  # 남영1, 남영2, 남영3, 남영5, 남영6, 남영7
# chat_id_hg = ['-929608682', '-994984369', '-959749001'] #테스트123 - 한강

# 원하는 년도를 설정합니다.
desired_year = "40"

# 현재 날짜와 시간을 가져옵니다.
current_date = datetime.now()

# 원하는 년도로 날짜를 변경합니다.
current_date = current_date.replace(year=int(desired_year))

# 날짜를 원하는 형식으로 포맷팅합니다. (예: YYYY-MM-DD)
newdate = current_date.strftime(f"{desired_year}%m%d")

# 보낼 메세지 내용을 입력하세요.
message4 = f"""
☁️{newdate} 14시 예약문자 보냅니다.
"""

message1 = f"""
☁️{newdate} 주일예배 사전 출결☁️

- 남영 7 00/11

* 실시간대면(오전/오후 통합)예배참여자(이름/인증/필기) 00/11

* 실시간온라인참여자(이름/인증/필기) 00/11

* 개별(이름/사유/개인예배시간) 00/11

* 미취합자
임승환 이정민 이지선 최수정 김소정 박지수 송주영 박선경 유정민 유창혁 오주은
"""

message2 = f"""
💕

예배 취합 부탁드립니다!

💕
"""

message3 = f"""
💗💗💗💗💗💗

예배 취합 아직 안하셨다면 예배 취합 부탁드립니다!

💗💗💗💗💗💗

"""

message_notice = f"""
✨ 오늘은 예배날 🔖

안녕하세요 예배 알리미 남산이예요 🏔️😆

오늘은 영들과 하나되어 말씀으로 나를 씻는 시간이예요! 한 번 마음내서 준비해볼까요?

그리고 예배 후 꼭 '인증!' 부탁드릴게요 :)

그럼 예배때 봐요~~!

도예시 🛬
예배 인증 🤳
구님과 소통 💕 
나를 씻는 소중한 시간 🐳
저는 예배 알리미 남산이 🏔️

"""

# 📣 [예배 출결 취합] 📣
# 요일별 예약 시간 설정 (예약 시간을 계산식으로 지정)
# 예: 월요일 12시 0분 0초

# 출결 취합용 예약 문자
scheduled_times1_2 = {
    0: datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)  # 월요일
}
scheduled_times1 = {
    3: datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)  # 목요일
}

# 출결 취합 안한 인원 독려용 예약 문자
scheduled_times2 = {
    # 0: datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),  # 월요일
    1: datetime.now().replace(hour=2, minute=0, second=0, microsecond=0),  # 화요일
    2: datetime.now().replace(hour=2, minute=0, second=0, microsecond=0),  # 수요일
    # 3: datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),  # 목요일
    4: datetime.now().replace(hour=10, minute=30, second=0, microsecond=0),  # 금요일
    5: datetime.now().replace(hour=10, minute=30, second=0, microsecond=0),  # 토요일
    # 6: datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)   # 일요일
}

# 텔레그램 봇 API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# 예약 메시지를 보내는 함수
while True:

    def send_scheduled_message(message, chat_id, scheduled_time):
        current_time = datetime.now()
        if current_time < scheduled_time:
            time_difference = scheduled_time - current_time
            time.sleep(time_difference.total_seconds())

            # for chat_id in chat_id_ny_7: #남영7
            #     data = {'chat_id': chat_id, 'text': message}
            #     response = requests.post(url, data=data)
            #     if response.status_code == 200:
            #         print(f"[남영7] 예약 메시지가 성공적으로 보내졌습니다.")
            #     else:
            #         print(f"예약 메시지 보내기 실패: [남영7] {response.status_code}")

            for chat_id in chat_id_ny:  # 남영
                data = {"chat_id": chat_id, "text": message}
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    print(f"[남영 테스트] 예약 메시지가 성공적으로 보내졌습니다.")
                else:
                    print(f"예약 메시지 보내기 실패: [남영] {response.status_code}")

            # for chat_id in chat_id_hg: #한강테스트
            #     data = {'chat_id': chat_id, 'text': message}
            #     response = requests.post(url, data=data)
            #     if response.status_code == 200:
            #         print(f"[한강 테스트] 예약 메시지가 성공적으로 보내졌습니다.")
            #     else:
            #         print(f"예약 메시지 보내기 실패: [한강] {response.status_code}")
        else:
            print(f"예약 시간이 이미 지났습니다. 메시지가 보내지지 않았습니다.")
            time.sleep(1)

    # 현재 요일을 가져오는 함수
    def get_current_weekday():
        return datetime.now().weekday()

    # 현재 요일에 해당하는 예약 메시지 보내기
    current_weekday = get_current_weekday()
    if current_weekday in scheduled_times1_2:  # 수요예배
        scheduled_time = scheduled_times1_2[current_weekday]
        print(f"[1번 - 수요예배] 그룹 메세지 전송하는 곳에 도착했습니다. 예약 발송을 기다립니다.")
        # send_scheduled_message(message4, chat_id_ny_7, scheduled_time), #남영7
        send_scheduled_message(message4, chat_id_ny, scheduled_time),  # 남영
        # send_scheduled_message(message2, chat_id_ny, scheduled_time), #남영
        # send_scheduled_message(message4, chat_id_hg, scheduled_time), #한강 테스트
        # send_scheduled_message(message2, chat_id_hg, scheduled_time) #한강 테스트
        print(f"[1번] 그룹 메세지 전송 완료되었습니다.")
    else:
        print("오늘은 예약된 메시지를 보낼 요일이 아닙니다. [1번] 수요예배 그룹 메세지")

    if current_weekday in scheduled_times1:  # 주일예배
        scheduled_time = scheduled_times1[current_weekday]
        print("[1번 - 주일예배] 그룹 메세지 전송 완료되었습니다.")
        # send_scheduled_message(message1, chat_id_ny_7, scheduled_time) #남영7
        # send_scheduled_message(message2, chat_id_ny_7, scheduled_time) #남영7
        send_scheduled_message(message1, chat_id_ny, scheduled_time)  # 남영
        send_scheduled_message(message2, chat_id_ny, scheduled_time)  # 남영
        # send_scheduled_message(message1, chat_id_hg, scheduled_time) #한강 테스트
        # send_scheduled_message(message2, chat_id_hg, scheduled_time) #한강 테스트
        print("[1번] 그룹 메세지 전송 완료되었습니다.")
    else:
        print("오늘은 예약된 메시지를 보낼 요일이 아닙니다. [1번] 주일 예배 그룹 메세지")

    if current_weekday in scheduled_times2:
        scheduled_time = scheduled_times2[current_weekday]
        send_scheduled_message(message_notice, chat_id_ny, scheduled_time)  # 남영
        # send_scheduled_message(message_notice, chat_id_hg, scheduled_time) #한강 테스트
        print("[2번] 그룹 메세지 전송 완료되었습니다.")
    else:
        print("오늘은 예약된 메시지를 보낼 요일이 아닙니다. [2번] 그룹 메세지")
pass  # 이 줄은 루프를 종료하지 않기 위해 필요합니다.
