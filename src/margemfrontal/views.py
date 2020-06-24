from django.shortcuts import render
from margemfrontal.settings import EMAIL_HOST_USER, RECIPIENT_EMAIL
from .forms import ContactForm, OportunitiesForm
from django.core.mail import send_mail
import logging

def index(request):
        return render(request, 'index.html')

def food(request):
        return render(request, 'food.html')

def security(request):
        return render(request, 'security.html')

def construction(request):
        return render(request, 'construction.html')

def houses(request):
        return render(request, 'houses.html')

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("Name")
            email = form.cleaned_data.get("Email")
            country = form.cleaned_data.get("Country")
            matter = form.cleaned_data.get("Subject")
            message = form.cleaned_data.get("Message")

            subject = 'Nova mensagem enviada através do website '
            message = 'Nova mensagem recebida:' + '\n'\
                'Nome: ' + name + '\n'\
                'E-mail: ' + email + '\n'\
                'Pais: ' + country + '\n'\
                'Assunto: ' + matter + '\n' \
                'Mensagem:' + message + '\n'

            send_mail(subject, 
                message, EMAIL_HOST_USER, [RECIPIENT_EMAIL], fail_silently = False)
            return render(request, 'contact.html', {'form' : form, 'alert': 'success','alertmsg' : 'Pedido enviado com sucesso!'})
        else:
            return render(request, 'contact.html', {'form' : form,'alert': 'fail','alertmsg' : 'Formulário inválido! Verifique os dados do formulário!'})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form' : form})

def oportunidades(request):

    if request.method == 'POST':
        form = OportunitiesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("Name")
            email = form.cleaned_data.get("Email")
            districtHome = form.cleaned_data.get("DistrictHome")
            districtWork = form.cleaned_data.get("DistrictWork")
            preference = form.cleaned_data.get("Preference")
            service = form.cleaned_data.get("Service")
            message = form.cleaned_data.get("Message")

            subject = 'Nova candidatura enviada através do website '
            message = 'Nova candidatura recebida:' + '\n'\
                'Nome: ' + name+ '\n'\
                'E-mail: ' + email + '\n'\
                'Distrito onde vive: ' + districtHome + '\n'\
                'Distrito onde pretende colaborar: ' + districtWork + '\n'\
                'Preferência: ' + preference + '\n'\
                'Serviços onde pretende colaborar: ' + service + '\n'\
                'Mensagem:' + message + '\n'
            send_mail(subject, 
                message, EMAIL_HOST_USER, [RECIPIENT_EMAIL], fail_silently = False)
            return render(request, 'oportunidades.html', {'form' : form,'alert': 'success','alertmsg' : 'Pedido enviado com sucesso!'})
        else:
            return render(request, 'oportunidades.html', {'form' : form,'alert': 'fail','alertmsg' : 'Formulário inválido! Verifique os dados do formulário!'})
    else:
        form = OportunitiesForm()
        return render(request, 'oportunidades.html',{'form' : form})