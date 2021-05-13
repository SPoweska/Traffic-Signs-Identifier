from trafficsignsidentifier import app
from PIL import Image, UnidentifiedImageError
import base64
import io
from flask import render_template, request, redirect, url_for, flash
from trafficsignsidentifier.forms import UploadPhotoForm


@app.route('/')
def main_page():
    form = UploadPhotoForm()
    return render_template('main.html', form=form)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    error = None
    try:
        im = Image.open(request.files['file'])
        im.thumbnail((400, 400))
        data = io.BytesIO()
        formats = 'PNG' or 'JPEG'
        im.save(data, formats)
        encoded_img_data = base64.b64encode(data.getvalue())
        return render_template('results.html', img_data=encoded_img_data.decode('utf-8'))
    except UnidentifiedImageError:
        flash('Wrong File Format!')
        return redirect(url_for('main_page', error=error))





