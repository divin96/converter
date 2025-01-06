# Currency Converter Application

## Overview

This Currency Converter Application allows users to convert amounts between different currencies using live exchange rates fetched from the CurrencyLayer API. The application features a graphical user interface (GUI) built with Tkinter and displays information on an OLED screen.

## Features

- Fetch live exchange rates from the CurrencyLayer API.
- Convert amounts between different currencies.
- Display the converted amount and exchange rate in a user-friendly interface.
- Responsive design with hover effects on buttons.

## Requirements

Before running the application, make sure you have the following libraries installed:

- `requests`: For making HTTP requests to fetch exchange rates.
- `Pillow`: For image processing (used with the OLED display).
- `Adafruit-SSD1306`: For controlling the SSD1306 OLED display.
- `gpiozero`: For controlling the buzzer (if applicable).
- `google-auth` and `google-auth-oauthlib`: For Google OAuth authentication (if using Google services).

### Installation

You can install the required packages using pip. Create a `requirements.txt` file with the following content:

```plaintext
requests
Pillow
Adafruit-SSD1306
gpiozero
google-auth
google-auth-oauthlib
```

Then, run:

```bash
pip install -r requirements.txt
```

## Setup

1. **API Key**: Obtain an access key from [CurrencyLayer](https://currencylayer.com/) by signing up for a free account. Replace the placeholder in the code with your actual access key.

2. **Run the Application**: You can run the application by executing the script in your Python environment.

## Code Explanation

Here’s a breakdown of the code:

### Imports

```python
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, StringVar
import requests
```
- **pathlib**: Used for handling file paths.
- **tkinter**: Used to create GUI components.
- **requests**: Used to make HTTP requests to fetch exchange rates.

### Function to Get Live Exchange Rates

```python
def get_live_exchange_rates():
    url = "http://api.currencylayer.com/live"
    access_key = "YOUR_ACCESS_KEY"  # Replace with your actual access key
    
    full_url = f"{url}?access_key={access_key}"
    
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
```
- This function constructs a URL to fetch live exchange rates from the CurrencyLayer API using an access key.
- It makes a GET request and checks if it was successful (HTTP status code 200).
- If successful, it returns the JSON data; otherwise, it prints an error message.

### Main Class for Currency Converter App

```python
class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("513x325")
        self.master.configure(bg="#FFFFFF")
```
- The `CurrencyConverterApp` class initializes the main application window and its properties.

#### Load Assets

```python
def load_assets(self):
    """Load images and assets for the UI."""
    self.assets_path = Path(__file__).parent / Path("path_to_assets")  # Update with your assets path
    
    def relative_to_assets(path: str) -> Path:
        return self.assets_path / Path(path)

    self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    # Load other images similarly...
```
- This method loads images used in the GUI from a specified assets directory.

#### Create Widgets

```python
def create_widgets(self):
    """Create all widgets for the application."""
    self.canvas.create_image(256.0, 162.0, image=self.image_1)
    
    # Labels and Entry fields are created here...
```
- This method creates all GUI elements such as labels, entry fields, and buttons.

#### Convert Currency Functionality

```python
def convert_currency(self):
    self.t.set(f"1 USD= {calc['USD'+self.to_currency_entry.get()]} {self.to_currency_entry.get()}")
    self.d.set(self.to_currency_entry.get())
    self.calculate.set(float(self.amount_entry.get()) * float(calc['USD'+self.to_currency_entry.get()]))
```
- This method handles currency conversion logic when the user clicks the convert button.

### Running the Application

```python
if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverterApp(root)
    app.run()
```
- This block initializes and runs the application.

## Usage

1. Open the application.
2. Enter an amount in USD.
3. Select a currency to convert to from the dropdown menu.
4. Click on the convert button to see results displayed on the screen.

## License

This project is licensed under 8 RONINS.
