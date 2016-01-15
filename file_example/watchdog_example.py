from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

#This handles all the events
class MyEventHandler(FileSystemEventHandler):
    """Prints all events"""

    def on_moved(self, event):
        what = 'directory' if event.is_directory else 'file'
        print("Moved {}: from {} to {}".format(what, event.src_path,
                     event.dest_path))

    def on_created(self, event):
        what = 'directory' if event.is_directory else 'file'
        print("Created {}: {}".format(what, event.src_path))

    def on_deleted(self, event):
        what = 'directory' if event.is_directory else 'file'
        print("Deleted " + what + ": " + event.src_path)

    def on_modified(self, event):
        what = 'directory' if event.is_directory else 'file'
        print ("Modified {}: {}".format(what, event.src_path))
        #Open the folder
        with open(event.src_path) as f:

            #Print the new contents of the folder
            file_contents = f.read()
            print("Text in the file is now: " + file_contents)

            #Write the contents to a new file
            with open('test_folder/copy_test.txt', 'w') as c:
                c.write("Other file contains: " + file_contents)

#This will watch the folder the program is in, it will pick up all changes made in the folder
path = '.'

#Create an event_handler, this will decide what to do when files are changed
event_handler = MyEventHandler()

#Create the observer, this will watch the files
observer = Observer()

#Tell the observer what to watch and give it the class that will handle the events
observer.schedule(event_handler, path)

#Start watching files
observer.start()

try:
    #Wait forever for the user to press Ctrl-C
    while True:
        pass
except KeyboardInterrupt:
    #The user has pressed Ctrl-C, stop watching files
    observer.stop()
observer.join()
