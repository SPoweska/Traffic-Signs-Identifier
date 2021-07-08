from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from wtforms import SubmitField

images = ['JPEG', 'PNG']


class UploadPhotoForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('✓')
