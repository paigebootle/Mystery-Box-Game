from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                          "(between $5 and $50) in the box "
                                          "below. Then choose the stakes. "
                                          "The higher the stakes, the more "
                                          "you can win!", wrap=275, justify=LEFT,
                                          padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # entry box (row 2)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 19 bold")
        self.start_amount_entry.grid(row=2)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # button font
        button_font = "Arial 12 bold"

        # orange low stakes button
        self.lowstakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # yellow medium stakes button
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                           command=lambda: self.to_game(2),
                                           font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, padx=5, pady=10)

        # green high stakes button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                         command=lambda: self.to_game(3),
                                         font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, pady=10)

        # help button
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=4, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

    #     partner.low_stakes_button.config(state=DISABLED)
    #
    #     # initialise variables
    #     self.balance = IntVar()
    #
    #     # set starting balance to amount set by user at start of game
    #     self.balance.set(starting_balance)
    #
    #     # GUI setup
    #     self.game_box = Toplevel()
    #     self.game_frame = Frame(self.game_box)
    #     self.game_frame.grid()
    #
    #     # heading row
    #     self.heading_label = Label(self.game_frame, text="Heading",
    #                                font="Arial 24 bold", padx=10, pady=10)
    #     self.heading_label.grid(row=0)
    #
    #     # balance label
    #     self.balance_frame = Frame(self.game_frame)
    #     self.balance_frame.grid(row=1)
    #
    #     self.balance_label = Label(self.game_frame, text="Balance...")
    #     self.balance_label.grid(row=2)
    #
    #     self.play_button = Button(self.game_frame, text="Gain",
    #                               padx=10, pady=10, command=self.reveal_boxes)
    #     self.play_button.grid(row=3)
    #
    # def reveal_boxes(self):
    #     # retrieve the balance from the initial function
    #     current_balance = self.balance.get()
    #
    #     # adjust the balance (subtract game cost and add pay out)
    #     # for testing, just add 2
    #     current_balance += 2
    #
    #     # set balance to adjusted balance
    #     self.balance.set(current_balance)
    #
    #     # edit label so user can see their balance
    #     self.balance_label.configure(text="Balance: {}".format(current_balance))

# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start()
    root.mainloop()
