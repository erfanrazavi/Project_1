from django.forms import ModelForm
from captcha.fields import CaptchaField
from index.models import Contact , NewsLetter

class ContactForm(ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Contact
        fields = "__all__"
class NewsLetterForm(ModelForm):
    
    
    class Meta:
        model = NewsLetter
        fields = "__all__"
    