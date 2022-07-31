import tkinter as tk
from tkinter import *
# Pillow Library is imported for use with loading images into tkinter window
from PIL import ImageTk, Image


# count_down function will be useful to close the program after the user has ordered their sandwich
def count_down(time):
    # Once the time is less than 0 (time has run out) the program will close
    if time == -1:
        window.destroy()
    else:
        countDownLabel.configure(text="Window Closing In: " + str(time))
    # After 1000 milliseconds (1 second) the time is decremented by 1
    window.after(1000, count_down, time - 1)


# frame_destroy will only be called once the order has been completed; destroys all previous frames
def frame_destroy():
    topBar.destroy()
    breadFrame.destroy()
    meatFrame.destroy()
    toppingsFrame.destroy()
    drinkFrame.destroy()
    orderFrame.destroy()


# show_frame function passes through the current frame and raises it to the top to allow frames to be used as
# separate tabs
def show_frame(frame):
    frame.tkraise()
    if frame == purchaseCompleteFrame:
        purchaseCompleteFrame.grid(row=0, column=0, sticky="nsew")
        frame_destroy()
        count_down(5)


# Basic window attributes are set
window = tk.Tk()
window.geometry("800x600")
window.title("Sandwich Designer")
window.iconbitmap("images\sandwich.ico")
window.resizable(False, False)

# topBar frame holds the navigation bar for the gui and is placed on a different row so that it is always visible
topBar = Frame(window)
topBar.configure(bg="#262626", height=50, width=800)
topBar.grid(row=0, column=0)

# Nav Bar items
breadBtn = Button(topBar, text="Bread Type", font=("Arial", 12), bg="#262626", fg="white", bd=0,
                  # show_frame function is called with the argument of the frames name that is selected
                  command=lambda: show_frame(breadFrame))
breadBtn.place(x=240, y=12)
meatsBtn = Button(topBar, text="Meats", font=("Arial", 12), bg="#262626", fg="white", bd=0,
                  command=lambda: show_frame(meatFrame))
meatsBtn.place(x=340, y=12)
toppingBtn = Button(topBar, text="Toppings", font=("Arial", 12), bg="#262626", fg="white", bd=0,
                    command=lambda: show_frame(toppingsFrame))
toppingBtn.place(x=402, y=12)
drinkBtn = Button(topBar, text="Drink", font=("Arial", 12), bg="#262626", fg="white", bd=0,
                  command=lambda: show_frame(drinkFrame))
drinkBtn.place(x=485, y=12)

# Each page's frame is defined and placed onto the window
# 50 pixel gap is taken from the total height of the frame to allocate enough space for the order button
breadFrame = tk.Frame(window, width=350, height=550)
meatFrame = tk.Frame(window, width=350, height=550)
toppingsFrame = tk.Frame(window, width=350, height=550)
drinkFrame = tk.Frame(window, width=350, height=550)
orderFrame = tk.Frame(window, width=350, height=550)
purchaseCompleteFrame = tk.Frame(window, width=800, height=600)
# All the frames except for purchaseCompleteFrame are placed on the same row and in the exact same position
for frame in (breadFrame, meatFrame, toppingsFrame, drinkFrame, orderFrame):
    # Frames are stickied; they stretch to fill the window accordingly
    frame.grid(row=1, column=0, sticky="nsew")


# SelectedBread accepts arguments for breadType (variable's name) and itemName (string value that corresponds with img)
# which is useful for displaying images using concatenation
def selectedBread(breadType, itemName):
    # BreadItems list holds the  names of all the variables so that they can be reset to original color
    # (ensures that only one button is shown as being selected at a time)
    breadItems = [wheatBread, whiteBread, italianBread, parmesanBread]
    for i in breadItems:
        i.configure(background="#262626", fg="white")
    # The bread option the user clicked is displayed with a different bg color and font color
    breadType["bg"] = "#C52D2D"
    breadType["fg"] = "white"
    # Global variable which holds the bread image is declared so that the variable's value can be accessed outside
    # this function's scope
    global brdImg
    # BreadImgLabel is destroyed (placeholder image before a user makes their own selection)
    breadImgLabel.destroy()
    # Concatenated string is used to open the correct image using the itemName argument
    brdImg = ImageTk.PhotoImage(Image.open("images\\" + itemName + ".jpg"))
    brdImgLabel = Label(breadFrame, image=brdImg, width=300, height=300)
    brdImgLabel.place(x=420, y=50)


