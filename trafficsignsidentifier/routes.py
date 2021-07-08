from trafficsignsidentifier import app
from PIL import Image, UnidentifiedImageError
from tensorflow.keras.models import load_model
from skimage import transform, io
import numpy as np
import base64
import io as ios
from flask import render_template, request, redirect, url_for, flash
from trafficsignsidentifier.forms import UploadPhotoForm

model = load_model('./model/output/trafficsignnet.model')
labelNames = open("./model/signnames.csv").read().strip().split("\n")[1:]
labelNames = [l.split(",")[1] for l in labelNames]


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
        file = request.files['file']
        img = Image.open(file)
        data = ios.BytesIO()
        formats = 'PNG' or 'JPEG'
        img.save(data, formats)
        encoded_img_data = base64.b64encode(data.getvalue())

        imgOriginal = io.imread(file, plugin='matplotlib')
        imgOriginal = transform.resize(imgOriginal, (32, 32))
        imgOriginal = imgOriginal.astype("float32") / 255.0
        imgOriginal = np.expand_dims(imgOriginal, axis=0)
        pred = model.predict(imgOriginal)
        j = pred.argmax(axis=1)[0]
        sign = labelNames[j]

        return render_template('results.html', img_data=encoded_img_data.decode('utf-8'),
                               context={"predictedSign": sign})
    except UnidentifiedImageError:
        flash('Wrong File Format! Please use .jpg or .png file.')
        return redirect(url_for('main_page', error=error))
