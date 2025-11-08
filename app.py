from flask import Flask
import subprocess

# Name the app
app = Flask(__name__)

@app.route('/')
def run_tests():
    """
    Runs the main.py script using subprocess and returns its output.
    """
    try:
        # Execute the main.py script
        # The 'text=True' argument captures output as a string.
        result = subprocess.run(
            ['python', 'main.py'],
            capture_output=True,
            text=True,
            timeout=30  # 30-second timeout
        )
        
        # Get the standard output and error
        output = result.stdout
        errors = result.stderr
        
        # Format the output for an HTML page
        # Replace newlines with <br> tags for browser display
        html_output = output.replace('\n', '<br>')
        html_errors = errors.replace('\n', '<br>')
        
        # Return the output
        return f"<h1>freeCodeCamp Test Output</h1><pre>{html_output}</pre><h2>Errors (if any):</h2><pre>{html_errors}</pre>"

    except Exception as e:
        return f"An error occurred while running the script: {str(e)}"

if __name__ == '__main__':
    # '0.0.0.0' makes it accessible on the network
    app.run(host='0.0.0.0', port=8080)
