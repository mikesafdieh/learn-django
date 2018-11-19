from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


## without using ModelSerializer:
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

