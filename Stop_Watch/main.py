from playsound3 import playsound
import time

# ANSI values used to clear console screen and then return it
CLEAR_SCREEN = "\033[2J"
CLEAR_SCREEN_RETURN = "\033[H"

def stop_watch(seconds):
    time_counter = 0
    print(CLEAR_SCREEN) # clears the console screen
    while time_counter < seconds:   
        time.sleep(1)
        time_counter += 1
        total_time_left = seconds - time_counter
        timeleft_minutes = total_time_left // 60
        timeleft_seconds = total_time_left % 60
        print(f"{CLEAR_SCREEN_RETURN} Total time left (mm:ss): {timeleft_minutes:02d}:{timeleft_seconds:02d}")

    playsound('ringtone.mp3') # plays ringer when time is up

minutes_input = int(input("Enter how many minutes? "))
seconds_input = int(input("Enter how many seconds? "))

min_to_sec = minutes_input * 60
sec_to_sec = seconds_input
total_time = min_to_sec + sec_to_sec

stop_watch(total_time)