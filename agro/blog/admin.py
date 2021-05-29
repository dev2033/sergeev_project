from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from . import models


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Post
        fields = '__all__'


class AboutAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.About
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.About, AboutAdmin)
