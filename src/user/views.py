from django.shortcuts import render,redirect
from forms import RegisterForm
from django.views.decorators.cache import cache_page

#ajustar esse registro
@cache_page(60*5)
def register(request):
    form=RegisterForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        try:
            if request.method=='POST':
                form=RegisterForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('register')
                context={
                    'form':form
                }
                return render(request,'register.html',context=context)

        except:
            print("error")