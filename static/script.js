const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileInfo = document.getElementById('file-info');
const form = document.getElementById('upload-form');
const resultDiv = document.getElementById('result');

dropZone.addEventListener('click', () => fileInput.click());

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');

    const files = [];
    for (let file of e.dataTransfer.files) {
        if (file.name.endsWith(".txt")) files.push(file);
    }

    const dataTransfer = new DataTransfer();
    for (let file of files) {
        dataTransfer.items.add(file);
    }
    fileInput.files = dataTransfer.files;

    if (files.length > 0) {
        dropZone.classList.add('hidden');
        fileInfo.classList.remove('hidden');
        fileInfo.textContent = `✅ Folder loaded with ${files.length} TXT files`;
    }
});

fileInput.addEventListener('change', () => {
    const files = fileInput.files;
    if (files.length > 0) {
        dropZone.classList.add('hidden');
        fileInfo.classList.remove('hidden');
        fileInfo.textContent = `✅ Folder loaded with ${files.length} TXT files`;
    }
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const files = fileInput.files;
    if (!files.length) {
        alert("Please select a folder with TXT files!");
        return;
    }

    const formData = new FormData();
    for (let file of files) {
        formData.append('files[]', file);
    }

    resultDiv.innerHTML = "Merging...";
    const response = await fetch('/merge', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = "merged_results.zip";
        a.textContent = "Download Merged Files";
        resultDiv.innerHTML = "";
        resultDiv.appendChild(a);
    } else {
        resultDiv.textContent = "Error merging files.";
    }
});
