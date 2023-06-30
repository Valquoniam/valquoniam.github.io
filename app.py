from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    target_image = request.files['targetImage']
    target_image.save('target_image.jpeg')

    command = ['python', 'projector.py', '--outdir=out', '--target=target_image.jpeg', '--network=training-runs/snapshots/network-snapshot-005400.pkl']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        return output
    else:
        return error

if __name__ == '__main__':
    app.run()
