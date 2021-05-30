try:
    from watchdog.observers import Observer
    from watchdog.events import *

    class FileEventHandler(FileSystemEventHandler):
        def __init__(self):
            FileSystemEventHandler.__init__(self)

        def on_moved(self, event):
            if event.is_directory:
                print("目录从 {} 移到 {}".format(event.src_path, event.dest_path))
            else:
                print("文件从 {} 移到 {}".format(event.src_path, event.dest_path))
                self.task(filName=event.dest_path)

        def on_created(self, event):
            print("{} 被创建".format(event.src_path))

        def on_deleted(self, event):
            print("{} 被删除".format(event.src_path))

        def on_modified(self, event):
            print("{} 被修改".format(event.src_path))

        def task(self, filName):
            print(filename)
            # 具体任务
    if __name__ == "__main__":
        observer = Observer()
        event_handler = FileEventHandler()
        filePath = input("要跟踪的文件夹绝对路径：")
        observer.schedule(event_handler, filePath, True)
        observer.start()
        from time import sleep
        sleep(int(input("要跟踪几秒？")))
except FileNotFoundError:
    print("\a找不到此路径！")
except Exception as e:
    print(e)
