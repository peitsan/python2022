from unCheckinList import mainCheck
# from apscheduler.schedulers.blocking import BlockingScheduler
import time


# def startCronTask(task, **config):
#     # BlockingScheduler
#     scheduler = BlockingScheduler()
#     scheduler.add_job(task, 'interval', **config)
#     scheduler.start()

if __name__ == '__main__':
    while True:
        time_now = time.strftime("%H%M", time.localtime())  # 刷新
        if time_now == "08:01":  # 设置要执行的时间
            mainCheck()
            time.sleep(61)  # 停止执行61秒，防止反复运行程序。
        elif time_now == "10:01":  # 设置要执行的时间:
            mainCheck()
            time.sleep(61)  # 停止执行61秒，防止反复运行程序。
        elif time_now == "11:01":  # 设置要执行的时间:
            mainCheck()
            time.sleep(61)
        elif time_now == "12:01":  # 设置要执行的时间:
            mainCheck()
            time.sleep(61)