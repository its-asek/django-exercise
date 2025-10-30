from django.core.validators import FileExtensionValidator
from django.forms import Form, FileField


class TextUploadForm(Form):
    text_file = FileField(
        validators=[FileExtensionValidator(allowed_extensions=["txt"])],
        help_text="Upload a .txt file",
    )
