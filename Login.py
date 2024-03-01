import PySimpleGUI as sg
layout = [
[sg.B('中文(Chinese)'),sg.B('English(英语)')],
[sg.T('请输入个人信息',key='-TITCE-')],
[sg.T('姓名',key='-NAMETXT-'),sg.In()],
[sg.T('性别',key='-SEXTXT-'),sg.In()],
[sg.T('年龄',key='-AGETXT-'),sg.In()],
[sg.T('身份证号',key='-IDTXT-'),sg.In()],
[sg.B('确认',key='-CONF-'),sg.B('取消',key='-CANCEl-')],
]
window=sg.Window('注册   Login',layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event =='English(英语)':
        window['-TITCE-'].update('Please Enter Personal Information')
        window['-NAMETXT-'].update('Name')
        window['-SEXTXT-'].update('Sex')
        window['-AGETXT-'].update('Age')
        window['-IDTXT-'].update('Id Card')
        window['-CONF-'].update('Confirm')
        window['-CANCEl-'].update('cancel')
    if event == '中文(Chinese)':
        window['-TITCE-'].update('请输入个人信息')
        window['-NAMETXT-'].update('姓名')
        window['-SEXTXT-'].update('性别')
        window['-AGETXT-'].update('年龄')
        window['-IDTXT-'].update('身份证号')
        window['-CONF-'].update('确认')
        window['-CANCEl-'].update('取消')
    if event =='-CONF-':
        window.close()
    if event == '-CANCEl-':
        window.close()
window.close()