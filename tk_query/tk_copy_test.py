import tkinter as tk
from PIL import Image, ImageTk


class ImageDisplay(tk.Tk):
    def __init__(self):
        super().__init__()

        # 加载图片
        image = Image.open("../base_api_query/1.jpg")
        photo = ImageTk.PhotoImage(image)

        # 创建标签并显示图片
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()

        # 创建右键菜单
        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="复制", command=self.copy_image)
        label.bind("<Button-2>", lambda event: context_menu.post(event.x_root, event.y_root))

    def copy_image(self):
        # 复制图片到剪贴板
        import pyperclip
        pyperclip.copy(self.clipboard_image)


if __name__ == "__main__":
    app = ImageDisplay()
    app.mainloop()