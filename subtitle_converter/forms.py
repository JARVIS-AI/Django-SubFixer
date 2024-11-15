from django import forms

class SubtitleUploadForm(forms.Form):
    subtitle_file = forms.FileField(label="زیر نویس فارسی یا عربی خود را انتخاب کنید")
