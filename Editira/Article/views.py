from django.shortcuts import render
from django.http import HttpResponse
import translate as tran
from translate import translate
# Create your views here.


def home(request):
    return render(request, 'index.html' )


def Translator(request):
    to_lang = 'en'
    from_lang = 'fr'
    to_translate = 'to translate'
    if request.method=='POST':
        if request.POST.get('to_translate') == None:
            to_translate = 'to translate'
        else:
            to_translate= request.POST['to_translate']
            from_lang = request.POST['LangFrom']
            print(from_lang)
            to_lang = request.POST['LangTo']
            print(to_lang)
    translator = tran.Translator(to_lang=to_lang,from_lang=from_lang)
    translation = translator.translate(to_translate)
    context={
        'to_translate': to_translate,
        'translation' : translation
    }
    #return HttpResponse(context)
    return render(request,'Article/translator.html',context)
