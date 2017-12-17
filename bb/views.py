from xml.etree.ElementTree import fromstring
from urllib.request import urlopen
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Message


def main(request):
    validate = 'https://passport.ustc.edu.cn/serviceValidate?service=http://hypercube.lug.ustc.edu.cn/&ticket=%s'
    if 'ticket' not in request.GET:
        return redirect('http://score.0x01.me/')
    with urlopen(validate % request.GET['ticket']) as req:
        data = fromstring(req.read())
    result = data.getchildren()[0]
    if result.tag != '{http://www.yale.edu/tp/cas}authenticationSuccess':
        return redirect('http://score.0x01.me/')
    name = result.getchildren()[0].text.upper()
    msg, created = Message.objects.get_or_create(user=name)
    return HttpResponse(msg.body)
