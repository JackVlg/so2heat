global photoW, photoH, imageLabel

import tkinter as tk
from PIL import Image, ImageTk
import so2heat_http_server
import queue
import threading

msg_queue = queue.Queue()

photoW = 800
photoH = 600

root = tk.Tk()

img1 = Image.open("house.jpg").resize((photoW, photoH))
img2 = Image.open("work.jpg").resize((photoW, photoH))
photo1 = ImageTk.PhotoImage(img1)
photo2 = ImageTk.PhotoImage(img2)
photo3 = None

root.title("Heat")

label = tk.Label(root, text="Let's heat my house!")
label.pack()


def left_button_click():
    label.config(text="Left pressed!")


def right_button_click():
    label.config(text="Right pressed!")


def start_http_button_click():
    httpServer.start()
    imageLabel.config(image=photo1)
    label.config(text="Http server started!")


def stop_http_button_click():
    httpServer.stop()
    imageLabel.config(image=photo2)
    label.config(text="Http server stoped!")


imageLabel = tk.Label(root, image=photo2)
imageLabel.pack()

startHttpButton = tk.Button(root, text="HTTP start", command=start_http_button_click)
startHttpButton.pack()

stopHttpButton = tk.Button(root, text="HTTP stop", command=stop_http_button_click)
stopHttpButton.pack()

space = tk.Label(root, text="")
space.pack()

lbutton = tk.Button(root, text="Rotate left", command=left_button_click)
lbutton.pack()

rbutton = tk.Button(root, text="Rotate right", command=right_button_click)
rbutton.pack()

so2heat_http_server.initialize({
    "photoW": photoW,
    "photoH": photoH,
    "msg_queue": msg_queue
})
httpServer = so2heat_http_server.StoppableHTTPServer()


def image_handler(data):
    print("image comming")
    global photo3
    photo3 = ImageTk.PhotoImage(data)
    imageLabel.config(image=photo3)


class QueueManager:
    def __init__(self, root, check_interval=100):
        self.root = root
        self.check_interval = check_interval
        self.handlers = {}  # Словарь обработчиков по типам сообщений

    def register_handler(self, msg_type, callback):
        """Регистрация обработчика для определенного типа сообщений"""
        self.handlers[msg_type] = callback

    def start_checking(self):
        """Запуск проверки очереди"""
        self._check_queue()

    def _check_queue(self):
        """Внутренний метод проверки"""
        try:
            while True:
                msg = msg_queue.get_nowait()

                if isinstance(msg, tuple) and len(msg) == 2:
                    msg_type, data = msg
                    if msg_type in self.handlers:
                        # Вызываем зарегистрированный обработчик
                        self.root.after(0, self.handlers[msg_type], data)
                    else:
                        print(f"Нет обработчика для типа {msg_type}")
        except:
            pass

        self.root.after(self.check_interval, self._check_queue)

    def put(self, msg_type, data):
        """Добавление сообщения в очередь"""
        msg_queue.put((msg_type, data))


qm = QueueManager(root)
qm.register_handler('image', image_handler)
qm.start_checking()

print(f"Имя потока (прямой доступ): {threading.current_thread().name}")

root.mainloop()
