import schedule
import time

def job():
    print("test")


schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute