from PIL import Image, ImageTk
import tkinter as tk

class SO2HeatGUI :
    photoW : int
    photoH : int

    root = None
    houseImg = None
    workImg = None

    label : tk.Label
    image_label : tk.Label
    housePhoto : ImageTk.PhotoImage
    workPhoto : ImageTk.PhotoImage

    image : Image
    photo : ImageTk.PhotoImage

    def __init__(self, on_left_button_press, on_right_button_press, on_start_button_press, on_stop_button_press, img_size):
        self.root = tk.Tk()
        self.photoW = img_size[0]
        self.photoH = img_size[1]
        self.root.title("Heat")

        self.houseImg = Image.open("house.jpg").resize((self.photoW, self.photoH))
        self.workImg = Image.open("work.jpg").resize((self.photoW, self.photoH))

        self.housePhoto = ImageTk.PhotoImage(self.houseImg)
        self.workPhoto = ImageTk.PhotoImage(self.workImg)

        self.label = tk.Label(self.root, text="Let's heat my house!")
        self.label.pack()

        self.image_label = tk.Label(self.root, image=self.workPhoto)
        self.image_label.pack()

        start_http_button = tk.Button(self.root, text="HTTP start", command=on_start_button_press)
        start_http_button.pack()

        stop_http_button = tk.Button(self.root, text="HTTP stop", command=on_stop_button_press)
        stop_http_button.pack()

        space = tk.Label(self.root, text="")
        space.pack()

        left_button = tk.Button(self.root, text="Rotate left", command=on_left_button_press)
        left_button.pack()

        right_button = tk.Button(self.root, text="Rotate right", command=on_right_button_press)
        right_button.pack()

    def set_label(self, txt : str) :
        self.label.config(text=txt)

    def set_home_image(self) :
        self.image_label.config(image=self.housePhoto)

    def set_work_image(self) :
        self.image_label.config(image=self.workPhoto)

    def set_image(self, image : Image) :
        self.image = image.resize((self.photoW, self.photoH), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

    def start(self):
        self.root.mainloop()