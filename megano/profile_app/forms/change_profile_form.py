from django import forms
from profile_app.models import Profile


class UserProfileChangeForm(forms.ModelForm):

    username = forms.CharField(max_length=20, label='ФИО', required=False)
    phone = forms.CharField(
        required=False,
        max_length=18,
        label='Телефон',
        widget=forms.NumberInput(
            attrs={
                'type': 'tel',
                'class': 'data-tel-input',
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['avatar']
        labels = {
            'username': 'Имя пользователя',
            # 'phone': 'Телефон',
        }
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'Profile-file form-input', 'required': False}),
            # 'phone': forms.NumberInput(attrs={'type': 'tel', 'class': 'data-tel-input'}),
        }

    def separate_phone(self, phone: str) -> str:
        """
        Функция для выдачи номера телефона без +, 7, 8, (, ), то есть в формате 10 цифр
        """
        result = ''.join([i for i in tuple(phone) if i.isdigit()])
        return result[1:]

    def save(self, commit=True):
        profile = super().save(commit=False)
        username = self.cleaned_data.get('username')
        if username:
            profile.user.username = username
            profile.user.save()
        profile.avatar = self.cleaned_data.get('avatar')
        profile.phone = self.separate_phone(self.cleaned_data.get('phone'))
        if commit:
            profile.save()
        return profile
