from django.db import models

#create your models here.
class carro ( models.Model ):
    title = models.TextField(max_length=255)
    def myView(request):
        car_list = [{'title': 'BMW'}, {'title': 'Mazda'}]
        context = {'car_list': car_list}
        return render(request, 'my_first_app/car_list.html', context)
  
