import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import pyperclip
import io


def show_image():
    # 在这里替换为你的图片路径
    image_path = "../base_api_query/1.jpg"

    # 打开图片并创建Tkinter PhotoImage对象
    image = Image.open(image_path)

    # 调整图片大小为615*415
    image = image.resize((615, 415))

    photo = ImageTk.PhotoImage(image)

    # 在Label中显示图片
    image_label.config(image=photo)
    image_label.image = photo


def copy_to_clipboard():
    # 获取图片路径
    image_path = "../base_api_query/1.jpg"

    # 打开图片
    image = Image.open(image_path)

    # 将图片复制到剪贴板
    copy_image(image)


def copy_image(image):
    # 将图片转换为字节流
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')

    # 获取字节流
    image_data = image_byte_array.getvalue()

    # 使用pyperclip复制图片数据到剪贴板
    pyperclip.copy(image_data)


# 创建主窗口
root = tk.Tk()
root.title("Tkinter程序")

# 创建左侧输入框
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=10, pady=10)

# 创建右侧按钮
button = tk.Button(root, text="显示图片", command=show_image)
button.grid(row=0, column=1, padx=10, pady=10)

# 创建底部Label用于显示图片
image_label = tk.Label(root)
image_label.grid(row=1, column=0, columnspan=2, pady=10)

# 创建右键菜单
right_click_menu = tk.Menu(root, tearoff=0)
right_click_menu.add_command(label="复制", command=copy_to_clipboard)


def show_context_menu(event):
    right_click_menu.post(event.x_root, event.y_root)


# 将右键菜单绑定到图片Label上，使用<Button-2>表示右键单击
image_label.bind("<Button-2>", show_context_menu)

# 运行Tkinter主循环
root.mainloop()
