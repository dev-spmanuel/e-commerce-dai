from django import forms

CATEGORY_CHOICES = (
	("men's clothing", "Men's Clothing"),
	("women's clothing", "Women's Clothing"),
	("electronics", "Electronics"),
	("jewelery", "Jewelery")
)

class ProductoForm(forms.Form):
	title = forms.CharField(label='Nombre', max_length=100)
	price = forms.DecimalField(label='Precio')
	category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Categoría')
	description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label='Descripción')
	image = forms.FileField(label='Imagen')
	
class LoginForm(forms.Form):
	username = forms.CharField(label='Nombre de usuario', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')