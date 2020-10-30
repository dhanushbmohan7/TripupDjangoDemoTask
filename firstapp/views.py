from django.shortcuts import render,redirect
#from translate import Translator
from  googletrans import Translator
from .models import results,languages
# Create your views here.
lang=languages.objects.all()
print('languages',lang)
def home(request):
    items=results.objects.all()

    return render(request,'home.html',{'items':items})

def search(request):

    if request.method =='GET':
        
        search_element=request.GET.get('element')
        s=search_element.split(" ")
       
        final_result=results.objects.filter(title=search_element)
        if final_result:
            res=results.objects.get(title=search_element)
            print(res.answer)
            request.session['answer']=res.answer
            return render(request,'resultpage.html',{'res':res.answer,'lang':lang})

        else:
            print('not found')    
            return render(request,'notfound.html')

          
    return render(request,'resultpage.html')    



def language(request,language_key):
    try:
        ans=request.session['answer']
        print(language_key)
        translator=Translator()
        translation=translator.translate(text=ans,src='en',dest=language_key)
        print(translation)
        current_language=languages.objects.get(key=language_key)
        print(current_language.language)
    except Exception as e :   
        print('exception occured')    
        print(e.args) 
        return redirect('language')

    return render(request,'resultpage.html',{'res':translation.text,'lang':lang,'cr':current_language.language})    
    

     
    
  