# Empty lists are created which will be later store values relating to the user's selection under each category
bread_type = []
meat_type = []
drink_type = []
store_toppings = []


def orderValidate():
    # If bread_type and meat_type are no longer empty then the user can proceed to the order window
    if len(bread_type) > 0 and len(meat_type) > 0:
        # Order buttons states are changed to active meaning they can be clicked
        orderBtn["state"] = "active"
        orderBtn2["state"] = "active"
        orderBtn3["state"] = "active"
        orderBtn4["state"] = "active"


def storeBread(name):
    if len(bread_type) > 0:
        # If the bread_type list isn't empty it is cleared since there can only be one selection for bread made
        bread_type.remove(bread_type[0])
    # The users choice of bread (name argument) is sent to the bread_type list
    bread_type.append(name)
    breadLabel["text"] = "Bread: " + str(bread_type[0]).capitalize()
    # OrderValidate function is called to see if the user has selected a bread type and meat type
    orderValidate()


def storeMeat(name):
    if len(meat_type) > 0:
        meat_type.remove(meat_type[0])
    meat_type.append(name)
    meatLabel["text"] = "Meat: " + str(meat_type[0]).capitalize()
    meatLabel.pack()
    orderValidate()


# Logic to determine selected bread is used for selected meat
def selectedMeat(meatType, itemName):
    meatVars = [turkeyBtn, hamBtn, beefBtn, chickenBtn]
    for i in meatVars:
        i.configure(background="#262626", fg="white")
    meatType["bg"] = "#C52D2D"
    meatType["fg"] = "white"
    global img
    meatImgLabel.destroy()
    img = ImageTk.PhotoImage(Image.open("images\\" + itemName + ".jpg"))
    imgLabel = Label(meatFrame, image=img, width=300, height=300)
    imgLabel.place(x=420, y=50)


def selectedDrink(drinkType, drinkName):
    if len(drink_type) > 0:
        drink_type.remove(drink_type[0])
    drink_type.append(drinkType)
    drinkVars = [pepsiBtn, spriteBtn, lemonadeBtn, waterBtn, rootbeerBtn, orangeJuiceBtn]
    for i in drinkVars:
        i.configure(background="#262626", fg="white")
    drinkName["bg"] = "#C52D2D"
    drinkName["fg"] = "white"
    drinkLabel["text"] = "Drink Selected: " + drinkType


def validate_toppings():
    # ToppingVars stores the IntValue for all the buttons (0, or 1); is used to determine if the user has selected
    # a button or not
    toppingVars = [picklesBtn, cheddarBtn, lettuceBtn, tomatoesBtn, avocadoBtn, baconBtn, mustardBtn, mayonnaiseBtn]
    # CheckButtonIndex stores the variables which hold the information about each button (e.g. button text)
    checkButtonIndex = [picklesValue, cheddarValue, lettuceValue, tomatoesValue, avocadoValue, baconValue, mustardValue,
                        mayonnaiseValue]
    # A counter variable is created so that the index of a variable can be retrieved from the counter's value
    checkButtonCounter = 0
    # Store_toppings list is cleared just in case a user goes back to the toppings page and makes change
    # (Just makes sure that list items aren't repeated)
    store_toppings.clear()
    # The toppingsHeader and toppingsLabel text are set to nothing by default and only changed if a user actually
    # chooses one or more toppings
    toppingsHeader["text"] = ""
    toppingsLabel["text"] = ""
    for i in toppingVars:
        # If the button is checked or not (if 1 then true)
        if toppingVars[checkButtonCounter].get():
            toppingsHeader["text"] = "Toppings: "
            # The text value is gotten from the current checkButtonIndex by passing through the counter variable
            store_toppings.append(checkButtonIndex[checkButtonCounter].cget("text"))
            checkButtonCounter += 1
            res = [*set(store_toppings)]
            # A "+" is added at the beginning of every item
            userToppings = ["+" + i for i in res]
            # The toppingsLabel is reformatted so things look prettier
            toppingsLabel["text"] = " " + str(userToppings).replace('[', '').replace(']', '').replace("'", "").replace(
                ",",
                "\n")
            # ToppingsLabel is justified to the left instead of center so that there is proper
            # alignment between the items
            toppingsLabel.configure(justify=LEFT)
        else:
            checkButtonCounter += 1


