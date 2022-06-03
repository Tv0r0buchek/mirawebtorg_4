from typing import Dict, Any
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView  # views.generic хранит все классовые обработчики
from core.forms import CommentForm, AddProductForm
from core.models import *
from django.db.models import Avg
import json

# def home(request):
#     return render(request, "home.html")

# def FunclistView(request):
#     product_list = Product.objects.all()
#     return render(request, "home.html", {'product_list': product_list})

class ProductListView(ListView):
    model = Product  # Указываем классовому обработчику с какой моделью (базы данных) работать
    template_name = "core/home.html"
    context_object_name = "product_list"

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=int(request.POST.get("product_list_view_id")))
        product_to_basket = ShoppingCart(
            user=self.request.user,
            product=product

        )
        product_to_basket.save()
        return redirect("home")


class ProductDetailView(DetailView):
    model = Product
    template_name = "core/product.html"
    context_object_name = "product"
    temporary_data = None

    @staticmethod
    def round_custom(num, step=0.5):
        return round(num / step) * step

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["pictures_list"] = Photo.objects.filter(product_connected=self.get_object())
        data["comments"] = Review.objects.filter(product_connected=self.get_object())

        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        else:
            data['comment_form'] = CommentForm()
        if len(Review.objects.filter(product_connected=self.get_object())) > 0:
            average_rt = Review.objects.filter(product_connected=self.get_object()).aggregate(Avg('rating'))
            avr_intermediate = str(average_rt.get("rating__avg")).replace(",", ".")
            data["average_rating"] = self.round_custom(float(avr_intermediate))
        else:
            data["average_rating"] = 0

        # data["average_rating"] = average_rt.get("rating__avg")
        return data

    def post(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            body_data = json.loads(request.body.decode('utf-8'))
            key_ = body_data['key']
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' and key_ == "AddToBasket":
                this_user = self.request.user
                this_product = Product.objects.get(id=self.get_object().id)
                product_to_basket = ShoppingCart(
                    user=this_user,
                    product=this_product
                )
                if ShoppingCart.objects.filter(user=this_user, product=this_product).exists():
                    data_to_response = {"message": "product_already_exists"}
                else:
                    data_to_response = {"message": "product_added"}
                    product_to_basket.save()
                return HttpResponse(json.dumps(data_to_response))
        else:
            response = HttpResponse(json.dumps({'message': "UserAuthenticationFAIL"}),
                                    content_type='application/json', status=401)
            return response

        if request.POST.get("product_detail_form") == 'add_comment_form_two':
            if self.request.user.is_authenticated:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = Review(review=request.POST.get("review"),
                                     rating=request.POST.get("rating"),
                                     author=self.request.user,
                                     product_connected=self.get_object())
                    comment.save()
                    print(form.errors())
                else:
                    print(form.errors)
                    # raise Http404
                return redirect("product_detail", *args, **kwargs)


class AddProductView(TemplateView):
    template_name = "core/add_product.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form = AddProductForm
        data["add_form"] = form
        return data

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            ...
        print(request.POST, "словарь Post")
        print(request.headers, 'это headers')

        # current_slug = request.POST.get("slug")
        # product = Product(title=request.POST.get("title"),
        #                   description=request.POST.get("description"),
        #                   owner=self.request.user,
        #                   slug=current_slug,
        #                   price=request.POST.get("price"),
        #                   image1=request.FILES.get("image1"),
        #                   mark=request.POST.get("mark")
        #                   )
        # product.save()
        # product_object = Product.objects.get(slug = current_slug)
        # photos = request.FILES.getlist('get_images')
        # for photo in photos:
        #     Photo(image = photo, product_connected=product_object).save()

        return HttpResponse(json.dumps({"success":True}),content_type='application/json')


class BasketView(ListView):
    template_name = "core/basket.html"
    model = ShoppingCart
    context_object_name = "basket"

    def get_context_data(self, **kwargs):
        data: Dict[str, Any] = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            if ShoppingCart.objects.filter(user_id=user).exists():
                ShoppingCart.objects.all().filter(user=user)
                products = []
                for item in data["basket"]:
                    product_id = item.product.id
                    x = Product.objects.get(id=product_id)
                    products.append(x)
                data["products"] = products
        #     else:
        #         data["my_errors"] = "no_products_found"
        # else:
        #     data["my_errors"] = "is_not_authenticated"
        return data
