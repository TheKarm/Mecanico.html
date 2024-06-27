from django.forms import ModelForm
from .models import *
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MecanicoForm(ModelForm):
    captcha = CaptchaField()
    #captcha = ReCaptchaField()

    class Meta:
        model = Mecanico
        fields = '__all__'

class TipoMecanicoForm(ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = TipoMecanico
        fields = '__all__'

class GeneroForm(ModelForm):

    class Meta:
        model = Genero
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    #captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        