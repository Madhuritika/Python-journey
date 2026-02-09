import time
def study_timer():
    print(" Welcome to Study Timer (Pomodoro)")
    study_minutes = int(input("Enter study time in minutes: "))
    break_minutes = int(input("Enter break time in minutes: "))
    sessions = int(input("How many sessions do you want to study? "))

    for session in range(1, sessions + 1):
        print(f"\nSession {session} - Study Time Starts Now!")
        study_seconds = study_minutes * 60

        while study_seconds > 0:
            mins = study_seconds // 60
            secs = study_seconds % 60
            print(f"Study Time Left: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            study_seconds -= 1

        print("\nStudy session complete! Time for a break ")

        break_seconds = break_minutes * 60
        while break_seconds > 0:
            mins = break_seconds // 60
            secs = break_seconds % 60
            print(f" Break Time Left: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            break_seconds -= 1
    print("\nBreak over! Back to study!")
    print("\nAll sessions completed! You’re a warrior")
study_timer()
