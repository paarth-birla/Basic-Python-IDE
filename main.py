from tkinter import *
from tkinter import font 
from tkinter import filedialog
from tkinter import messagebox


BACKGROUND = '#ffffff'
FOREGROUND = '#000000'
FONT = 'Arial 13'
ACTIVE_BACKGROUND = '#d6d6d6'
BAR_BACKGROUND = ''
BAR_FOREGROUND = ''
filename = ''

'''
==========================================MENU FUNCTIONS==========================================
'''

'''
File Functions
'''
# New file
def _new(*args):
    editor.delete('1.0', END)

# Open file
def _open(*args):
    editor.delete('1.0', END)
    openfile = filedialog.askopenfilename(title='Open File', filetypes=(('Text Files', '*.txt'), ('Python Files', '*.py'), ('All files', '*.*')))
    if openfile:
        _file = open(openfile, 'r')
        data = _file.read()
        editor.insert(END, data)
        _file.close()
    
    else:
        return

# Save file
def _save(*args):
    pass

# Save As
def _saveas(*args):
    filename = filedialog.asksaveasfilename(defaultextension='*.txt', title='Save File', filetypes=(('Text Files', '*.txt'), ('Python Files', '*.py'), ('All files', '*.*')))
    if filename:
        filename = open(filename, 'w')
        filename.write(editor.get('1.0', END))
        filename.close()
# Exit
def _exit(*args):
    user = messagebox.askyesno('Warning', 'Do you want to exit?')
    if user > 0:
        root.destroy()
    
    else:
        return


'''
Edit Functions
'''
# Copy
def _copy(*args):
    editor.event_generate('<<Copy>>')

# Cut
def _cut(*args):
    editor.event_generate('<<Cut>>')

# Paste
def _paste(*args):
    editor.event_generate('<<Paste>>')

# Undo
def _undo(*args):
    pass



'''
Run Functions
'''
# run file
def _runfile():
    pass


'''
View Functions
'''
# default theme
def _defaulttheme():
    BACKGROUND = '#ffffff'
    FOREGROUND = '#000000'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# atom dark theme
def _atomdark():
    BACKGROUND = '#282c34'
    FOREGROUND = '#ffffff'
    ACTIVE_BACKGROUND = '#3e4451'
    BAR_BACKGROUND = '#21252b'
    BAR_FOREGROUND = '#9da5b4'
    root.config(background=BAR_BACKGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# dark theme
def _darktheme():
    BACKGROUND = '#1e1e1e'
    FOREGROUND = '#d4d4d4'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# solarised light theme
def _solartheme():
    BACKGROUND = '#fdf6e3'
    FOREGROUND = '#333333'
    ACTIVE_BACKGROUND = '#eee8d5'
    BAR_BACKGROUND = '#eee8d5'
    BAR_FOREGROUND = '#586e75'
    root.config(background=BAR_BACKGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# hacker theme
def _hackertheme():
    BACKGROUND = '#0F0F0F'
    FOREGROUND = '#33FF33'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)
# default font
def _defaultfont():
    FONT = 'Arial 13'
    editor.config(font=FONT)

# times font
def _timesfont():
    FONT = 'Times 13'
    editor.config(font=FONT)

# system font
def _systemfont():
    FONT = 'System 13'
    editor.config(font=FONT)
# helvetica font
def _helveticafont():
    FONT = 'Helvetica 13'
    editor.config(font=FONT)

# fixedsys font
def _fixedsysfont():
    FONT = 'fixedsys 13'
    editor.config(font=FONT)


'''
Help Functions
'''
def _about():
    pass


'''
Shorcuts function
'''
def shortcuts():
    editor.bind('<Control-n>', _new)
    editor.bind('<Control-o>', _open)
    editor.bind('<Control-s>', _save)
    editor.bind('<Control-k>', _saveas)
    editor.bind('<Control-c>', _copy)
    editor.bind('<Control-x>', _cut)
    editor.bind('<Control-v>', _paste)
    editor.bind('<Control-u>', _undo)

'''
==========================================GUI==========================================
'''

root = Tk()
root.title('IDE')
root.geometry('1200x600+200+50')

statusbar = Label(root, text='x,y\tPython\t', anchor=E)
statusbar.pack(fill=X, side=BOTTOM)

main_frame = Frame(root)
main_frame.pack(padx=5, pady=5)

scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT, fill=Y)

editor = Text(main_frame, width=500, height=550, font=FONT, background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND, yscrollcommand=scrollbar.set)
editor.pack(expand=True, fill=BOTH)
shortcuts()

scrollbar.config(command=editor.yview)

menu_bar = Menu(root)
'''
File Menu
'''
def _file():
    file = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file)
    file.add_command(label='New', accelerator='Ctrl+N', command=_new)
    file.add_command(label='Open', accelerator='Ctrl+O', command=_open)
    file.add_command(label='Save', accelerator='Ctrl+S', command=_save)
    file.add_command(label='Save As', accelerator='Ctrl+K', command=_saveas)
    file.add_separator()
    file.add_command(label='Exit', command=_exit)

'''
Edit Menu
'''
def _edit():
    edit = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Undo', accelerator='Ctrl+U', command=_new)
    edit.add_separator()
    edit.add_command(label='Cut', accelerator='Ctrl+X', command=_cut)
    edit.add_command(label='Copy', accelerator='Ctrl+C', command=_copy)
    edit.add_command(label='Paste', accelerator='Ctrl+V', command=_paste)
    edit.add_separator()

'''
Run Menu
'''
def _run():
    run = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Run', menu=run)
    run.add_command(label='Run', accelerator='F5', command=_runfile)


'''
View Menu
'''
def _view():
    view = Menu(menu_bar, tearoff=0)

    appear = Menu(view, tearoff=0)
    appear.add_command(label='Default', command=_defaulttheme)
    appear.add_command(label='Atom One Dark', command=_atomdark)
    appear.add_command(label='Dark', command=_darktheme)
    appear.add_command(label='Solarized Light', command=_solartheme)
    appear.add_command(label='Hacker', command=_hackertheme)

    fonts = Menu(view, tearoff=0)
    fonts.add_command(label='Default', command=_defaultfont)
    fonts.add_command(label='Times', command=_timesfont)
    fonts.add_command(label='System', command=_systemfont)
    fonts.add_command(label='Helvetica', command=_helveticafont)
    fonts.add_command(label='Fixedsys', command=_fixedsysfont)

    view.add_cascade(label='Appearance', menu=appear)
    view.add_cascade(label='Fonts', menu=fonts)

    menu_bar.add_cascade(label="View", menu=view)

def _help():
    help = Menu(menu_bar, tearoff=0)
    help.add_command(label='About', command=_about)
    menu_bar.add_cascade(label='Help', menu=help)
# call functions
_file()
_edit()
_run()
_view()
_help()
root.config(menu = menu_bar)
root.mainloop()