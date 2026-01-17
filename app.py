from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from agent import query
import os
load_dotenv()
app = FastAPI()
API_MAGIC_TOKEN = os.environ.get('API_MAGIC_TOKEN')
class FormData(BaseModel):
    message: str
    token: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Query Form</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 450px;
            }
            h1 {
                color: #333;
                margin-bottom: 30px;
                font-size: 28px;
                text-align: center;
            }
            .form-group {
                margin-bottom: 24px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                color: #555;
                font-weight: 500;
                font-size: 14px;
            }
            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 12px 16px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                font-size: 15px;
                transition: border-color 0.3s;
            }
            input[type="text"]:focus,
            input[type="password"]:focus {
                outline: none;
                border-color: #667eea;
            }
            button {
                width: 100%;
                padding: 14px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
            }
            button:active {
                transform: translateY(0);
            }
            .response {
                margin-top: 24px;
                padding: 16px;
                background: #f8f9fa;
                border-radius: 8px;
                border-left: 4px solid #667eea;
                display: none;
            }
            .response.show {
                display: block;
            }
            .response h3 {
                color: #333;
                margin-bottom: 8px;
                font-size: 16px;
            }
            .response p {
                color: #666;
                font-size: 14px;
                line-height: 1.6;
            }
            .spinner {
                display: none;
                width: 20px;
                height: 20px;
                border: 3px solid rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                border-top-color: white;
                animation: spin 1s ease-in-out infinite;
                margin-left: 10px;
                vertical-align: middle;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            button.loading .spinner {
                display: inline-block;
            }
            button:disabled {
                opacity: 0.7;
                cursor: not-allowed;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Write your query</h1>
            <form id="messageForm">
                <div class="form-group">
                    <label for="message">Query</label>
                    <input type="text" id="message" name="message" placeholder="eg. Create a topic with name Uber" required>
                </div>
                <div class="form-group">
                    <label for="token">Magic Token</label>
                    <input type="password" id="token" name="token" placeholder="Enter your magic token" required>
                </div>
                <button type="submit" id="submitBtn">
                    <span>Submit</span>
                    <span class="spinner"></span>
                </button>
            </form>
            <div class="response" id="response">
                <h3>Response</h3>
                <p id="responseText"></p>
            </div>
        </div>

        <script>
            document.getElementById('messageForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                
                const submitBtn = document.getElementById('submitBtn');
                const formData = new FormData();
                formData.append('message', document.getElementById('message').value);
                formData.append('token', document.getElementById('token').value);
                
                // Show loader and disable button
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                try {
                    const response = await fetch('/submit', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    const responseDiv = document.getElementById('response');
                    const responseText = document.getElementById('responseText');
                    
                    responseText.textContent = JSON.stringify(data, null, 2);
                    responseDiv.classList.add('show');
                } catch (error) {
                    alert('Error submitting form: ' + error.message);
                } finally {
                    // Hide loader and enable button
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/submit")
async def submit_form(message: str = Form(...), token: str = Form(...)):
    if token != API_MAGIC_TOKEN:
        return {
            "success": False,
            "error": "Invalid token"
        }

    result =  await query(message)
    print("result", result)
    return {
        "success": True,
        "result": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
