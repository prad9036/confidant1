from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class DiaryCreateForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()], render_kw={"placeholder": "Title", "autofocus": True}
    )
    content = CKEditorField(
        "Content", validators=[DataRequired()]
    )
    diary_date = StringField(
        "Date", validators=[DataRequired()], render_kw={"readonly": True}
    )

    submit = SubmitField("Submit")
