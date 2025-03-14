
### 📌 **Event Finder using Flask & Apify**  

This is a simple Flask web application that scrapes event data based on user-provided search criteria using the Apify API.  

---

## ✨ **Features**  
✅ Accepts user input (Keyword, City, State, Country).  
✅ Uses Apify to fetch event details.  
✅ Displays results in a styled HTML table.  
✅ Uses an HTML template and CSS for better UI.  

---

## 📦 **Prerequisites**  
Ensure you have the following installed:  
🔹 **Python 3.x**  
🔹 **Flask**  
🔹 **Pandas**  
🔹 **ApifyClient**  

---

## ⚡ **Installation**  

1. Install dependencies:  
   ```sh
   pip install flask pandas apify-client
   ```

---

## 📂 **Project Structure**  
```
event-finder/
│── templates/
│   ├── index.html  # 🎨 HTML form for user input
│── static/
│   ├── styles.css  # 🎨 Styling for the page
│── app.py          # 🚀 Main Flask application
│── README.md       # 📖 Project documentation
│── requirements.txt  # 📌 Dependencies
```

---

## 🚀 **Running the Application**  

1. Start the Flask app:  
   ```sh
   python app.py
   ```

2. Open your browser and go to:  
   ```
   http://127.0.0.1:5000
   ```

---

## 🎨 **HTML & CSS**  

📜 **`templates/index.html`**  
- This file contains a simple form where users enter:  
  ✅ **Event Keyword**  
  🔹 **City, State, and Country**  
  - The submitted data is processed by Flask to fetch event details.

🎨 **`static/styles.css`**  
- Defines basic **styling** for the HTML page and the results table.

---

## 🔥 **Notes**  
⚠️ **Ensure your Apify actor ID is correct.**  
⚠️ **Keep your API token secure** – Avoid hardcoding it in your code.  

---
