import tkinter
from tkinter import *
from PIL import Image, ImageTk

def main():

    verbing = input("Enter a verb that ends in ing: ")
    number = input("Enter a number: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a another noun: ")
    adjective = input("Enter an adjective: ")
    kid_name = input("Enter name: ")
    # age = input("Enter an age: ")

    color = input("pink (1) or yellow (2)")

    pinkButterflyPath = "dw-butterfly.png"

    yellowButterflyPath = "dw-butterfly-yellow.png"

    butterflyPath = yellowButterflyPath if color == '2' else pinkButterflyPath


    # # text = f"Roses are {color} \n {plural_noun} are blue \n I love {celebrity}"
    # story = f"Computers are amazing pieces of technology that are really great at {verbing}.\n\n You would be surprised by the amount of computers you see a day! \n\n " \
    #         f"In an average day, you see {number} computers. \n\n Computers can be as big as a {noun1} or as small as a {noun2}.\n\n  Did you know that {adjective} calculators " \
    #         f"are computers too?\n\n  Technology can do so much! \n\n I wonder what technology will do when {kid_name} is {age}!!"


            # text = f"Roses are {color} \n {plural_noun} are blue \n I love {celebrity}"
    story = f"Computers are amazing pieces of technology that are really great at {verbing}. " \
            f"\n\n Computers can be as big as a {noun1} or as small as a {noun2}.\n\n  Did you know that {adjective} calculators " \
            f"are computers too?\n\n  Technology can do so much! \n\n I wonder what technology will do when {kid_name} is {number}!!"

    root = Tk()

    butterfly = Image.open(butterflyPath)

    test = ImageTk.PhotoImage(butterfly)

    butterflyLabel = tkinter.Label(image=test)
    butterflyLabel.image = test
    # butterflyLabel.place(x=0, y=0)

    butterflyLabel.pack(side=tkinter.BOTTOM)

    label = tkinter.Label(
                        None,
                        text=story,
                        font=('Times', '28'),
                        fg='blue'
                     )
    label.pack()
    label.mainloop()

if __name__ == "__main__":
    main()


