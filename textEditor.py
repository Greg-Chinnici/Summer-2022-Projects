import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saveFile():
    #save the current file as a new file, new name
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("Markdown Files", "*.md*")],)
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    screen.title(f"GregEditor >> {filepath}")

def openFile():
    #opens file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Markdown Files", "*.md*")])
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    screen.title(f"GregEditor >> {filepath}")

screen = tk.Tk()
screen.title("GregEditor")
screen.rowconfigure(0, minsize=800, weight=1)
screen.columnconfigure(1, minsize=400, weight=1)

txt_edit = tk.Text(screen)
fr_buttons = tk.Frame(screen, relief=tk.RAISED, bd=3)
btn_open = tk.Button(fr_buttons, text="Open", command=openFile)
btn_save = tk.Button(fr_buttons, text="Save As", command=saveFile)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

screen.mainloop()
