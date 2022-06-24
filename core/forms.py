from django import forms
from core.models import \
    Review, \
    Product, \
    Category, \
    SubCategory, \
    LaptopCharacteristic, \
    GPU_Characteristic


class CommentForm(forms.ModelForm):
    review = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "comment_form", "placeholder": "Комментарий"}), label=""

    )
    OPTIONS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       choices=OPTIONS)

    class Meta:
        model = Review
        fields = ["review", "rating"]


class AddProductForm(forms.ModelForm):
    # title = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "area"}), label="")
    #
    # description = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "area"}), label="")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['description'].label = ""
    #     self.fields['owner'].label = ""
    #     self.fields['slug'].label = ""
    #     self.fields['price'].label = ""
    #     self.fields['image1'].label = ""
    #     self.fields['mark'].label = ""

    class Meta:
        model = Product
        fields = ["title", "description", "slug", "price", "image1", "mark", "sub_category"]


class ChoiseSubcategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name','categories']


class LaptopCharacteristicForm(forms.ModelForm):
    class Meta:
        model = LaptopCharacteristic
        exclude = ['product_connected']