# Default unselected image (question mark graphic) for the bread and meat pages
breadImg = ImageTk.PhotoImage(Image.open("images\questionMark.png"))
breadImgLabel = Label(breadFrame, image=breadImg, width=300, height=300)
breadImgLabel.place(x=420, y=60)

meatImg = ImageTk.PhotoImage(Image.open("images\questionMark.png"))
meatImgLabel = Label(meatFrame, image=meatImg, width=300, height=300)
meatImgLabel.place(x=420, y=60)

# Bread page items
wheatBread = tk.Button(breadFrame, text="Wheat Bread", font=("Arial", 14), width=15, bg="#262626", fg="white",
                       command=lambda: [selectedBread(wheatBread, "wheatBread"), storeBread("wheat")])
wheatBread.pack(side=TOP, anchor=NW, padx=100, pady=(120, 0))
whiteBread = tk.Button(breadFrame, text="White Bread", font=("Arial", 14), width=15, bg="#262626", fg="white",
                       command=lambda: [selectedBread(whiteBread, "whiteBread"), storeBread("white")])
whiteBread.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
italianBread = tk.Button(breadFrame, text="Italian Bread", font=("Arial", 14), width=15, bg="#262626", fg="white",
                         command=lambda: [selectedBread(italianBread, "italianBread"), storeBread("italian")])
italianBread.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
parmesanBread = tk.Button(breadFrame, text="Parmesan Bread", font=("Arial", 14), width=15, bg="#262626", fg="white",
                          command=lambda: [selectedBread(parmesanBread, "parmesanBread"), storeBread("parmesan")])
parmesanBread.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
orderBtn = tk.Button(breadFrame, text="Place Order", font=("Arial", 16), bg="#751E87", fg="white", state="disabled",
                     activeforeground="white", activebackground="#751E87",
                     command=lambda: [show_frame(orderFrame), validate_toppings()])
orderBtn.place(x=560, y=450)

# Meat page items
turkeyBtn = tk.Button(meatFrame, text="Turkey", font=("Arial", 14), width=15, bg="#262626", fg="white",
                      command=lambda: [selectedMeat(turkeyBtn, "turkeyImg"), storeMeat("turkey")])
turkeyBtn.pack(side=TOP, anchor=NW, padx=100, pady=(120, 0))
hamBtn = tk.Button(meatFrame, text="Ham", font=("Arial", 14), width=15, bg="#262626", fg="white",
                   command=lambda: [selectedMeat(hamBtn, "hamImg"), storeMeat("ham")])
hamBtn.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
beefBtn = tk.Button(meatFrame, text="Roast Beef", font=("Arial", 14), width=15, bg="#262626", fg="white",
                    command=lambda: [selectedMeat(beefBtn, "beefImg"), storeMeat("beef")])
beefBtn.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
chickenBtn = tk.Button(meatFrame, text="Chicken", font=("Arial", 14), width=15, bg="#262626", fg="white",
                       command=lambda: [selectedMeat(chickenBtn, "chickenImg"), storeMeat("chicken")])
chickenBtn.pack(side=TOP, anchor=NW, padx=100, pady=(10, 0))
orderBtn2 = tk.Button(meatFrame, text="Place Order", font=("Arial", 16), bg="#751E87", fg="white", state="disabled",
                      activeforeground="white", activebackground="#751E87",
                      command=lambda: [show_frame(orderFrame), validate_toppings()])
orderBtn2.place(x=560, y=450)

# Toppings page items
toppingBG = ImageTk.PhotoImage(Image.open("images\\toppings_bg.jpg"))
toppingBGLabel = Label(toppingsFrame, image=toppingBG, width=234, height=327)
toppingBGLabel.place(x=80, y=50)

toppingImg = ImageTk.PhotoImage(Image.open("images\\toppingsImg.jpg"))
toppingImgLabel = Label(toppingsFrame, image=toppingImg, width=405, height=327)
toppingImgLabel.place(x=314, y=50)

