from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from models import Item
from resource import PrettyJSONSerializer

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username', 'first_name', 'last_name', 'last_login']
		serializer = PrettyJSONSerializer()

class ItemResource(ModelResource):
	class Meta:
		# Should be sorted by most recently updated
		queryset = Item.objects.all()
		resource_name = 'item'
		serializer = PrettyJSONSerializer()