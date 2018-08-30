from django import forms
from .models import Collection, Product, Shape, Style, Fabric
import django_filters



class WeddingCollectionFilter(django_filters.FilterSet):
    # p_name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    collection = django_filters.ModelMultipleChoiceFilter(queryset=Collection.objects.filter(category__slug='wedding_dress'), widget=forms.CheckboxSelectMultiple)
    shape = django_filters.ModelMultipleChoiceFilter(queryset=Shape.objects.all(), widget=forms.CheckboxSelectMultiple)
    style = django_filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), widget=forms.CheckboxSelectMultiple)
    fabric = django_filters.ModelMultipleChoiceFilter(queryset=Fabric.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['collection', 'shape', 'style', 'fabric', ]



class EveningCollectionFilter(django_filters.FilterSet):
    collection = django_filters.ModelMultipleChoiceFilter(queryset=Collection.objects.filter(category__slug='evening_dress'), widget=forms.CheckboxSelectMultiple)
    shape = django_filters.ModelMultipleChoiceFilter(queryset=Shape.objects.all(), widget=forms.CheckboxSelectMultiple)
    style = django_filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), widget=forms.CheckboxSelectMultiple)
    fabric = django_filters.ModelMultipleChoiceFilter(queryset=Fabric.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['collection', 'shape', 'style', 'fabric', ]
