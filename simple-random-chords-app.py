import tkinter as tk
import random

CHORDS = [1, 2, 3, 4, 5, 6, 7]
CHORD_NAMES_IN_KEY = {
    "C": {1: "C", 2: "Dm", 3: "Em", 4: "F", 5: "G", 6: "Am", 7: "Bdim"},
    "C#": {1: "C#", 2: "D#m", 3: "E#m", 4: "F#", 5: "G#", 6: "A#m", 7: "B#dim"},
    "Db": {1: "Db", 2: "Ebm", 3: "Fm", 4: "Gb", 5: "Ab", 6: "Bbm", 7: "Cdim"},
    "D": {1: "D", 2: "Em", 3: "F#m", 4: "G", 5: "A", 6: "Bm", 7: "C#dim"},
    "Eb": {1: "Eb", 2: "Fm", 3: "Gm", 4: "Ab", 5: "Bb", 6: "Cm", 7: "Ddim"},
    "E": {1: "E", 2: "F#m", 3: "G#m", 4: "A", 5: "B", 6: "C#m", 7: "D#dim"},
    "F": {1: "F", 2: "Gm", 3: "Am", 4: "Bb", 5: "C", 6: "Dm", 7: "Edim"},
    "F#": {1: "F#", 2: "G#m", 3: "A#m", 4: "B", 5: "C#", 6: "D#m", 7: "E#dim"},
    "Gb": {1: "Gb", 2: "Abm", 3: "Bbm", 4: "Cb", 5: "Db", 6: "Ebm", 7: "Fdim"},
    "G": {1: "G", 2: "Am", 3: "Bm", 4: "C", 5: "D", 6: "Em", 7: "F#dim"},
    "G#": {1: "G#", 2: "A#m", 3: "B#m", 4: "C#", 5: "D#", 6: "E#m", 7: "Gdim"},
    "Ab": {1: "Ab", 2: "Bbm", 3: "Cm", 4: "Db", 5: "Eb", 6: "Fm", 7: "Gbdim"},
    "A": {1: "A", 2: "Bm", 3: "C#m", 4: "D", 5: "E", 6: "F#m", 7: "G#dim"},
    "Bb": {1: "Bb", 2: "Cm", 3: "Dm", 4: "Eb", 5: "F", 6: "Gm", 7: "Adim"},
    "B": {1: "B", 2: "C#m", 3: "D#m", 4: "E", 5: "F#", 6: "G#m", 7: "A#dim"},
    "Cb": {1: "Cb", 2: "Dbm", 3: "Ebm", 4: "Fb", 5: "Gb", 6: "Abm", 7: "Bbdim"},
}
PATTERN_FONT = ('Arial', 40, 'bold')
TEMPO_FONT = ('Arial', 12, 'bold')
KEY_FONT = ('Arial', 24, 'bold')


def generate_pattern():
    # Clear text
    canvas.itemconfig(pattern_text, text='', font=PATTERN_FONT)
    canvas.itemconfig(key_text, text='', font=KEY_FONT)
    canvas.itemconfig(tempo_text, text='', font=TEMPO_FONT)

    # Generate pattern
    pattern_with_chord_names = []

    pattern_length = int(length_value.get())
    key = key_listbox.get(key_listbox.curselection())

    if include_dim_value.get() == 1:
        pattern = [random.choice(CHORDS) for _ in range(pattern_length)]
    elif include_dim_value.get() == 0:
        pattern = [random.choice(CHORDS[0:6]) for _ in range(pattern_length)]

    for name in CHORD_NAMES_IN_KEY[key]:
        for chord in pattern:
            if chord == name:
                pattern_with_chord_names.append(CHORD_NAMES_IN_KEY[key][name])

    # Set text
    canvas.itemconfig(pattern_text, text=pattern_with_chord_names, font=PATTERN_FONT)
    canvas.itemconfig(key_text, text=f"Key: {key}", font=KEY_FONT)

    if include_tempo_value.get() == 1:
        random_tempo = random.randint(50,150)
        canvas.itemconfig(tempo_text, text=f"Tempo: {random_tempo}", font=TEMPO_FONT)

    # Set focus to generate button
    generate_button.focus()

# Window

window = tk.Tk()
window.title('Simple Random Chord Pattern App')
window.config(padx=50, pady=50)

# Canvas

canvas = tk.Canvas(width=500, height=200)
pattern_text = canvas.create_text(250, 100, text='[Pattern]', font=PATTERN_FONT)
tempo_text = canvas.create_text(250, 50, text='[Tempo]', font=TEMPO_FONT)
key_text = canvas.create_text(250, 20, text='[Key]', font=KEY_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Labels

key_label = tk.Label(text='Key: ', anchor='n')
key_label.grid(row=1, column=0)

length_label = tk.Label(text='Pattern length:')
length_label.grid(row=2, column=0)

include_dim_label = tk.Label(text='Allow dim chord in pattern:')
include_dim_label.grid(row=4, column=0)

include_tempo_label = tk.Label(text='Include random tempo (50~150 bpm):')
include_tempo_label.grid(row=5, column=0)

# Listbox

key_listbox = tk.Listbox(height=15)
key_listbox.yview()
key_listbox.yview_scroll(6, tk.UNITS)
key_listbox.insert(1, 'Cb')
key_listbox.insert(2, 'Gb')
key_listbox.insert(3, 'Db')
key_listbox.insert(4, 'Ab')
key_listbox.insert(5, 'Eb')
key_listbox.insert(6, 'Bb')
key_listbox.insert(7, 'F')
key_listbox.insert(8, 'C')
key_listbox.insert(9, 'G')
key_listbox.insert(10, 'D')
key_listbox.insert(11, 'A')
key_listbox.insert(12, 'E')
key_listbox.insert(13, 'B')
key_listbox.insert(14, 'F#')
key_listbox.insert(15, 'C#')
key_listbox.grid(row=1, column=1)

# Radiobuttons

length_value = tk.IntVar()
length_2 = tk.Radiobutton(text='2', var=length_value, value=2)
length_2.grid(row=2, column=1)
length_4 = tk.Radiobutton(text='4', var=length_value, value=4)
length_4.grid(row=3, column=1)


# Checkbutton

include_dim_value = tk.IntVar()
include_dim_chkbutton = tk.Checkbutton(text="yes/no", var=include_dim_value, onvalue=1, offvalue=0)
include_dim_chkbutton.grid(row=4, column=1, columnspan=2)

include_tempo_value = tk.IntVar()
include_tempo_chkbutton = tk.Checkbutton(text="yes/no", var=include_tempo_value, onvalue=1, offvalue=0)
include_tempo_chkbutton.grid(row=5, column=1, columnspan=2)


# Button

generate_button = tk.Button(text='Generate pattern', width=50, command=generate_pattern)
generate_button.grid(row=6, column=0, columnspan=2)

window.mainloop()