picklesBtn = IntVar()
picklesValue = tk.Checkbutton(toppingsFrame, text="Pickles", variable=picklesBtn, font=("Arial", 14), bg="#2a2a2a",
                              fg="white",
                              selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
picklesValue.pack(anchor=W, padx=100, pady=(70, 0))
cheddarBtn = IntVar()
cheddarValue = tk.Checkbutton(toppingsFrame, text="Shredded Cheddar", variable=cheddarBtn, font=("Arial", 14),
                              bg="#2a2a2a",
                              fg="white",
                              selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
cheddarValue.pack(anchor=W, padx=100)

lettuceBtn = IntVar()
lettuceValue = tk.Checkbutton(toppingsFrame, text="Lettuce", variable=lettuceBtn, font=("Arial", 14), bg="#2a2a2a",
                              fg="white",
                              selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
lettuceValue.pack(anchor=W, padx=100)

tomatoesBtn = IntVar()
tomatoesValue = tk.Checkbutton(toppingsFrame, text="Tomatoes", variable=tomatoesBtn, font=("Arial", 14), bg="#2a2a2a",
                               fg="white",
                               selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
tomatoesValue.pack(anchor=W, padx=100)
avocadoBtn = IntVar()
avocadoValue = tk.Checkbutton(toppingsFrame, text="Avocado Slices", variable=avocadoBtn, font=("Arial", 14),
                              bg="#2a2a2a",
                              fg="white",
                              selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
avocadoValue.pack(anchor=W, padx=100)
baconBtn = IntVar()
baconValue = tk.Checkbutton(toppingsFrame, text="Bacon", variable=baconBtn, font=("Arial", 14), bg="#2a2a2a",
                            fg="white",
                            selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
baconValue.pack(anchor=W, padx=100)
mustardBtn = IntVar()
mustardValue = tk.Checkbutton(toppingsFrame, text="Mustard", variable=mustardBtn, font=("Arial", 14), bg="#2a2a2a",
                              fg="white",
                              selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
mustardValue.pack(anchor=W, padx=100)
mayonnaiseBtn = IntVar()
mayonnaiseValue = tk.Checkbutton(toppingsFrame, text="Mayonnaise", variable=mayonnaiseBtn, font=("Arial", 14),
                                 bg="#2a2a2a",
                                 fg="white",
                                 selectcolor="#000000", activebackground="#2a2a2a", activeforeground="#ffffff")
mayonnaiseValue.pack(anchor=W, padx=100)
orderBtn3 = tk.Button(toppingsFrame, text="Place Order", font=("Arial", 16), bg="#751E87", fg="white", state="disabled",
                      activeforeground="white", activebackground="#751E87",
                      command=lambda: [show_frame(orderFrame), validate_toppings()])
orderBtn3.place(x=560, y=450)

# Drink items
pepsiBtn = tk.Button(drinkFrame, text="Diet Pepsi", font=("Arial", 14), width=12, bg="#262626", fg="white",
                     command=lambda: selectedDrink("Diet Pepsi", pepsiBtn))
pepsiBtn.place(x=130, y=150)
spriteBtn = tk.Button(drinkFrame, text="Sprite", font=("Arial", 14), width=12, bg="#262626", fg="white",
                      command=lambda: selectedDrink("Sprite", spriteBtn))
spriteBtn.place(x=330, y=150)
lemonadeBtn = tk.Button(drinkFrame, text="Lemonade", font=("Arial", 14), width=12, bg="#262626", fg="white",
                        command=lambda: selectedDrink("Lemonade", lemonadeBtn))
lemonadeBtn.place(x=530, y=150)
waterBtn = tk.Button(drinkFrame, text="Water", font=("Arial", 14), width=12, bg="#262626", fg="white",
                     command=lambda: selectedDrink("Water", waterBtn))
waterBtn.place(x=130, y=350)
rootbeerBtn = tk.Button(drinkFrame, text="Root Beer", font=("Arial", 14), width=12, bg="#262626", fg="white",
                        command=lambda: selectedDrink("Root beer", rootbeerBtn))
rootbeerBtn.place(x=330, y=350)
orangeJuiceBtn = tk.Button(drinkFrame, text="Orange Juice", font=("Arial", 14), width=12, bg="#262626", fg="white",
                           command=lambda: selectedDrink("Orange Juice", orangeJuiceBtn))
orangeJuiceBtn.place(x=530, y=350)

pepsiImg = ImageTk.PhotoImage(Image.open("images\\pepsiImg.jpg"))
pepsiImgLabel = Label(drinkFrame, image=pepsiImg, width=100, height=100, bd=0)
pepsiImgLabel.place(x=150, y=40)
spriteImg = ImageTk.PhotoImage(Image.open("images\\spriteImg.jpg"))
spriteImgLabel = Label(drinkFrame, image=spriteImg, width=100, height=100)
spriteImgLabel.place(x=350, y=40)
lemonadeImg = ImageTk.PhotoImage(Image.open("images\\lemonadeImg.jpg"))
lemonadeImgLabel = Label(drinkFrame, image=lemonadeImg, width=100, height=100)
lemonadeImgLabel.place(x=550, y=40)
waterImg = ImageTk.PhotoImage(Image.open("images\\waterImg.jpg"))
waterImgLabel = Label(drinkFrame, image=waterImg, width=100, height=100)
waterImgLabel.place(x=150, y=240)
rootbeerImg = ImageTk.PhotoImage(Image.open("images\\rootbeerImg.jpg"))
rootbeerImgLabel = Label(drinkFrame, image=rootbeerImg, width=100, height=100)
rootbeerImgLabel.place(x=350, y=240)
orangeJuiceImg = ImageTk.PhotoImage(Image.open("images\\orangejuiceImg.jpg"))
orangeJuiceImgLabel = Label(drinkFrame, image=orangeJuiceImg, width=100, height=100)
orangeJuiceImgLabel.place(x=550, y=240)
orderBtn4 = tk.Button(drinkFrame, text="Place Order", font=("Arial", 16), bg="#751E87", fg="white", state="disabled",
                      activeforeground="white", activebackground="#751E87",
                      command=lambda: [show_frame(orderFrame), validate_toppings()])
orderBtn4.place(x=560, y=450)

# Order page items
testLabel = tk.Label(orderFrame, text="Does everything look correct?" + "\n" + ("-" * 30), font=("Arial Bold", 18))
testLabel.pack(side=TOP, anchor=NW, padx=(215, 0), pady=(25, 10))
breadLabel = tk.Label(orderFrame, text="", font=("Arial Bold", 14))
breadLabel.pack(side=TOP, anchor=NW, padx=(285, 0))
meatLabel = tk.Label(orderFrame, text="", font=("Arial Bold", 14))
meatLabel.pack(side=TOP, anchor=NW, padx=(285, 0))
drinkLabel = tk.Label(orderFrame, text="Drink: None Selected", font=("Arial Bold", 14))
drinkLabel.pack(side=TOP, anchor=NW, padx=(285, 0))
toppingsHeader = tk.Label(orderFrame, text="", font=("Arial Bold", 14))
toppingsHeader.pack(side=TOP, anchor=NW, padx=(285, 0))
toppingsLabel = tk.Label(orderFrame, text="", font=("Arial Bold", 14), fg="#8E3B8D")
toppingsLabel.pack(side=TOP, anchor=NW, padx=(285, 0))
purchaseBtn = tk.Button(orderFrame, text="Purchase", font=("Arial", 14), bg="#751E87", fg="white", width=10,
                        command=lambda: show_frame(purchaseCompleteFrame))
purchaseBtn.pack(pady=(20, 5), padx=(0, 75))
goBackBtn = tk.Button(orderFrame, text="Go Back", font=("Arial", 14), bg="#262626", fg="white", width=10,
                      command=lambda: show_frame(breadFrame))
goBackBtn.pack(padx=(0, 75))

# Purchase Complete items
purchaseCompleteLabel = tk.Label(purchaseCompleteFrame, text="Purchase Complete!", fg="#7E2EDB",
                                 font=("Arial Bold", 24))
purchaseCompleteLabel.place(relx=.5, rely=.35, anchor=CENTER)
countDownLabel = tk.Label(purchaseCompleteFrame, text="Window Closing In: ", fg="#222222", font=("Arial Bold", 18))
countDownLabel.place(relx=.5, rely=.45, anchor=CENTER)

# initially show_frame is called with breadFrame being passed through because it is the first page
show_frame(breadFrame)

# window.mainloop is called so that the program stays open
window.mainloop()
