from django.shortcuts import render
from margemfrontal.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


def index(request):
    sub = forms.Contact()
    if request.method == 'POST':
        
        sub = forms.Contact(request.POST)
        subject = 'Nova mensagem enviada através do website '
        message = 'Nova mensagem recebida:' + '\n'\
            'Nome: ' + sub.Name + '\n'\
            'E-mail: ' + sub.Email + '\n'\
            'Pais: ' + sub.Country + '\n'\
            'Assunto: ' + sub.Subject + '\n' \
            'Mensagem:' + sub.Message + '\n'

        recepient = "margemfrontalwebsite@gmail.com"
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'index.html', {'form' : sub, 'alert': 'success','alertmsg' : 'Pedido enviado com sucesso!'})

    return render(request, 'index.html', {'form' : sub})

def oportunidades(request):
    sub = forms.Oportunities()
    if request.method == 'POST':
        
        sub = forms.Oportunities(request.POST)
        subject = 'Nova candidatura enviada através do website '
        message = 'Nova candidatura recebida:' + '\n'\
            'Nome: ' + sub.Name + '\n'\
            'E-mail: ' + sub.Email + '\n'\
            'Distrito onde vive: ' + sub.DistrictHome + '\n'\
            'Distrito onde pretende colaborar: ' + sub.DistrictWork + '\n'\
            'Preferência: ' + sub.Preference + '\n'\
            'Serviços onde pretende colaborar: ' + sub.Service + '\n'\
            'Mensagem:' + sub.Message + '\n'
        recepient = "margemfrontalwebsite@gmail.com"
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'oportunidades.html', {'form' : sub,'alert': 'success','alertmsg' : 'Pedido enviado com sucesso!'})

    return render(request, 'oportunidades.html',{'form' : sub})