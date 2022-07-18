import sys
import PySimpleGUI as sg
from ram import RAM

sg.theme("DarkAmber")
sg.set_options(font=('Courier New', 12))

if len(sys.argv) < 2:
    print("usage: ram program.ram input1 input2 ...")
    sys.exit(1)

file_name = sys.argv[1]
file = open(file_name, mode='r')
source_code = file.read()
file.close()

input = [int(i) for i in sys.argv[2:]]
ram = RAM(source_code, input)
source_code_list = [[line] for line in source_code.split('\n')]

layout = [
    [
        sg.Text('Input:', key='Input',  text_color = 'tomato', relief=sg.RELIEF_GROOVE, expand_x=True, expand_y=False)
    ],
    [
        sg.Table(source_code_list, key='Program', headings=['Program'], col_widths=[10], auto_size_columns=False, num_rows=min(25, len(source_code_list)),  display_row_numbers=True, justification='left', select_mode=sg.TABLE_SELECT_MODE_NONE, expand_x=True, expand_y=True),
        sg.Table([], key='Register', headings=['Registers'], col_widths=[10], auto_size_columns=False, num_rows=min(25, len(source_code_list)), display_row_numbers=True, justification='right', select_mode=sg.TABLE_SELECT_MODE_NONE, expand_x=True, expand_y=True, text_color = 'SkyBlue3'),
    ],
    [
        sg.Text('Output:', key='Output', text_color = 'light green', relief=sg.RELIEF_GROOVE, expand_x=True, expand_y=False)
    ]
]

window = sg.Window('RAM - '+file_name, layout, finalize=True, resizable=True, return_keyboard_events=True)

while True:
    window['Program'].update(select_rows=[ram.pc])
    window['Program'].Widget.see(1+ram.pc) # make selected item visible
    window['Input'].update(value='Input: '+str(ram.input))
    window['Register'].update(values=[[i] for i in ram.register])
    window['Output'].update(value='Output: '+str(ram.output))

    event, values = window.read()
    if event==sg.WIN_CLOSED:
        break
    if event==' ':
        try:
            if not ram.halted and not ram.step():
                sg.popup_auto_close('RAM halted')
                for i in ram.output:
                    print(i, end=' ')
                print('')
        except Exception as e:
            sg.popup_error_with_traceback(f'Exception occured executing instruction number {ram.pc}', e)
            break

window.close()