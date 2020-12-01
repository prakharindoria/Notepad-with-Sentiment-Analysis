import tkinter as tk
import tkinter.font
import pyttsx3
from tkinter import ttk, font, colorchooser, messagebox, filedialog
from textblob import TextBlob
import NotepadController
import traceback

class Notepad:

    #Intialize.
    def __init__(self, root):
        #Root Window
        self.root = root
        self.root.geometry('1200x800')
        self.root.title('NotePad')
        self.root.wm_iconbitmap('icons/icon.ico')
        self.root.protocol("WM_DELETE_WINDOW", self.exit_func)

        #Obtain NotepadController obj
        self.notepadController = NotepadController.Controller()
        self.url = ''
        self.prev_text = ''
        self.text_changed = False

        #Method Calls
        self.show_statusbar=tk.BooleanVar()
        self.show_statusbar.set(True)
        self.show_toolbar=tk.BooleanVar()
        self.show_toolbar.set(True)

        #Method Calls
        self.set_menu_bar()
        self.set_icons()
        self.set_file_sub_menu()
        self.set_edit_sub_menu()
        self.set_view_sub_menu()
        self.set_color_theme()
        self.set_tool_bar()
        self.set_canvas()
        self.set_status_bar()
        self.set_file_menu_event_bindings()
        self.set_tool_bar_event_bindings()



    #Set Icons.
    def set_icons(self):
        self.new_icon = tk.PhotoImage(file='icons/new.png')
        self.open_icon = tk.PhotoImage(file='icons/open.png')
        self.save_icon = tk.PhotoImage(file='icons/save.png')
        self.save_as_icon = tk.PhotoImage(file='icons/save_as.png')
        self.exit_icon = tk.PhotoImage(file='icons/exit.png')
        self.copy_icon = tk.PhotoImage(file='icons/copy.png')
        self.paste_icon = tk.PhotoImage(file='icons/paste.png')
        self.cut_icon = tk.PhotoImage(file='icons/cut.png')
        self.clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
        self.find_icon = tk.PhotoImage(file='icons/find.png')
        self.tool_bar_icon=tk.PhotoImage(file='icons/tool_bar.png')
        self.status_bar_icon=tk.PhotoImage(file='icons/status_bar.png')
        self.light_default_icon=tk.PhotoImage(file='icons/light_default.png')
        self.light_plus_icon=tk.PhotoImage(file='icons/light_plus.png')
        self.dark_icon=tk.PhotoImage(file='icons/dark.png')
        self.red_icon=tk.PhotoImage(file='icons/red.png')
        self.monokai_icon=tk.PhotoImage(file='icons/monokai.png')
        self.night_blue_icon=tk.PhotoImage(file='icons/night_blue.png')
        self.microphone=tk.PhotoImage(file='icons/microphone.png')
        self.speaker = tk.PhotoImage(file='icons/speaker_icon.png')


    #Set Horizantal MenuBar
    def set_menu_bar(self):
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.color_theme = tk.Menu(self.menu_bar, tearoff=0)

        #Add to MenuBar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.menu_bar.add_cascade(label="Color Theme", menu=self.color_theme)
        self.root.config(menu=self.menu_bar)

    #Set Vertical File SubMenuBar inside MenuBar
    def set_file_sub_menu(self):
        self.file_menu.add_command(label='New', image=self.new_icon, compound=tk.LEFT, accelerator='Ctrl+N',
                                   command=self.new_file)
        self.file_menu.add_command(label='Open', image=self.open_icon, compound=tk.LEFT, accelerator='Ctrl+O',
                                   command=self.open_file)
        self.file_menu.add_command(label='Save', image=self.save_icon, compound=tk.LEFT, accelerator='Ctrl+S',
                                   command=self.save_file)
        self.file_menu.add_command(label='Save As', image=self.save_as_icon, compound=tk.LEFT, accelerator='Alt+S',
                                   command=self.save_as)
        self.file_menu.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q',
                                   command=self.exit_func)

    #Set File Menu Event Bindings
    def set_file_menu_event_bindings(self):
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-N>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-O>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-S>", self.save_file)
        self.root.bind("<Alt-s>", self.save_as)
        self.root.bind("<Alt-S>", self.save_as)
        self.root.bind("<Control-q>", self.exit_func)
        self.root.bind("<Control-Q>", self.exit_func)


    #Set Vertical Edit SubMenuBar inside MenuBar
    def set_edit_sub_menu(self):
        self.edit_menu.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                                   command=lambda: self.text_editor.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                                   command=lambda: self.text_editor.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                                   command=lambda: self.text_editor.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT, accelerator='Alt+X',
                                   command=lambda: self.text_editor.delete(1.0, tk.END))
        self.edit_menu.add_command(label='Find', image=self.find_icon, compound=tk.LEFT, accelerator='Ctrl+F',
                                   command=lambda: self.find_func())

    #Set Find Function inside SubMenuBar of MenuBar
    def find_func(self, event=None):
        self.find_dialogue = tk.Toplevel()
        self.find_dialogue.geometry('450x250+500+200')
        self.find_dialogue.title('Find')
        self.find_dialogue.title('Find')
        self.find_dialogue.resizable(0, 0)

        self.find_frame = ttk.LabelFrame(self.find_dialogue, text='find/replace')
        self.find_frame.pack(pady=20)

        self.text_find_label = ttk.Label(self.find_frame, text='find:')
        self.text_replace_label = ttk.Label(self.find_frame, text='replace:')

        self.find_input = ttk.Entry(self.find_frame, width=30)
        self.replace_input = ttk.Entry(self.find_frame, width=30)

        self.find_button = ttk.Button(self.find_frame, text='Find', command=self.find)
        self.replace_button = ttk.Button(self.find_frame, text='Replace', command=self.replace)

        self.text_find_label.grid(row=0, column=0, padx=4, pady=4)
        self.text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        self.find_input.grid(row=0, column=1, padx=4, pady=4)
        self.replace_input.grid(row=1, column=1, padx=4, pady=4)

        self.find_button.grid(row=2, column=0, padx=8, pady=4)
        self.replace_button.grid(row=2, column=1, padx=8, pady=4)

        self.find_dialogue.mainloop()

    #Set Vertical View SubMenuBar inside MenuBar
    def set_view_sub_menu(self):
        self.view_menu.add_checkbutton(label='Tool bar',onvalue=True,offvalue=False,variable=self.show_toolbar,
                                  image=self.tool_bar_icon,compound=tk.LEFT,command=self.hide_toolbar)
        self.view_menu.add_checkbutton(label='Status bar', onvalue=True, offvalue=False, variable=self.show_statusbar,
                                  image=self.status_bar_icon, compound=tk.LEFT, command=self.hide_statusbar)

    #Set Vertical Color Theme SubMenuBar inside MenuBar
    def set_color_theme(self):
        self.theme_choice=tk.StringVar()
        self.color_icons=(self.light_default_icon,self.light_plus_icon,self.dark_icon,self.red_icon,self.monokai_icon,self.night_blue_icon)
        self.color_dict={
            'Light Default':('#000000','#ffffff'),
            'Light Plus':('#474747','#e0e0e0'),
            'Dark':('#c4c4c4','#2d2d2d'),
            'Red':('#2d2d2d','#ffe8e8'),
            'Monokai':('#d3b774','#474747'),
            'Night Blue':('#ededed','#6b9dc2')}
        self.count=0
        for x in self.color_dict:
            self.color_theme.add_radiobutton(label=x,image=self.color_icons[self.count],variable=self.theme_choice,
                                             compound=tk.LEFT,value=self.color_dict[x],command=self.change_theme)
            self.count+=1

    #Set Horizantal ToolBar
    def set_tool_bar(self):
        self.tool_bar = ttk.Label(self.root)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)

        self.font_tuple = tk.font.families()
        self.font_family = tk.StringVar()
        self.font_box = ttk.Combobox(self.tool_bar, width=30, textvariable=self.font_family, state='readonly')
        self.font_box['values'] = self.font_tuple
        self.font_box.current(self.font_tuple.index('Arial'))
        self.font_fam='Arial'
        self.font_box.grid(row=0, column=0, padx=5)

        self.size_var = tk.IntVar()
        self.font_size = ttk.Combobox(self.tool_bar, width=14, textvariable=self.size_var, state='readonly')
        self.font_size['values'] = tuple(range(8, 81))
        self.font_size.current(4)
        self.font_size.grid(row=0, column=1, padx=5)

        self.bold_icon = tk.PhotoImage(file='icons/bold.png')
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon)
        self.bold_btn.grid(row=0, column=2, padx=5)

        self.italic_icon = tk.PhotoImage(file='icons/italic.png')
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon)
        self.italic_btn.grid(row=0, column=3, padx=5)

        self.underline_icon = tk.PhotoImage(file='icons/underline.png')
        self.underline_btn = ttk.Button(self.tool_bar, image=self.underline_icon)
        self.underline_btn.grid(row=0, column=4, padx=5)

        self.font_color_icon = tk.PhotoImage(file='icons/font_color.png')
        self.font_color_btn = ttk.Button(self.tool_bar, image=self.font_color_icon)
        self.font_color_btn.grid(row=0, column=5, padx=5)

        self.align_left_icon = tk.PhotoImage(file='icons/align_left.png')
        self.align_left_btn = ttk.Button(self.tool_bar, image=self.align_left_icon)
        self.align_left_btn.grid(row=0, column=6, padx=5)

        self.align_center_icon = tk.PhotoImage(file='icons/align_center.png')
        self.align_center_btn = ttk.Button(self.tool_bar, image=self.align_center_icon)
        self.align_center_btn.grid(row=0, column=7, padx=5)

        self.align_right_icon = tk.PhotoImage(file='icons/align_right.png')
        self.align_right_btn = ttk.Button(self.tool_bar, image=self.align_right_icon)
        self.align_right_btn.grid(row=0, column=8, padx=5)

        self.mic_icon = tk.PhotoImage(file='icons/microphone.png')
        self.mic_btn = ttk.Button(self.tool_bar, image=self.mic_icon)
        self.mic_btn.grid(row=0, column=9, padx=5)

        self.speak_icon = tk.PhotoImage(file='icons/speaker_icon.png')
        self.speak_btn = ttk.Button(self.tool_bar, image=self.speak_icon)
        self.speak_btn.grid(row=0, column=10, padx=5)

    #Set ToolBar Event Bindings
    def set_tool_bar_event_bindings(self):
        self.current_font_family='Arial'
        self.current_font_size=12
        self.current_weight='normal'
        self.current_slant='roman'
        self.current_underline=0
        self.font_box.bind("<<ComboboxSelected>>",self.change_font)
        self.font_size.bind("<<ComboboxSelected>>",self.change_fontsize)
        self.bold_btn.configure(command=self.change_bold)
        self.italic_btn.configure(command=self.change_italic)
        self.underline_btn.configure(command=self.change_underline)
        self.font_color_btn.configure(command=self.change_font_color)
        self.align_right_btn.configure(command=self.align_right)
        self.align_left_btn.configure(command=self.align_left)
        self.align_center_btn.configure(command=self.align_center)
        self.mic_btn.configure(command=self.saySomething)
        self.speak_btn.configure(command=self.speakOut)


    # Set Canvas For TextColor
    def set_canvas(self):
        self.text_editor = tk.Text(self.root)
        self.text_editor.config(wrap='word', relief=tk.FLAT)
        self.text_editor.focus_set()
        self.scroll_bar = tk.Scrollbar(self.root)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.scroll_bar.config(command=self.text_editor.yview)
        self.text_editor.config(yscrollcommand=self.scroll_bar.set)
        self.text_changed = False
        self.text_editor.bind('<<Modified>>', self.changed)

    #Set Status Bar
    def set_status_bar(self):
        self.status_bar = ttk.Label(self.root, text='Status Bar')
        self.status_bar.pack(side=tk.BOTTOM)
        self.count = 0

    #Method to Change Theme
    def change_theme(self):
        print(type(self.theme_choice.get()))
        ls=self.theme_choice.get().split()
        self.text_editor.configure(background=ls[1],foreground=ls[0])


    #Method to Hide Status Bar
    def hide_statusbar(self):
        if self.show_statusbar:
            self.status_bar.pack_forget()
            self.show_statusbar=False

        else:
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_statusbar=True

    # Method to Hide ToolBar
    def hide_toolbar(self):
        if self.show_toolbar:
            self.tool_bar.pack_forget()
            self.show_toolbar=False
        else:
            self.text_editor.pack_forget()
            self.status_bar.pack_forget()
            self.tool_bar.pack(side=tk.TOP,fill=tk.X)
            self.text_editor.pack(fill=tk.BOTH,expand=True)
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_toolbar=True

    #Method to Find Word Occurance
    def find(self):
        print('hello from find')
        word = self.find_input.get()
        self.text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                print(start_pos, end_pos)
                self.text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.text_editor.tag_config('match', foreground='red', background='yellow')
        if matches:
            messagebox.showinfo('word found', f'{word} occurs {matches} times')

    #Method to Replace Word Occurance
    def replace(self):
        word = self.find_input.get()
        self.replace_text = self.replace_input.get()
        self.content = self.text_editor.get(1.0, tk.END)
        self.new_content = self.content.replace(word, self.replace_text)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(1.0, self.new_content)


    # Method for New File
    def new_file(self):
        self.url = ''
        self.text_editor.delete(1.0, tk.END)
        self.root.title('MyNotePad')
        self.text_changed = False

    #Method to Open new File
    def open_file(self):
        try:
            self.url = filedialog.askopenfilename(title='select a file', filetypes=[('text documents', '*.*')])
            self.msg, self.base = self.notepadController.read_file(self.url)
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(1.0, self.msg)
            self.root.title(self.base)
            self.text_editor.edit_modified(False)
        except FileNotFoundError:
            messagebox.showerror('error', 'please select a file')
            print(traceback.format_exc())

    # Method to Save File (Normal Text Without Encryption)
    def save_file(self, e=None):
        try:
            content = self.text_editor.get(1.0, 'end-1c')
            if self.url == '':
                print('inside if block')
                self.save_dialog()
                self.notepadController.save_file(content, self.url)
                self.text_editor.edit_modified(False)
                self.text_changed = False
            else:
                self.notepadController.save_file(content, self.url)
                self.text_editor.edit_modified(False)
                self.text_changed = False

        except Exception:
            self.url=''
            messagebox.showerror('Error!', 'please select a file to save')
            print(traceback.format_exc())

    def save_dialog(self):
        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',
                                            filetypes=[('all files', "*.*"), ('text documents', '*.txt')])

    #Method to Save File As .ntxt (Encrypted Format)
    def save_as(self):
        content = self.text_editor.get(1.0, tk.END)
        self.save_dialog()
        try:
            self.notepadController.save_as(content, self.url)
            self.text_changed = False
        except FileNotFoundError:
            self.url=''
            messagebox.showerror('Error!', 'please select a file to save')
            print(traceback.format_exc())

    #Method for Exit
    def exit_func(self, event=None):
        result = messagebox.askyesno("App Closing", "Do you want to Quit?")
        if result == False:
            return
        try:
            if self.url == '':
                if len(self.text_editor.get('1.0', 'end-1c')) == 0:
                    self.text_changed = False
            if self.text_changed:
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
                if mbox:
                    content = self.text_editor.get(1.0, 'end-1c')
                    if (self.url == ''):
                        self.save_dialog()
                        self.notepadController.save_file(content, self.url)
                    else:
                        self.notepadController.save_file(content,self.url)
            messagebox.showinfo('Have A Good Day', 'Thank You for using Notepad')
            self.root.destroy()
        except:
            messagebox.showerror('Error', 'Please select file to save.')
            print(traceback.format_exc())


    #Methods For ToolBar Functionality
    def change_font(self,e):
        self.current_font_family=self.font_box.get()
        self.font_spec=font.Font(family=self.current_font_family,size=self.current_font_size,weight=self.current_weight,
                                 slant=self.current_slant,underline=self.current_underline)
        self.text_editor.configure(font=self.font_spec)


    def change_fontsize(self,e):
        self.current_font_size = self.font_size.get()
        self.font_spec = font.Font(family=self.current_font_family, size=self.current_font_size,
                                   weight=self.current_weight, slant=self.current_slant,
                                   underline=self.current_underline)
        self.text_editor.configure(font=self.font_spec)

    def change_bold(self):
        if self.current_weight == 'normal':
            self.current_weight = 'bold'
        else:
            self.current_weight = 'normal'
        self.font_spec = font.Font(family=self.current_font_family, size=self.current_font_size, weight=self.current_weight,
                                   slant=self.current_slant, underline=self.current_underline)
        self.text_editor.configure(font=self.font_spec)

    def change_italic(self):
        if self.current_slant=='roman':
            self.current_slant='italic'
        else:
            self.current_slant = 'roman'
        self.font_spec = font.Font(family=self.current_font_family, size=self.current_font_size, weight=self.current_weight,
                                   slant=self.current_slant, underline=self.current_underline)
        self.text_editor.configure(font=self.font_spec)

    def change_underline(self):
        if self.current_underline == 0:
            self.current_underline = 1
        else:
            self.current_underline = 0
        self.font_spec = font.Font(family=self.current_font_family, size=self.current_font_size, weight=self.current_weight,
                                   slant=self.current_slant, underline=self.current_underline)
        self.text_editor.configure(font=self.font_spec)

    def change_font_color(self):
        self.current_text_color=colorchooser.askcolor(title='choose text color',color='black')
        if(self.current_text_color[1] is None):
            return
        else:
            print(type(self.current_text_color[1]),self.current_text_color)
            self.text_editor.configure(foreground=self.current_text_color[1])

    def align_left(self):
        text_content=self.text_editor.get(1.0,tk.END)
        self.text_editor.tag_config('left',justify=tk.LEFT)
        self.text_editor.delete(1.0,tk.END)
        self.text_editor.insert(tk.INSERT,text_content,'left')

    def align_center(self):
        text_content = self.text_editor.get(1.0, tk.END)
        self.text_editor.tag_config('center', justify=tk.CENTER)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'center')

    def align_right(self):
        text_content = self.text_editor.get(1.0, tk.END)
        self.text_editor.tag_config('right', justify=tk.RIGHT)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'right')


    def changed(self, event=None):
        words = len(self.text_editor.get(1.0, 'end-1c').split())
        characters = len(self.text_editor.get(1.0, 'end-1c'))
        sentimentMood=self.saySentiment(self.text_editor.get(1.0, 'end-1c'))
        if sentimentMood=="Positive":
            self.status_bar.config(text=f'characters: {characters} words:{words} sentiment: {sentimentMood}',foreground="green")
        elif sentimentMood=="Neutral":
            self.status_bar.config(text=f'characters: {characters} words:{words} sentiment: {sentimentMood}',
                                   foreground="yellow")
        elif sentimentMood=="Negative":
            self.status_bar.config(text=f'characters: {characters} words:{words} sentiment: {sentimentMood}',
                                   foreground="red")
        if self.text_editor.edit_modified():
            self.text_changed = True
        self.text_editor.edit_modified(False)


    def saySentiment(self,text):
        self.blob=TextBlob(text).sentiment
        if self.blob[0]>=0.6:
            return "Positive"
        elif self.blob[0]<0.6 and self.blob[0]>=0.4:
            return "Neutral"
        else:
            return "Negative"

    def speakOut(self):
        try:
            self.engine = pyttsx3.init()
            self.text=self.text_editor.get(1.0,'end-1c')
            self.engine.say("How are You")
            self.engine.runAndWait()
        except Exception:
            messagebox.showerror("Error!", "Can't Speak Right Now! I am Sleeping...")



    #Method For Audio Input
    def saySomething(self):
        try:
            self.takeAudio = self.notepadController.saySomething()
            if self.takeAudio == "":
                messagebox.showinfo("say again", "speech not recognized!!")
            elif self.takeAudio == 'hello':
                messagebox.showinfo("Hello", "How Can I Help You!")
            elif self.takeAudio == 'what can you do':
                messagebox.showinfo("Help", "I can perform operations like Save, Open, Close and many more.")
            elif self.takeAudio == 'open file':
                self.open_file()
            elif self.takeAudio == 'change background':
                self.change_theme()
            elif self.takeAudio == 'save file':
                self.save_file()
            elif self.takeAudio == 'new file':
                self.new_file()
            elif self.takeAudio == 'file save':
                self.save_as()
            elif self.takeAudio == 'close app':
                self.exit_func()
            elif self.takeAudio == 'text bold':
                self.change_bold()
            elif self.takeAudio == 'text italic':
                self.change_italic()
            elif self.takeAudio == 'search':
                self.find_func()
            elif self.takeAudio == 'hide status bar':
                self.hide_statusbar()
            elif self.takeAudio == 'hide toolbar':
                self.hide_toolbar()
            elif self.takeAudio:
                self.text_editor.insert(tk.INSERT,self.takeAudio+" ")
            else:
                messagebox.showerror("Error", "audio not matched")
        except Exception:
            messagebox.showerror("Error!", "Some problem in device!")

#Run Function
    def run(self):
        self.root.mainloop()


#Obtain Tk object and call run function
root = tk.Tk()
obj = Notepad(root)
obj.run()
