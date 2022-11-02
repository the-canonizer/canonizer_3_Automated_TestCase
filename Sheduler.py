import schedule
import time
from mailer import mailern
import mailer
import main
import os
def job():
    print("The testing begin ...")
    #exec("main.py")
    #Running the testcases
    os.system('python3 main.py')

    #os.system('python my_file.py')
def job2():
    #Sending the test report.
    mailer.mailern()
    print("Mail Sent")

'''schedule.every(5).seconds.do(job)
schedule.every(5).seconds.do(job2)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)'''
schedule.every().monday.at("11:55").do(job2)
schedule.every().tuesday.at("16:01").do(job2)
schedule.every().wednesday.at("14:57").do(job2)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
