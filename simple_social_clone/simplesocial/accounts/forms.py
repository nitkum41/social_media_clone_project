from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class UserCreateForm(UserCreationForm): #should not have the same name
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super.__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'   #setting up label like on the html forms
            self.fields['email'].label = 'Email Address'
            
