from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from . import insert_data_script


def start():
    #sched = BlockingScheduler(timezone="Asia/Kolkata")
    scheduler = BackgroundScheduler()
    scheduler.add_job(insert_data_script.transfer_daily_data, 'interval', minutes=1) # This script will run every day on 1 am (UTC time)
    scheduler.start()
