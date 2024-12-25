from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage,ttk,StringVar
import requests

def get_live_exchange_rates():
    # Define the API endpoint and access key
    url = "http://api.currencylayer.com/live"
    access_key = "f727f578fcd5ddfbed2e6f8b50f4cc4d"
    
    # Create the complete URL with access key
    full_url = f"{url}?access_key={access_key}"
    
    try:
        # Make a GET request to the API
        response = requests.get(full_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Convert response to JSON
            return data  # Return the data for further processing
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

data=get_live_exchange_rates()
key=data['quotes'].keys()
calc=data['quotes']
calc['']='none'

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("513x325")
        self.master.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=325,
            width=513,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.t=StringVar(value='None')
        self.b=[i[3:] for i in key]
        self.d=StringVar(value='')
        self.calculate=StringVar(value='')

        self.load_assets()
        self.create_widgets()

    def load_assets(self):
        """Load images and assets for the UI."""
        self.assets_path = Path(__file__).parent / Path(r"C:\Users\hp\Desktop\my projects\programm\build 2\build\assets\frame0")
        
        def relative_to_assets(path: str) -> Path:
            return self.assets_path / Path(path)

        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))

    def create_widgets(self):
        """Create all widgets for the application."""
        self.canvas.create_image(256.0, 162.0, image=self.image_1)
        
        # Labels
        self.canvas.create_text(17.0, 70.0, anchor="nw", text="Amount:", fill="#FFFFFF", font=("Jaro Regular", 15 * -1))
        self.canvas.create_text(17.0, 228.0, anchor="nw", text="Converted Amount:", fill="#FFFFFF", font=("Jaro Regular", 15 * -1))
        self.canvas.create_text(17.0, 281.0, anchor="nw", text="Exchange rate:", fill="#FFFFFF", font=("Jaro Regular", 15 * -1))
        
        # Entry for amount
        self.canvas.create_image(267.0, 83.5, image=self.entry_image_1)
        self.amount_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.amount_entry.place(x=174.5, y=72.0, width=185.0, height=25.0)

        # Entry for converted amount

        self.canvas.create_image(267.0, 233.5, image=self.entry_image_2)
        self.converted_entry = Entry(textvariable=self.calculate,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0,state='readonly')
        self.converted_entry.place(x=174.5, y=222.0, width=185.0, height=25.0)
        
        
       

        # Exchange rate placeholder
        self.create_fields()

        # From currency entry
        style = ttk.Style()
        style.configure("TCombobox", background="#FFFFFF", foreground="#000716")

        # From currency Combobox
        self.from_currency_entry = ttk.Combobox(
            master=self.master,
            values=["USD"],
            style="TCombobox",
            textvariable='USD',
            state='readonly'
        )
        self.from_currency_entry.place(x=76.0, y=121.0, width=153.0)

        # To currency Combobox
        self.to_currency_entry = ttk.Combobox(
            master=self.master,
            values = self.b,
            style="TCombobox",
            textvariable=self.d,
            state='readonly',
        )
        self.to_currency_entry.place(x=76.0, y=163.0, width=153.0)


        # Convert button
        self.convert_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.convert_currency,
            relief="flat"
        )
        self.convert_button.place(x=435.0, y=260.0, width=60.0, height=56.0)

        # Button hover effects
        self.convert_button.bind('<Enter>', lambda e: self.convert_button.config(image=self.button_image_hover_1))
        self.convert_button.bind('<Leave>', lambda e: self.convert_button.config(image=self.button_image_1))

    def create_fields(self):
        self.canvas.create_text(158.0, 281.0, anchor="nw", text=self.t.get(), fill="#FFFFFF", font=("Jaro Regular", 15 * -1))

        # From and To labels
        self.canvas.create_text(17.0, 121.0, anchor="nw", text="From:", fill="#000000", font=("Jaro Regular", 15 * -1))
        self.canvas.create_text(17.0, 163.0, anchor="nw", text="To:", fill="#000000", font=("Jaro Regular", 15 * -1))

    def convert_currency(self):
        self.t.set(f"1 USD= {calc['USD'+self.to_currency_entry.get()]} {self.to_currency_entry.get()}")
        self.d.set(self.to_currency_entry.get())
        self.calculate.set(float(self.amount_entry.get())*float(calc['USD'+self.to_currency_entry.get()]))
        print(self.calculate)
        self.canvas.delete("all")
        self.create_widgets()


        amount =(self.amount_entry.get())
        
        # Here you would implement the logic to get the exchange rate and perform conversion.
        
    def run(self):
        """Run the application."""
        self.master.resizable(False, False)
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverterApp(root)
    app.run()
