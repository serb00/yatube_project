# from django.shortcuts import render
# import CreateView to inherit from it
from django.shortcuts import redirect, render
from django.views.generic import CreateView
# reverse_lazy allow to get URL by "name" parameter
from django.urls import reverse_lazy
# import form class to use it in view class
from .forms import ContactForm, CreationForm


# Create your views here.


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")  # where login is a parameter in path()
    template_name = "signup.html"


def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['body']

            form.save()
            return redirect('/thank-you/')
        return render(request, 'contact.html', {'form': form})

    form = ContactForm()

    return render(request, 'users/contact.htms', {"form": form})
