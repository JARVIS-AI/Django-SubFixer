function validateAndSubmit() {
            const fileInput = document.getElementById('subtitle_file');
            const errorMessage = document.getElementById('error-message');

            if (fileInput.files.length === 0) {
                errorMessage.classList.remove('hidden');
            } else {
				
            	fetch('/addcount/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Process the response data
                    document.getElementById('counter').innerText = data["counter"];
                })
                .catch(error => {
                    // Handle any errors
                    document.getElementById('result').innerHTML = 'Error: ' + error.message;
                });
				
                errorMessage.classList.add('hidden');
                document.getElementById('subtitleForm').submit();	
            }
        }