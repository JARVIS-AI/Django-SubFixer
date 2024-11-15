function updateFileName() {
            const fileInput = document.getElementById('subtitle_file');
            const fileName = fileInput.files.length > 0 ? fileInput.files[0].name : '';
            document.getElementById('file-name').textContent = fileName;
            document.getElementById('error-message').classList.add('hidden');
        }
