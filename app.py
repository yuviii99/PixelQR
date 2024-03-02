from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')


@app.route('/')
def index():
    return render_template("user.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/images', methods=['GET', 'POST'])
def images():
    user_uuid = request.form['unique_id']
    event_name = user_uuid.split("-")[0]
    upload_folder = os.path.join("uploads", event_name)
    if os.path.exists(upload_folder):
        user_folder = os.path.join(upload_folder, user_uuid)
        files = os.listdir(user_folder)
        print(type(files[0]))
        files_url = [os.path.join(user_folder, file.replace("%", " ")) for file in files]
        return render_template("images.html", files=files_url, event_name=event_name.replace("_", " "))
    else:
        return "No images have been uploaded yet, check again later!"


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        event_name = request.form['event_name'].replace(" ", "_")
        unique_id = request.form['unique_id']
        event_folder = os.path.join('uploads', event_name)
        os.makedirs(f'{event_folder}/{unique_id}')
        files = request.files.getlist("file")
        for file in files:
            file.save(f'uploads/{event_name}/{unique_id}/{file.filename}')

    return render_template("admin.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
