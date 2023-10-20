import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

class FileEventHandler(FileSystemEventHandler):

    
    def on_created(self,event):
        print(f"oye,{event.src_path} ha sido creado")
    def on_deleted(self,event):
        print(f"lo siento, alguien borro {event.src_path}")
    def on_modificated(self,event):
        print(f"hola,{event.src_path} ha sido modificado")
    def on_moved(self,event):
        print(f"algien movio {event.src_path} a {event.dest_path}")


  
        



event_handler = FileEventHandler()


observer = Observer()


observer.schedule(event_handler, from_dir, recursive=True)



observer.start()



try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()



