from django import forms

class ContactmeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','id':'firstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','id':'lastName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','id':'username','placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'type':'email','class':'form-control','id':'email','placeholder':'emailKamu@gmail.com',}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','id':'alamat','placeholder':'Apartment, suite, kontrakan, atau alamat rumah anda'}))
    pesan = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','id':'alamat','rows':'8','cols':'80','placeholder':'Masukkan Pesan Anda'}))
