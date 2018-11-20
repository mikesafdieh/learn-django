from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


########################################
### Using HyperlinkedModelSerializer ###
########################################

# The `HyperlinkedModelSerializer` has the following differences from `ModelSerializer`:
# 1 - It does not include the `id` field by default.
# 2 - It includes a `url` field, using `HyperlinkedIdentityField`.
# 3 - Relationships use `HyperlinkedRelatedField`, instead of `PrimaryKeyRelatedField`.


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # same type as `url` field

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


#############################
### Using ModelSerializer ###
#############################

'''
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # NOTE: Because 'snippets' is a reverse relationship on the User model, it will not be 
    # included by default when using the `ModelSerializer` class, so we needed to add an 
    # explicit field for it.

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Could have used `CharField(read_only=True)` here as well.
    # This field will not be used when updating model instances (since it's read-only).
    # Since we specified 'owner.username', the owner field will only be represented as
    # a username of the given User instance (as oppossed to a full user object).

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'title', 'code', 'linenos', 'language', 'style')
'''


#####################################
### Without using ModelSerializer ###
#####################################

'''
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''


### Serialization/Deserialization Example ###
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io

# ## Serialization:
# snippet = Snippet(code='print "hello, world"\n')
# serializer = SnippetSerializer(snippet)

# # render data into JSON string
# content = JSONRenderer().render(serializer.data)

# ## Deserialization:

# # parsing a stream into Python native types:
# stream = io.BytesIO(content)
# data = JSONParser().parse(stream) # data is a simple python dictionary

# # take those native types and populate an object instance with them;
# serializer = SnippetSerializer(data=data)
# serializer.is_valid()
# serializer.save() # this creates/updates a Snippet

