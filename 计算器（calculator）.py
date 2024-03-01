import PySimpleGUI as sg
def button(text):
    return sg.B(text,pad=(2,2),size=(4,2),font=('黑体',18),button_color='black' )
layout=[
    [sg.T('',key='-SHOW-')],
    [sg.In('',size=(12,2),font=('黑体',28),key='-INPUT-')],
    [button(i)for i in ['AC','(',')','%']],
    [button(i)for i in '123+'],
    [button(i)for i in '456-'],
    [button(i)for i in '789X'],
    [button(i)for i in '0.=÷']

]
window=sg.Window('Apple的计算器',layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event in list('0123456789+-().=X÷%'):
        window['-INPUT-'].update(values['-INPUT-'] + event)
        window['-SHOW-'].update('')
    if event == 'X':
        window['-INPUT-'].update(values['-INPUT-'] + '*')
        window['-SHOW-'].update('')
    if event == '÷':
        window['-INPUT-'].update(values['-INPUT-'] + '/')
        window['-SHOW-'].update('')
    if event == '%':
        try:
            window['-INPUT-'].update(eval(values['-INPUT-'] + '/100'))
            window['-SHOW-'].update('')
        except:
            window['-INPUT-'].update('')
            window['-SHOW-'].update('不是，你怎么输入的啊')
    if event == '=':
        try:
            window['-INPUT-'].update(eval(values['-INPUT-']))
        except:
            window['-INPUT-'].update('')
            window['-SHOW-'].update('不是，你故意的啊')
    if event == 'AC':
        window['-INPUT-'].update('')
        window['-SHOW-'].update('')
window.close()