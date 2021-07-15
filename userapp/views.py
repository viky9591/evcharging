
from django.shortcuts import render ,redirect
from django.http import HttpResponse

from .models import admin_table, manager_table, slots_table, user_request, user_table,stations_table,history_table
from .forms import InputForm
import random
from datetime import datetime

# Create your views here.

def Index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html') 

def login(request):
    form = InputForm()
    
    if request.method == 'POST': #grtting from form
        
        username=request.POST['username']
        password=request.POST['password']   
        u=user_table.objects.get(username=username)
        if u.username==username and u.password==password:
           user=u
           
           return render(request,'home.html',{'user':user})        
    #creating form objuct
    return render(request,'login.html')   

#def login_back(request):
#username=request.POST['username']
    
     

"""if request.method=="POST":
        u=user_table.objects.get(username=username)
        name = u.username
        
        if u.username == request.POST['username'] and u.password == request.POST['password']:

            return redirect( request ,'home.html',usernam=name)"""
        
#return render(request ,'login.html',sword')})
     
    

def register_back(request):

    if request.method=="POST":
        u=user_request()
        u.username=request.POST['username']
        u.password=request.POST['password']
        u.email=request.POST['email']
        u.phoneno=request.POST['phone_no']
        u.save()
        
        return redirect('index')    
      

def home(request,id):
    user=user_table.objects.get(id=id)
    
    #context={'user':user}
    return render(request ,'home.html',{'user':user})    

def charging(request,id):
    user=user_table.objects.get(id=id)
    stations=stations_table.objects.all()
    loca='0000'  #giving empty values for booking..
    bno='0000'
    slot='0000'

    #passing history...
    uname=user.username
    his=history_table.objects.filter(username=uname)
    
    if request.method=="POST":
        loca1=request.POST['loc']
        #bno=random.randrange(0000,9999)
        today=datetime.now()
        loc=stations_table.objects.get(location=loca1)
        id=loc.id
        locn=slots_table.objects.all()
        for i in locn: #booking slot..

            if i.station_id_id==id:
                if i.booking_status=='avilable':
                    print('test')
                    
                    
                    slot=i.slotno
                    bno=random.randrange(0000,9999)
                    loca=loca1
                    hy=history_table() #history taible
                    hy.username=user.username
                    hy.dateTime=today
                    hy.bookingNo=bno
                    hy.location=loca
                    hy.slotno=slot
                    hy.save()

                    #bloking the slot
                    slots_table.objects.filter(slotno=slot).update(booking_status='booked')

                    break
       

    #user = 'vikas'
    #context={ 'user':user}
    return render(request ,'charging.html',{'user':user , 'stations':stations, 'loca':loca ,'bno':bno ,'slot':slot ,'his':his})

def about_us(request,id):
    user=user_table.objects.get(id=id)

    
    
    return render(request ,'about_us.html',{'user':user})    

  



#manager
def manager(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        temp=manager_table.objects.get(username=username)
        if temp.username==username and temp.password==password:
            return redirect('manager_page')
    return render(request, "manager_login.html") 

def manager_page(request):
    slot=slots_table.objects.all()
    

    temp=user_request.objects.all()
    history=history_table.objects.all()
    return render(request,'manager.html',{'temp':temp,'history':history,'slot':slot})  

def acharging(request):
    if request.method=='POST':
        bookingno=request.POST['bookingno']
        his=history_table.objects.get(bookingNo=bookingno)
        slot=his.slotno
        slots_table.objects.filter(slotno=slot).update(booking_status='avilable')
        return redirect('manager_page')


def allow_user(request):
    if request.method=='POST':
        id=request.POST['id']
        userp=user_request.objects.get(id=id)
        usert=user_table()
        usert.username=userp.username
        usert.password=userp.password
        usert.email=userp.email
        usert.phoneno=userp.phoneno
        usert.save()
        userp.delete()
        return redirect('manager_page')

def activate(requrst):
    if requrst.method=='POST':
        
        slot=requrst.POST['slno']
        slots_table.objects.filter(slotno=slot).update(booking_status='avilable')
        
        return redirect('manager_page')

def desable(requrst):
    if requrst.method=='POST':
        
        slot=requrst.POST['slno']
        slots_table.objects.filter(slotno=slot).update(booking_status='booked')
        
        return redirect('manager_page')            

#admin
def ev_admin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        temp=admin_table.objects.get(username=username)
        if temp.username==username and temp.password==password:
            

            return redirect('adminpage')
    return render(request,'admin_login.html') 


def adminpage(request):
    if request.method=='POST':
        l=stations_table()
        l.location=request.POST['loc']
        l.save()
        
    userprofiles=user_table.objects.all() 
    stations=stations_table.objects.all() 
    slot=slots_table.objects.all()      

    return render(request,'admin.html',{'userprofiles':userprofiles,'stations':stations,'slot':slot })

def addslots(request):
    if request.method=='POST':
        loc=request.POST['location']
        slno=request.POST['slotno']
        station=stations_table.objects.get(location=loc)
        slot=slots_table()
        slot.station_id=station
        slot.slotno=slno
        slot.save()
        return redirect('adminpage')   

def addman(request):
    if request.method=='POST':
        man=manager_table()
        man.username=request.POST['username']
        man.password=request.POST['password']
        man.save()
        return redirect('adminpage')  

def userprofile(request):
    if request.method=='POST':
        id=request.POST['id']
        u=user_table.objects.get(id=id)
        u.delete()
        return redirect('adminpage')   


#avtivate desable slot
def admin_activate(requrst):
    if requrst.method=='POST':
        
        slot=requrst.POST['slno']
        slots_table.objects.filter(slotno=slot).update(booking_status='avilable')
        
        return redirect('adminpage')

def admin_desable(requrst):
    if requrst.method=='POST':
        
        slot=requrst.POST['slno']
        slots_table.objects.filter(slotno=slot).update(booking_status='booked')
        
        return redirect('adminpage')            
               

    

