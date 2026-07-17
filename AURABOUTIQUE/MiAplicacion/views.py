from django.shortcuts import render,HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("""
                            <h1> HOLA MUNDO </h1>
                        """)

def pagina(request):
    return HttpResponse("""
                            <h1> SITIO WEB AURA BOUTIQUE </h1>
                            <H3> VISTETE DIFERENTE, SIENTETE UNICA</h3>
                        """)
