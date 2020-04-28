from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import User,Client

# Create your views here.
def login(request):
    if request.method ==  'POST':
        user_id = request.POST['user_id']
        if User.objects.filter(user_id = user_id).exists():
            #print('!!!!!!!! user logged in !!!!!!!!!!!!!!', User.objects.all()[0].prefix)
            #print('!!!!!!!! user logged in 222!!!!!!!!!!!!!!', User.objects.get(pk=user_id).prefix)
            #print('!!!!!!!! user logged in 333!!!!!!!!!!!!!!', User.objects.get(user_id=user_id).client_id.client_type)
            userType = User.objects.get(user_id=user_id).client_id.client_type
            if userType == 'staff':
                return render(request, 'dashboard.html')
            else:     #if its a client
                return redirect('/')
        else:
            print('!!!!!!!! This user does not exist !!!!!!!!!!!!!!')
            return redirect('/')
        


def register(request):
    if request.method ==  'POST':
        user_id = request.POST['user_id']
        client_id = Client(client_id = request.POST['companyTypeSelect']) #ForeignKey
        prefix = request.POST['appellationTypeSelect']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        job_title = request.POST['job_title']
        email = request.POST['email']
        office_phone = request.POST['office_phone']
        cell_phone = request.POST['cell_phone']

        if User.objects.filter(user_id = user_id).exists():
            messages.info(request, 'User already exists. Please try different User name')
            return redirect('register')
        else:
            user = User(user_id = user_id, client_id=client_id, prefix=prefix, first_name=first_name, middle_name=middle_name, 
            last_name=last_name, job_title=job_title, email=email, office_phone=office_phone, cell_phone=cell_phone)

            user.save()
            #messages.info(request, 'User Created. Please login now.')
            return redirect('/')
    else:
        client_list = Client.objects.order_by('client_id')  #all client records
        context = {'client_list' : client_list}
        return render(request, 'register.html', context)