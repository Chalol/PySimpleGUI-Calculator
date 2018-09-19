from PySimpleGUI import *
import PySimpleGUI as sg

#color
white = '#ffffff'
black = '#000000'
green = '#5ae03a'
red = '#df1e1e'
red1 = '#df3939'
yellow = '#fbc00c'
pastelyellow = '#ffff77'

#set button position, color, font, font size 
layout = [[sg.Input(size=(30,2), do_not_clear=True, justification='left', key='input', background_color=black,text_color=pastelyellow, font='Arial')],
            [sg.Text(" ", size=(25,1),justification='right', font=('Arial',15), text_color=red1 ,background_color=pastelyellow, key='out')],
            [sg.ReadFormButton('+', button_color=(white,green), font='Arial'), sg.ReadFormButton('-', button_color=(white,green), font='Arial'), sg.ReadFormButton('*', button_color=(white,green), font='Arial'), sg.ReadFormButton('/', button_color=(white,green), font='Arial')],
            [sg.ReadFormButton('7', button_color=(white,red), font='Arial'), sg.ReadFormButton('8', button_color=(white,red), font='Arial'), sg.ReadFormButton('9', button_color=(white,red), font='Arial'), sg.ReadFormButton('C', button_color=(white,green), font='Arial')],
            [sg.ReadFormButton('4', button_color=(white,red), font='Arial'), sg.ReadFormButton('5', button_color=(white,red), font='Arial'), sg.ReadFormButton('6', button_color=(white,red), font='Arial'), sg.ReadFormButton('Del', button_color=(white,green), font='Arial')],
            [sg.ReadFormButton('1', button_color=(white,red), font='Arial'), sg.ReadFormButton('2', button_color=(white,red), font='Arial'), sg.ReadFormButton('3', button_color=(white,red), font='Arial'), sg.ReadFormButton('.', button_color=(white,green), font='Arial')],
            [sg.ReadFormButton('(', button_color=(white,green), font='Arial'), sg.ReadFormButton('0', button_color=(white,red), font='Arial'), sg.ReadFormButton(')', button_color=(white,green), font='Arial'), sg.ReadFormButton('=', button_color=(white,yellow), font='Arial')],
            ]

# set screen and button size
form = sg.FlexForm('Calculator', default_button_element_size=(6,3), auto_size_buttons=False, grab_anywhere=False, background_color=black)
form.Layout(layout)

in_put= " "
answer = " "
while True:
    button,values = form.Read()                # read input
    # if button is None:
    #     break
    if len(in_put) >= 26:                      # set input range
        in_put = in_put[:-1]
    if button is 'C':                          # if click button C then show nothing
        in_put = " "
        answer = " "
    elif button is 'Del':                      # if click button Del then delete
        in_put = in_put[:-1]
    elif button in '1234567890':               # if click number pad then in_put add number and show number
        in_put = values['input']
        in_put += button
    elif button in  '+-*/.()':                 # if click operand pad then in_put add operand and show operand
        in_put = values['input']
        in_put += button
    elif button is '=':
        if in_put[0] == '+' or in_put[0] == '-' or in_put[0] == '*' or in_put[0] == '/':  # if at first is operand then show error
            answer = 'ERROR! Please try again..'
        elif in_put[-1] == '+' or in_put[-1] == '-' or in_put[-1] == '*' or in_put[-1] == '/': #if at last is operand then show error
            answer = 'ERROR! at the last one'
        elif '/0' in in_put:                   # if input divide by zero then shoe error
            answer = "ERROR! Can't divide by 0"
        elif '++' in in_put or '--' in in_put or '**' in in_put or '//' in in_put:  #if has operand more than 1 then show error
            answer = "Operation Error"
        elif in_put == ' ':                    # if input is blank then pass
            pass 
        else:
            in_put = values['input']
            answer = eval(in_put)
    # update input and answer on screen
    form.FindElement('out').Update(answer)
    form.FindElement('input').Update(in_put)