from django.shortcuts import render
from .models import Product
from .pagination import set_pagination
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def home(request):
    """
    Render the home page view.

    This view requires authentication, redirecting to the '/' URL if the user is not logged in.

    The view retrieves a list of product variants, orders them by descending ID, filters out variants without an 'price_englishelm' value,
    paginates the results using the set_pagination function, and renders the 'back/home.html' template with the paginated variants.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered 'back/home.html' template with the paginated variants in the context.

    Note:
        - This view assumes the use of Django's render function to render templates.
        - The view assumes the existence of a 'Product' model with the necessary fields.
        - The 'set_pagination' function is used to perform pagination for the product variants.
        - The 'back/home.html' template is expected to exist and contain the necessary markup for displaying the product variants.
    """

    # #set the pagination on products li
    variants = Product.objects.all().order_by('-id')
    variants = set_pagination(request, variants)
    context = {
               'variants':variants,
               }

    return render(request, 'back/home.html', context)