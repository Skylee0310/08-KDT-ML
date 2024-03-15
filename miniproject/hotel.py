from joblib import load

mdl = load('hotel_df.pkl')


# 로딩된 모델 확인
print(mdl.classes_)

# 사용자로부터 입력 받기
deposit_type = int(input('보증금 타입을 입력하세요. (no deposite이면 0, Non Refund이면 1, Refundable이면 2): ')) 
required_car_parking_spaces = int(input('고객이 필요한 주차장 공간 수를 입력하세요. : ')) 

previous_cancellations = int(input('이전 예약 취소 건수 :'))
assigned_room_type = int(input('제공된 방 유형 :'))
adr = int(input('일평균 숙박요금 :' ))

is_repeated_guest = int(input('이전에 방문한 적 있는 손님이면 1, 아니면 0'))
total_of_special_requests = int(input('추가요청 사항 :'))
lead_time = int(input("예약 후 대기 일수를 입력하세요: "))

arrival_week = int(input("도착 주의 주차를 입력하세요: "))
booking_changes =  int(input('예약변경/수정 횟수'))

# 입력된 데이터로 예측
input_data = [[deposit_type, required_car_parking_spaces, previous_cancellations, 
               assigned_room_type, adr, is_repeated_guest, total_of_special_requests, 
               lead_time, arrival_week, booking_changes]]

prediction = mdl.predict(input_data)


if prediction == 1:
    print("예약이 취소될 것으로 예측됩니다.")
else:
    print("예약이 유지될 것으로 예측됩니다.")