from django.shortcuts import render

# Create your views here.

def data_insert_filters(request):
    import datetime
    dt=datetime.datetime.now()
    data='hoW Are U Friends'
    d={'data':data,'c':1,'dt':dt}
    return render(request,'data_insert_filters.html',d)