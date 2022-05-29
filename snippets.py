
# cv.imshow('Input', boards_input_img)
# cv.imshow('Optimized', boards_optimized_img)

# cv.imwrite('input.jpg', boards_input_img)
# cv.imwrite('output.jpg', boards_optimized_img)

# input_img = ImageTk.PhotoImage(Image.open('input.jpg'))
# output_img = ImageTk.PhotoImage(Image.open('output.jpg'))

# input_img_label = tk.Label(image=input_img)
# output_img_label = tk.Label(image=output_img)

# input_img_label.pack()
# output_img_label.pack()

lamellae_before = [[]]

# functions:
def makeSubsection():
    quality_validation.grid_forget()
    length_validation.grid_forget()
    quality_missing.grid_forget()
    if (not quality_entry.get()):
        quality_missing.grid(row=3, column=3)
        return
    length = int(length_entry.get())
    
    if (not quality_entry.get().isnumeric()):
        quality_validation.grid(row=3, column=3)
        return 
    quality = int(quality_entry.get())
    if (quality <1 or quality > 4):
        quality_validation.grid(row=3, column=3)
        return 
    if (length == ''):
        length_validation.grid(row=3, column=3)
        return
    lamellae_before[0].append([quality,length])
    length_entry.delete(0,'end')
    quality_entry.delete(0,'end')
    print(lamellae_before)
    inputListDisplay = tk.Label(root, text='lamella: ' + str(lamellae_before))
    inputListDisplay.grid(row=9,column=1)


def enter_board():
    boards_before = [[]]
    for widget in board_frame.winfo_children():
        widget.destroy()
    warning.grid_forget()
    
    try:   
        arr = array_entry.get()
        arr = ast.literal_eval(arr) 
        for item in arr:
            quality = item[0]
            length = item[1]
            boards_before[0].append([quality,length])
        print(boards_before)
        inputListDisplay = tk.Label(root, text='lamella: ' + str(boards_before))
        inputListDisplay.grid(row=9,column=1)
    except:
        warning.grid(row=7, column=3)
    array_entry.delete(0,'end')

def make_board():
    pass

def display_images():
    pass
    # global lamellae_before 
    # before_img, after_img = vi.get_images(lamellae_before, lamellae_after)
    # print(before_img[0])
    # lamellae_before= [[]]
    # cv.imshow('before', before_img[0])
    # cv.imshow('after',after_img[1])
    # cv.imwrite("uncut.jpg", before_img[0])
    # cv.imwrite("cut.jpg", after_img[1])

    # uncut_img = ImageTk.PhotoImage(Image.open('uncut.jpg'))
    # before_label = tk.Label(image=uncut_img)
    # before_label.grid(row=3,column=5)
    # cut_img = ImageTk.PhotoImage(Image.open('cut.jpg'))
    # after_label = tk.Label(image=cut_img)
    # after_label.grid(row=4,column=5)
    


def clear_board():
    for widget in board_frame.winfo_children():
        widget.destroy()

def getLamellae():
    return lamellae_before



subsection_announcement1 = tk.Label(root, text="Create a custom board! Input quality and length individually:", padx=10,pady=10)
subsection_announcement1.grid(row=1, column=1, columnspan=2)

quality_label = tk.Label(root, text="Which quality?", padx=10)
quality_label.grid(row=2, column=1)

quality_entry = tk.Entry(root)
quality_entry.grid(row=2,column=2)

length_label = tk.Label(root, text="Which length?")
length_label.grid(row=3,column=1)

length_entry = tk.Entry(root)
length_entry.grid(row=3,column=2)

quality_validation = tk.Label(root, text="Quality must be 1,2,3 or 4!", fg='red')
quality_missing = tk.Label(root, text="You did not enter a quality (1,2,3,4)", fg='red')
length_validation = tk.Label(root, text="Enter a valid length!", fg='red')


submit_button1 = tk.Button(root, text="Make subsection", command=makeSubsection)
submit_button1.grid(row=4, column=1, columnspan=2, pady=20)

whole_announcement= tk.Label(root, text="OR enter all the qualities and lengths as a 2-dim array:", padx=10,pady=10)
whole_announcement.grid(row=5, column=1, columnspan=2)

usage_announcement= tk.Label(root, text=" [[quality, length],[quality,length],...]:")
usage_announcement.grid(row=6, column=1, columnspan=2)

array_entry = tk.Entry(root)
array_entry.grid(row=7, column=1, columnspan=2)

enter_board = tk.Button(root, text="Enter board", command=enter_board)
enter_board.grid(row=8, column=1, columnspan=2, pady=5)

warning = tk.Label(root, text="Wrong input, use [[q,l],[q,l]]", fg='red')

filler = tk.Label(root, text="                                ")
filler.grid(row=1,column=3)

board_frame = tk.Frame(root, height=120, width=700)
board_frame.grid(row= 4, column=4)

announcement4 = tk.Label(root, text="Board: Before")
announcement4.grid(row=1,column=4)

make_board = tk.Button(root, text="Make board", command=make_board)
make_board.grid(row=5, column=3)
clear_button = tk.Button(root, text="Clear board", command=clear_board)
clear_button.grid(row=6, column=3)
