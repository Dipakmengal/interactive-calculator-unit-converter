# 🧮 Interactive Calculator & Unit Converter

A beginner-friendly Python project developed as part of my
internship learning tasks. It combines a command-line calculator
with a browser-based interactive application.

## 🌐 Live Demo

**Try the application:** [Open Live Demo](https://interactive-calculator-unit-converter-jbedqywzkgkmsssxdp9ker.streamlit.app/)

> Replace the placeholder above with your deployed Streamlit URL.

## 📌 Features

- Basic arithmetic: addition, subtraction, multiplication and division
- Unit conversion: kilometers to miles and miles to kilometers
- Temperature conversion: Celsius to Fahrenheit and vice versa
- Currency conversion: USD to INR, INR to USD and EUR to INR
- Input validation using while loops and try/except
- Division-by-zero protection
- Command-line and browser-based interfaces

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Git and GitHub

## 📁 Project Structure

```text
interactive-calculator-unit-converter/
├── calculator_converter.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## 🚀 Run the Command-Line Version

1. Install Python 3.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/interactive-calculator-unit-converter.git
   ```

3. Enter the project folder:

   ```bash
   cd interactive-calculator-unit-converter
   ```

4. Run the CLI application:

   ```bash
   python calculator_converter.py
   ```

   On some systems, use `python3` instead of `python`.

## 💻 Run the Web Application Locally

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser. If it does not, use the
local URL printed in your terminal, usually
http://localhost:8501.

## 💱 Currency Rate Notice

Currency rates in this beginner project are illustrative examples,
not live financial data. Update the rates or connect a reliable
exchange-rate API before using them for real transactions.

## 📚 Concepts Practiced

- Variables and data types
- Functions
- Conditional statements
- While loops
- User input and output
- Exception handling
- Dictionaries
- Basic arithmetic and unit conversion

## 🎯 Project Objective

To practice fundamental Python programming concepts by building
a useful calculator and unit converter with a command-line
interface and an interactive web interface.

## 👤 Author

Dipak Mengal

- GitHub: https://github.com/Dipakmengal

## 📄 License

This project is licensed under the MIT License.
See the `LICENSE` file for details.