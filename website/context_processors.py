from .models import Tab

def add_variable_to_context(request):
    return {
        'tabs': Tab.objects.all()
    }