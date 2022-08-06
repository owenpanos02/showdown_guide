import tkinter as tk
from dict import gen5
from PIL import ImageTk, Image
    



root = tk.Tk()
root.title("Test GUI")
root.iconbitmap("4.ico")

root['background'] = '#adb8b0'


title_image = ImageTk.PhotoImage(Image.open("pokemonapp_title.png"))

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

title_image_label = tk.Label(root, image = title_image)
canvas1.create_window(200, 50, window = title_image_label)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def pkmnCheck():
    output = ''
    pokemonName = entry1.get()
    for key, value in gen5.items():
        if key == pokemonName:
            output += key + '\n'
            for k, v in value.items():
                if k != 'level':
                    output += (f"{k.upper()}:")
                    for entry in v:
                        if entry == v[-1]:
                            output += (entry + '\n')
                        else:
                            output += f" {entry} "

                else:
                    output += (f"{k}: {v}\n")

    output_text = tk.Label(root, text= output)
    canvas1.create_window(200, 250, window = output_text)
    
        
    


checkButton = tk.Button(root, text="Check Pokemon", command=pkmnCheck)
canvas1.create_window(200, 180, window= checkButton)


root.mainloop()