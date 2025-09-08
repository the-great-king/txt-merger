import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from collections import defaultdict
import zipfile
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
MERGED_FOLDER = "merged"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MERGED_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merge", methods=["POST"])
def merge_files():
    files = request.files.getlist("files[]")
    if not files:
        return "No files uploaded"

    # Clean old files
    shutil.rmtree(UPLOAD_FOLDER)
    shutil.rmtree(MERGED_FOLDER)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(MERGED_FOLDER, exist_ok=True)

    # Save uploaded files
    for f in files:
        # Folder name inazingua
        filename = os.path.basename(f.filename)
        filename = secure_filename(filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))

    # Stay focus for the name
    groups = defaultdict(list)
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(".txt"):
            prefix = filename.split("_")[0]   # Jina ndo issue
            groups[prefix].append(os.path.join(UPLOAD_FOLDER, filename))

    merged_files = []
    for prefix, file_list in groups.items():
        result_path = os.path.join(MERGED_FOLDER, f"{prefix}_result.txt")
        with open(result_path, "w", encoding="utf-8") as outfile:
            for file_path in sorted(file_list):
                with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
        merged_files.append(result_path)
        print(f'{prefix}_result.txt is Merged well, No error at all')

    # Can't just Save by Folder. i have to implement .ZIP hapa ndo kuna error 'i have to resolve this'
    zip_path = "merged_results.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for f in merged_files:
            zipf.write(f, os.path.basename(f))

    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
