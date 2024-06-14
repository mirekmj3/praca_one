from import_export import resources
from .models import SWATH

class SWATHResource(resources.ModelResource):
    class meta:
        model = SWATH