import tkinter as tk
import random

CHORDS = [1, 2, 3, 4, 5, 6, 7]

MAJOR_SCALE_NOTES = {
    "C": {1: "C", 2: "D", 3: "E", 4: "F", 5: "G", 6: "A", 7: "B"},
    "C#": {1: "C#", 2: "D#", 3: "E#", 4: "F#", 5: "G#", 6: "A#", 7: "B#"},
    "Db": {1: "Db", 2: "Eb", 3: "F", 4: "Gb", 5: "Ab", 6: "Bb", 7: "C"},
    "D": {1: "D", 2: "E", 3: "F#", 4: "G", 5: "A", 6: "B", 7: "C#"},
    "Eb": {1: "Eb", 2: "F", 3: "G", 4: "Ab", 5: "Bb", 6: "C", 7: "D"},
    "E": {1: "E", 2: "F#", 3: "G#", 4: "A", 5: "B", 6: "C#", 7: "D#"},
    "F": {1: "F", 2: "G", 3: "A", 4: "Bb", 5: "C", 6: "D", 7: "E"},
    "F#": {1: "F#", 2: "G#", 3: "A#", 4: "B", 5: "C#", 6: "D#", 7: "E#"},
    "Gb": {1: "Gb", 2: "Ab", 3: "Bb", 4: "Cb", 5: "Db", 6: "Eb", 7: "F"},
    "G": {1: "G", 2: "A", 3: "B", 4: "C", 5: "D", 6: "E", 7: "F#"},
    "Ab": {1: "Ab", 2: "Bb", 3: "C", 4: "Db", 5: "Eb", 6: "F", 7: "Gb"},
    "A": {1: "A", 2: "B", 3: "C#", 4: "D", 5: "E", 6: "F#", 7: "G#"},
    "Bb": {1: "Bb", 2: "C", 3: "D", 4: "Eb", 5: "F", 6: "G", 7: "A"},
    "B": {1: "B", 2: "C#", 3: "D#", 4: "E", 5: "F#", 6: "G#", 7: "A#"},
    "Cb": {1: "Cb", 2: "Db", 3: "Eb", 4: "Fb", 5: "Gb", 6: "Ab", 7: "Bb"},
}
MINOR_SCALE_NOTES = {
    "C": {1: "C", 2: "D", 3: "Eb", 4: "F", 5: "G", 6: "Ab", 7: "Bb"},
    "C#": {1: "C#", 2: "D#", 3: "E", 4: "F#", 5: "G#", 6: "A", 7: "B"},
    "Db": {1: "Db", 2: "Eb", 3: "Fb", 4: "Gb", 5: "Ab", 6: "Bbb", 7: "Cb"},
    "D": {1: "D", 2: "E", 3: "F", 4: "G", 5: "A", 6: "Bb", 7: "C"},
    "Eb": {1: "Eb", 2: "F", 3: "Gb", 4: "Ab", 5: "Bb", 6: "Cb", 7: "Db"},
    "E": {1: "E", 2: "F#", 3: "G", 4: "A", 5: "B", 6: "C", 7: "D"},
    "F": {1: "F", 2: "G", 3: "Ab", 4: "Bb", 5: "C", 6: "Db", 7: "Eb"},
    "F#": {1: "F#", 2: "G#", 3: "A", 4: "B", 5: "C#", 6: "D", 7: "E"},
    "Gb": {1: "Gb", 2: "Ab", 3: "Bbb", 4: "Cb", 5: "Db", 6: "Ebb", 7: "Fb"},
    "G": {1: "G", 2: "A", 3: "Bb", 4: "C", 5: "D", 6: "Eb", 7: "F"},
    "Ab": {1: "Ab", 2: "Bb", 3: "Cb", 4: "Db", 5: "Eb", 6: "Fb", 7: "Gbb"},
    "A": {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"},
    "Bb": {1: "Bb", 2: "C", 3: "Db", 4: "Eb", 5: "F", 6: "Gb", 7: "Ab"},
    "B": {1: "B", 2: "C#", 3: "D", 4: "E", 5: "F#", 6: "G", 7: "A"},
    "Cb": {1: "Cb", 2: "Db", 3: "Ebb", 4: "Fb", 5: "Gb", 6: "Abb", 7: "Bbb"},
}
HARMONIC_MINOR_SCALE_NOTES = {
    "C": {1: "C", 2: "D", 3: "Eb", 4: "F", 5: "G", 6: "Ab", 7: "B"},
    "C#": {1: "C#", 2: "D#", 3: "E", 4: "F#", 5: "G#", 6: "A", 7: "B#"},
    "Db": {1: "Db", 2: "Eb", 3: "Fb", 4: "Gb", 5: "Ab", 6: "Bbb", 7: "C"},
    "D": {1: "D", 2: "E", 3: "F", 4: "G", 5: "A", 6: "Bb", 7: "C#"},
    "Eb": {1: "Eb", 2: "F", 3: "Gb", 4: "Ab", 5: "Bb", 6: "Cb", 7: "D"},
    "E": {1: "E", 2: "F#", 3: "G", 4: "A", 5: "B", 6: "C", 7: "D#"},
    "F": {1: "F", 2: "G", 3: "Ab", 4: "Bb", 5: "C", 6: "Db", 7: "E"},
    "F#": {1: "F#", 2: "G#", 3: "A", 4: "B", 5: "C#", 6: "D", 7: "E#"},
    "Gb": {1: "Gb", 2: "Ab", 3: "Bbb", 4: "Cb", 5: "Db", 6: "Ebb", 7: "F"},
    "G": {1: "G", 2: "A", 3: "Bb", 4: "C", 5: "D", 6: "Eb", 7: "F#"},
    "Ab": {1: "Ab", 2: "Bb", 3: "Cb", 4: "Db", 5: "Eb", 6: "Fb", 7: "Gb"},
    "A": {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G#"},
    "Bb": {1: "Bb", 2: "C", 3: "Db", 4: "Eb", 5: "F", 6: "Gb", 7: "A"},
    "B": {1: "B", 2: "C#", 3: "D", 4: "E", 5: "F#", 6: "G", 7: "A#"},
    "Cb": {1: "Cb", 2: "Db", 3: "Ebb", 4: "Fb", 5: "Gb", 6: "Abb", 7: "Bb"},
}

SCALES = ['major', 'natural minor', 'harmonic minor']
CHORDS_IN_SCALE = {
    'major': ['', 'm', 'm', '', '', 'm', 'dim'],
    'natural minor': ['m', 'dim', '', 'm', 'm', '', ''],
    'harmonic minor': ['m', 'dim', '+5', 'm', '', '', 'dim']
}
CHORDS_IN_ROMAN_NUMERALS_BASED_ON_SCALES = {
    'major': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viidim'],
    'natural minor': ['i', 'iidim', 'III', 'iv', 'v', 'VI', 'VII'],
    'harmonic minor': ['i', 'iidim', 'IIIaug', 'iv', 'V', 'VI', 'VIIdim']
}
PATTERN_FONT = ('Arial', 36, 'bold')
TEMPO_FONT = ('Arial', 12, 'bold')
KEY_FONT = ('Arial', 24, 'bold')


def generate_pattern():
    # Clear text
    canvas.itemconfig(pattern_text, text='', font=PATTERN_FONT)
    canvas.itemconfig(key_text, text='', font=KEY_FONT)
    canvas.itemconfig(tempo_text, text='', font=TEMPO_FONT)

    # Generate pattern with chord names

    pattern_with_chord_names = []

    scale = SCALES[scale_value.get()]
    pattern_length = int(length_value.get())
    key = key_listbox.get(key_listbox.curselection())

    if scale == 'major' and include_dim_value.get() == 0:
        pattern = [random.choice(CHORDS[0:6]) for _ in range(pattern_length)]
    else:
        pattern = [random.choice(CHORDS) for _ in range(pattern_length)]

    for item in pattern:
        if scale == 'major':
            pattern_with_chord_names.append(f"{MAJOR_SCALE_NOTES[key][item]}{CHORDS_IN_SCALE[scale][item - 1]}")
        if scale == 'natural minor':
            pattern_with_chord_names.append(f"{MINOR_SCALE_NOTES[key][item]}{CHORDS_IN_SCALE[scale][item - 1]}")
        if scale == 'harmonic minor':
            pattern_with_chord_names.append(f"{HARMONIC_MINOR_SCALE_NOTES[key][item]}{CHORDS_IN_SCALE[scale][item - 1]}")

    # Pattern with numbers

    pattern_with_roman_numerals = []

    for item in pattern:
        pattern_with_roman_numerals.append(CHORDS_IN_ROMAN_NUMERALS_BASED_ON_SCALES[scale][item - 1])

    # Set text
    canvas.itemconfig(pattern_text, text=pattern_with_chord_names, font=PATTERN_FONT)
    canvas.itemconfig(key_text, text=f"Key: {key} {scale}", font=KEY_FONT)
    canvas.itemconfig(roman_text, text=pattern_with_roman_numerals, font=KEY_FONT)

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
roman_text = canvas.create_text(250, 150, text='[Roman]', font=KEY_FONT, fill='gray')

canvas.grid(row=0, column=0, columnspan=2)

# Labels

scale_label = tk.Label(text='Scale: ')
scale_label.grid(row=2, column=0)

key_label = tk.Label(text='Key: ')
key_label.grid(row=4, column=0)

length_label = tk.Label(text='Pattern length: ')
length_label.grid(row=5, column=0)

include_dim_label = tk.Label(text='Allow dim chord in major scale pattern: ')
include_dim_label.grid(row=7, column=0)

include_tempo_label = tk.Label(text='Include random tempo (50~150 bpm): ')
include_tempo_label.grid(row=8, column=0)

# Listbox

key_listbox = tk.Listbox(height=15)
# key_listbox.yview()
# key_listbox.yview_scroll(6, tk.UNITS)
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
key_listbox.grid(row=4, column=1)

# Radiobuttons

scale_value = tk.IntVar()

scale_major = tk.Radiobutton(text='major', var=scale_value, value=0)
scale_major.grid(row=1, column=1)
scale_natural_minor = tk.Radiobutton(text='natural minor', var=scale_value, value=1)
scale_natural_minor.grid(row=2, column=1)
scale_harmonic_minor = tk.Radiobutton(text='harmonic minor', var=scale_value, value=2)
scale_harmonic_minor.grid(row=3, column=1)

length_value = tk.IntVar()
length_2 = tk.Radiobutton(text='2', var=length_value, value=2)
length_2.grid(row=5, column=1)
length_4 = tk.Radiobutton(text='4', var=length_value, value=4)
length_4.grid(row=6, column=1)

# Checkbutton

include_dim_value = tk.IntVar()
include_dim_chkbutton = tk.Checkbutton(text="yes/no", var=include_dim_value, onvalue=1, offvalue=0)
include_dim_chkbutton.grid(row=7, column=1, columnspan=2)

include_tempo_value = tk.IntVar()
include_tempo_chkbutton = tk.Checkbutton(text="yes/no", var=include_tempo_value, onvalue=1, offvalue=0)
include_tempo_chkbutton.grid(row=8, column=1, columnspan=2)


# Button

generate_button = tk.Button(text='Generate pattern', width=50, command=generate_pattern)
generate_button.grid(row=9, column=0, columnspan=2)

window.mainloop()
