import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox, filedialog
import NotepadController as nc
import traceback


class Notepad:
    def __init__(self, root):
        self.root = root
        self.url = ''
        self.prev_text = ''
        self.text_changed = False
        self.show_statusbar = tk.BooleanVar()
        self.show_statusbar.set(True)
        self.show_toolbar = tk.BooleanVar()
        self.show_toolbar.set(True)
        self.notepadController = nc.Controller()
        self.root.geometry('1200x800')
        self.root.title('MyNotePad')
        self.root.wm_iconbitmap('icons/icon.ico')
        self.set_icons()
        self.set_menu_bar()
        self.set_tool_bar()
        self.set_file_sub_menu()
        self.set_view_sub_menu()
        self.set_edit_sub_menu()
        self.set_canvas()
        self.set_status_bar()

        self.set_file_menu_event_bindings()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_func)

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
        self.tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
        self.status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')
        self.light_default_icon = tk.PhotoImage(file='icons/light_default.png')
        self.light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
        self.dark_icon = tk.PhotoImage(file='icons/dark.png')
        self.red_icon = tk.PhotoImage(file='icons/red.png')
        self.monokai_icon = tk.PhotoImage(file='icons/monokai.png')
        self.night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

    def set_file_sub_menu(self):
        self.file.add_command(label='New', image=self.new_icon, compound=tk.LEFT, accelerator='Ctrl+N',
                              command=self.new_file)
        self.file.add_command(label='Open', image=self.open_icon, compound=tk.LEFT, accelerator='Ctrl+O',
                              command=self.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=tk.LEFT, accelerator='Ctrl+S',
                              command=self.save_file)
        self.file.add_command(label='Save As', image=self.save_as_icon, compound=tk.LEFT, accelerator='Alt+S',
                              command=self.save_as)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q',
                              command=self.exit_func)

    def set_menu_bar(self):
        self.main_menu = tk.Menu()
        self.file = tk.Menu(self.main_menu, tearoff=False)
        self.edit = tk.Menu(self.main_menu, tearoff=False)
        self.view = tk.Menu(self.main_menu, tearoff=False)
        self.color_theme = tk.Menu(self.main_menu, tearoff=False)

        self.main_menu.add_cascade(label='File', menu=self.file)
        self.main_menu.add_cascade(label='Edit', menu=self.edit)
        self.main_menu.add_cascade(label='View', menu=self.view)
        self.main_menu.add_cascade(label='Color Theme', menu=self.color_theme)
        self.root.config(menu=self.main_menu)

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
        self.text_editor.bind('<<Modified>>', self.text_changed)

    def set_status_bar(self):
        self.status_bar = ttk.Label(self.root, text='Status Bar')
        self.status_bar.pack(side=tk.BOTTOM)
        self.count = 0

    def set_file_menu_event_bindings(self):
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-N>", self.new_file)
        self.root.bind("<Control-O>", self.open_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-S>", self.save_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Alt-S>", self.save_as)
        self.root.bind("<Alt-s>", self.save_as)
        self.root.bind("<Control-q>", self.exit_func)
        self.root.bind("<Control-Q>", self.exit_func)

    def changed(self, event=None):
        words = len(self.text_editor.get(1.0, 'end-1c').split())
        characters = len(self.text_editor.get(1.0, 'end-1c'))
        self.set_status_bar.config(text=f'Characters: {characters} Words:{words}')
        if self.text_editor.edit_modified():
            self.text_changed = True
        self.text_editor.edit_modified(False)

    def exit_func(self, event=None):
        result = messagebox.askyesno("Quitting", "Are you sure you want to Quit?")
        if result == False:
            return
        try:
            if self.url == '':
                if len(self.text_editor.get("1.0", 'end-1c')) == 0:
                    self.text_changed = False
            if self.text_changed:
                mbox = messagebox.askyesno('Warning', 'Do you want to  quit?')
                if mbox == True:
                    content = self.text_editor.get(1.0, "end-1c")
                    if self.url == "":
                        self.save_dialog()
                        self.notepadController.save_file(content, self.url)
                    else:
                        self.notepadController.save_file(content, self.url)
            messagebox.showinfo("Have a Good Day", "Thank You for using Notepad")
            self.root.destroy()

        except:
            messagebox.showerror("Error", "Please Select a file to save")
            print(traceback.format_exc())

    def set_edit_sub_menu(self):
        self.edit.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                              command=lambda: self.text_editor.event_generate("<<Copy>>"))
        self.edit.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                              command=lambda: self.text_editor.event_generate("<<Paste>>"))
        self.edit.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                              command=lambda: self.text_editor.event_generate("<<Cut>>"))
        self.edit.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT, accelerator='Alt+X',
                              command=lambda: self.text_editor.delete(1.0, tk.END))
        self.edit.add_command(label='Find', image=self.find_icon, compound=tk.LEFT, accelerator='Ctrl+F',
                              command=lambda: self.find_func())

    def find_func(self, event=None):

        self.find_dialogue = tk.Toplevel()
        self.find_dialogue.geometry('450x250+500+200')
        self.find_dialogue.title('Find')
        self.find_dialogue.resizable(0, 0)

        self.find_frame = ttk.LabelFrame(self.find_dialogue, text='find/replace')
        self.find_frame.pack(pady=20)

        self.text_find_label = ttk.Label(self.find_frame, text='Find:')
        self.text_replace_label = ttk.Label(self.find_frame, text='Replace')

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

    def new_file(self):
        self.url = ''
        self.text_editor.delete(1.0, tk.END)
        self.root.title("MyNotePad")

    def save_file(self, event=None):
        try:
            content = self.text_editor.get(1.0, "end-1c")
            if self.url == "":
                self.save_dialog()
                self.notepadController.save_file(content, self.url)
                self.text_changed = False
            else:
                self.notepadController.save_file(content, self.url)
                self.text_changed
        except Exception:
            messagebox.showerror("Error!", "Please Select A File to Save")
            print(traceback.format_exc())

    def save_dialog(self):
        self.url = filedialog.asksaveasfilename(defaultextension='.ntxt',
                                                filetypes=([("All Files", "*.*"), ("Text Documents", "*.txt")]))

    def save_as(self):
        try:
            content = self.text_editor.get(1.0, "end-1c")
            self.save_dialog()
            self.notepadController.save_as(content, self.url)
            self.text_changed = False
        except Exception:
            messagebox.showerror("Error", "Please Select file to save")
            print(traceback.format_exc())

    def open_file(self):
        try:
            self.open_dialog()
            self.msg, self.base = self.notepadController.read_file(self.url)
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(1.0, self.msg)
            self.root.title(self.base)
            self.text_editor.edit_modified(False)
        except FileNotFoundError:
            messagebox.showerror("Error", "Please Select A File First")
            print(traceback.format_exc())

    def open_dialog(self):
        self.url = filedialog.askopenfile(title='Select File', filetypes=[("Test Docs", "*.*")])

    def find(self):
        word = self.find.input.get()
        self.text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:  # if word not equal to zero then we can write if word:,,,,,same for if not equal to false
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
            messagebox.showinfo("Word Found", f"{word} occurs {matches}times")

    def replace(self):
        word = self.find_input.get()
        self.replace_text = self.replace_input.get()
        self.content = self.text_editor.get(1.0, tk.END)
        self.new_content = self.content.replace(word, self.replace_text)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(1.0, self.new_content)

    def set_tool_bar(self):
        self.tool_bar = ttk.Label(self.root)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)

        self.font_tuple = tk.font.families()
        self.font_family = tk.StringVar()
        self.font_box = ttk.Combobox(self.tool_bar, width=30, textvariable=self.font_family, state='readonly')
        self.font_box['values'] = self.font_tuple
        self.font_box.current(self.font_tuple.index('Arial'))
        self.font_box.grid(row=0, column=0, padx=5)

        self.size_var = tk.IntVar()
        self.font_size = ttk.Combobox(self.tool_bar, width=14, textvariable=self.size_var, state='readonly')
        self.font_size['values'] = tuple(range(8, 81))
        self.font_size.current(4)
        self.font_size.grid(row=0, column=1, padx=5)

        self.bold_icon = tk.PhotoImage(file='icons/bold.png')
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon, command=self.change_bold)
        self.bold_btn.grid(row=0, column=2, padx=5)

        self.italic_icon = tk.PhotoImage(file='icons/italic.png')
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon, command=self.change_italic)
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

        self.mic_icon = tk.PhotoImage(file='icons/align_left.png')
        self.mic_btn = ttk.Button(self.tool_bar, image=self.mic_icon)
        self.mic_btn.grid(row=0, column=9, padx=5)

    def change_font(self, event=None):
        self.current_font_family = self.font_family.get()
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_font_size(self, event=None):
        self.current_font_family = self.size_var.get()
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_bold(self):
        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property['weight'] == 'normal':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'bold'))
        else:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def change_italic(self):
        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property['slant'] == 'roman':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'italic'))
        else:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'roman'))

    def change_bold(self):
        self.text_property = tk.font.Font(font=self.text_editor['font'])
        if self.text_property['underline'] == 1:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 0))
        else:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 1))

    def change_font_color(self):
        color_var = tk.colorchooser.askcolor()
        self.text_editor.configure(fg=color_var[1])

    def align_left(self):
        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('left', justify=tk.LEFT)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'left')

    def align_right(self):
        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('right', justify=tk.RIGHT)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'right')

    def align_center(self):
        text_content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('center', justify=tk.CENTER)
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(tk.INSERT, text_content, 'center')

    def set_view_sub_menu(self):
        self.view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False, variable=self.show_toolbar,
                                  image=self.tool_bar_icon, compound=tk.LEFT, command=self.hide_toolbar)
        self.view.add_checkbutton(label='Status Bar', onvalue=True, offvalue=False, variable=self.show_statusbar,
                                  image=self.status_bar_icon, compound=tk.LEFT, command=self.hide_statusbar)

    def hide_statusbar(self):
        if self.show_statusbar:
            self.status_bar.pack_forget()
            self.show_statusbar=False

        else:
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_statusbar=True

    def hide_toolbar(self):
        if self.show_toolbar:
            self.tool_bar.pack_forget()
            self.show_toolbar = False

        else:
            self.text_editor.pack_forget()
            self.status_bar.pack_forget()
            self.tool_bar.pack(side=tk.TOP,fill=tk.X)
            self.text_editor.pack(fill=tk.BOTH,expand=True)
            self.status_bar.pack(side=tk.BOTTOM)
            self.show_toolbar = True




    def saySomthing(self):
        try:
            self.takeAudio=self.notepadController.saysomeThing()
            if self.takeAudio=="":
                messagebox.showinfo("say again","speech not recognized!")
            elif self.takeAudio=='open file':
                self.open_file()
            elif self.takeAudio == 'save file':
                 self.save_file()
            elif self.takeAudio == 'close file':
                self.exit_func()
            else:
                 messagebox.showerror("Error", "audio not matched")
        except:
            messagebox.showerror("Error", "Some  error occurred.Please try again ")












    def run(self):
        self.root.mainloop()


root = tk.Tk()
obj = Notepad(root)
obj.run()

'''
quit functionality
>>>>>>>>>>>>
open clicked not selected
find color change

'''
