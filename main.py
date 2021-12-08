import eel
from win10toast import ToastNotifier
import schedule
import time
from threading import Thread
import asyncio
import plyer

@eel.expose
def thread1(message, time_push):
	thread = Thread(target=start_push, args=(message, time_push))
	thread.start()

def start_push(message, time_push):
	schedule.every().day.at(time_push).do(notification, message)
	while True:
		schedule.run_pending()
		time.sleep(1)  

def notification(text):

	plyer.notification.notify( 
	message= text,
	app_name='NO TIME',
	app_icon='D:\project\eel\web\cgo.ico',
	title='NO TIME',
	timeout=10,
	ticker='read'
	)
	
eel.init('D:\project\eel\web')
eel.start('main.html',size=(600,1000))
