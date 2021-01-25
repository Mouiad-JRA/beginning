from django import forms

from .models import  Products
#build-in method to transformation  Django form to html form {{ form.as_p }}
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ] #all have to do is rander this in the veiw