from django import forms

class DictForm(forms.Form):
    text = forms.CharField(
        label='Enter Text',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        max_length=700  
    )
    language = forms.ChoiceField(choices=[
        ('en', 'English'),
        ('zh', 'Chinese'),
        ('es', 'Spanish'),
        ('hi', 'Hindi'),
        ('ar', 'Arabic'),
        ('pt', 'Portuguese'),
        ('de', 'German'),
        ('fr', 'French'),
        ('ja', 'Japanese'),
        ('pl', 'Polish'),
    ])