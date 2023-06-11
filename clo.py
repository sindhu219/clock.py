import datetime
import time
import winsound

def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            print("Alarm!! Time to get up")
            for i in range(5):
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

print("Set alarm in 24 hour HH:MM:SS format")
alarm_time=input("Enter the alarm time: ")
