Txt Merger is a web application that lets you easily merge .txt files by prefix. Just drag & drop your files into the app, and it will automatically group, merge, and package them into a downloadable .zip.

Made with ❤️ by William's Great Strategy → william-strategy.com

✨ Features

📂 Drag & Drop Upload – Simply drop your .txt files into the app.

🔎 Smart Prefix Detection – Groups files by prefix (before the _ in filenames).

📝 Automatic Merging – Each group is merged into prefix_result.txt.

📦 One-Click Download – All merged files are zipped into a single archive.

🎨 Clean UI – Styled with custom CSS & interactive JavaScript.

🛠️ Tech Stack

Flask (Python) – Backend framework

HTML, CSS, JavaScript – Frontend interface

Werkzeug – Secure file handling

Zipfile & Shutil – For packaging results

🚀 How to Run Locally

Clone the repository:

git clone https://github.com/the-great-king/txt-merger.git
cd txt-merger


(Optional but recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install flask


Start the Flask app:

python app.py


Open the URL shown in your terminal (something like http://127.0.0.1:5000).

📁 Project Structure
txt-merger/
│── app.py              # Flask backend
│── templates/          # HTML templates
│── static/             # CSS & JS (style.css, script.js)
│── uploads/            # Temporary uploaded files
│── results/            # Zipped merged outputs
│── README.md

🔮 Future Ideas

File type support beyond .txt (e.g., .csv, .log)

Option to choose custom output filenames

Cloud storage integration (Google Drive, Dropbox)

📜 License

Released under the MIT License.