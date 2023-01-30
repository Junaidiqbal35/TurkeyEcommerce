#it takes a request as an argument it will return the dictionary of data as a context 
from .models import Category
from .models import SubCategory

#------------------------------------------------------------------
def menu_links(request):
    #all the categories from database
    links = Category.objects.all()
    sublinks= SubCategory.objects.all()
    return dict(links=links,sublinks=sublinks)

#-------------------------------------------------------------------