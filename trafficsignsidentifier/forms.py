from wtforms import Form, FileField, SubmitField


class UploadPhotoForm(Form):
    file = FileField('File')
    submit = SubmitField('Submit')