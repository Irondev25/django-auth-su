import logging

from django import forms

from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model

from .utils import ActivationMailFormMixin


logger = logging.getLogger(__name__)


class UserCreationForm(ActivationMailFormMixin, BaseUserCreationForm):
    mail_validation_error = ('User created. Could not send activation '
                             'email. Please try again later. (Sorry!)')

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    def save(self, **kwargs):
        user = super().save(commit=False)
        if not user.pk:
            user.is_active = False
            send_mail = True
        else:
            send_mail = False
        user.save()
        self.save_m2m()
        #after saving user in database we send conformation link
        if send_mail:
            self.send_mail(user=user, **kwargs)
        return user


class ResendActivationEmailForm(ActivationMailFormMixin, forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    mail_validation_error = (
        'Could not re-send activation email. '
        'Please try again later. (Sorry!)'
    )

    def save(self, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(
                email=self.cleaned_data['email']
            )
        except:
            logging = logger.warning(
                'Resend Activation: No user with '
                'email: {}.'.format(
                    self.cleaned_data['email']
                )
            )
            return None
        self.send_mail(user=user, **kwargs)
        return user
