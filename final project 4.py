import tkinter as tk

class TipCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Tip Calculator")

        # Create label and entry widgets for the bill amount
        self.bill_label = tk.Label(master, text="Bill Amount:")
        self.bill_label.pack()

        self.bill_entry = tk.Entry(master)
        self.bill_entry.pack()

        # Create label and radio button widgets for selecting the tip percentage
        self.tip_label = tk.Label(master, text="Select Tip Percentage:")
        self.tip_label.pack()

        self.tip_var = tk.StringVar(value="15")
        self.tip15_button = tk.Radiobutton(master, text="15%", variable=self.tip_var, value="15")
        self.tip15_button.pack()

        self.tip20_button = tk.Radiobutton(master, text="20%", variable=self.tip_var, value="20")
        self.tip20_button.pack()

        self.tip25_button = tk.Radiobutton(master, text="25%", variable=self.tip_var, value="25")
        self.tip25_button.pack()

        # Create button widgets for calculating the tip, viewing the total amount, and quitting the program
        self.calculate_button = tk.Button(master, text="Calculate Tip", command=self.calculate_tip)
        self.calculate_button.pack()

        self.total_button = tk.Button(master, text="Total Amount", command=self.show_total)
        self.total_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        # Create label widget for displaying the total amount including tip
        self.tip_label = tk.Label(master, text="Total Amount (including tip):")
        self.tip_label.pack()

        self.total_label = tk.Label(master, text="")
        self.total_label.pack()

    def calculate_tip(self):
        # Retrieve the bill amount and tip percentage selected by the user
        try:
            bill_amount = float(self.bill_entry.get())
            tip_percentage = float(self.tip_var.get()) / 100

            # Calculate the tip amount and total amount including tip
            tip_amount = bill_amount * tip_percentage
            total_amount = bill_amount + tip_amount

            # Display the total amount in the label widget
            self.total_label.configure(text="${:.2f}".format(total_amount))
        except ValueError:
            # Display an error message if the user enters invalid input
            self.total_label.configure(text="Invalid input!")

    def show_total(self):
        # Retrieve the bill amount and total amount including tip
        try:
            bill_amount = float(self.bill_entry.get())
            tip_percentage = float(self.tip_var.get()) / 100
            tip_amount = bill_amount * tip_percentage
            total_amount = bill_amount + tip_amount

            # Display the total amount in a message box
            tk.messagebox.showinfo("Total Amount", "The total amount (including tip) is ${:.2f}".format(total_amount))
        except ValueError:
            # Display an error message if the user enters invalid input
            self.total_label.configure(text="Invalid input!")

# Create the main GUI window and the TipCalculator instance
root = tk.Tk()
calculator = TipCalculator(root)

# Start the GUI event loop
root.mainloop()
