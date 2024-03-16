import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askokcancel, showinfo
appname = "Apple的记事本"


def main():
    def c_new():        #新建文件(new file)
        var_filename.set("")
        root.title(f"未命名文件 - {appname}")
        text.delete(1.0, "end")
        
    def c_open():     #打开文件(open file)
        filename = askopenfilename()
        if filename:
            var_filename.set(filename)
            root.title(f"{appname} - {appname}")
            with open(filename) as f:
                text.delete(1.0, "end")
                text.insert(1.0, f.read())

    def c_save():           #保存文件(save file)
        filename = var_filename.get()
        if not filename:
            filename = asksaveasfilename()
        if filename:
            var_filename.set(filename)
            root.title(f"{appname} - {appname}")
            with open(filename, "w") as f:
                content = text.get(1.0, "end-1c")
                f.write(content)


    def c_exit():   #退出(exit app)
        if askokcancel("退出","你确定要退出吗?(三思而后行！！！)"):
            root.destroy()


    def c_about():    #关于程序(about app)
        showinfo(f"关于{appname}","由Apple自主研发的文本编辑器,功能强大，十分轻便                                                                        @Apple.保留所有权力                                                 许可如下用户使用本产品                               Windows和Apple用户                                       Organiztion")


    root = tk.Tk()
    root.title(f"未命名 - {appname}")
    root.protocol ("WM_DELETE_WINDOW", c_exit)
    var_filename = tk.StringVar(root)
    menu = tk.Menu(root)
    root["menu"] = menu
    m_file = tk.Menu(menu)
    menu.add_cascade(label="文件",menu=m_file)
    m_file.add_command(label="新建", command=c_new)
    m_file.add_command(label="打开...",command=c_open)
    m_file.add_command(label="保存",command=c_save)
    m_file.add_separator()
    m_file.add_command(label="退出", command=c_exit)
    m_help = tk.Menu(menu)
    menu.add_cascade(label="帮助",menu=m_help)
    m_help.add_command(label="关于",command=c_about)
    text = ScrolledText(root,width=100, height=40)
    text.pack()
    text.focus()
    root.mainloop()


if __name__ == '__main__':
    main()