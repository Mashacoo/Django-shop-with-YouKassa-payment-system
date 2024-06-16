from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.shortcuts import render
from profile_app.models import Profile
from profile_app.forms import UserProfileChangeForm


class ProfileChangeView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileChangeForm
    template_name = 'profile_app/change_profile.html'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile_app:profile', pk=kwargs['pk'])
        return render(
            request,
            template_name=self.template_name,
            context={
                'message': 'Профиль не был обновлен',
                'profile': instance,
                'form': self.form_class
            }
        )
