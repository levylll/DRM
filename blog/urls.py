from django.conf.urls import url
from blog.views import IndexView,ArticleView,AllView,SearchView,ColumnView,UserView,NewsView,TagView,CategoryView,JsyqView
from blog.views import NewjzView,JsbzView,BzfhView,XtzcView,SpsyView,SpzwView,CspgView
from django.views.generic import TemplateView,DetailView
from blog.models import News

urlpatterns = [
        url(r'^$',IndexView.as_view()),
        url(r'^article/(?P<slug>\w+).html$',ArticleView.as_view()),
        url(r'^all/$',AllView.as_view()),
        url(r'^newjz/$',NewjzView.as_view()),
        url(r'^jsbz/$',JsbzView.as_view()),
        url(r'^jsyq/$',JsyqView.as_view()),
        url(r'^bzfh/$',BzfhView.as_view()),
        url(r'^xtzc/$',XtzcView.as_view()),
        url(r'^spsy/$',SpsyView.as_view()),
        url(r'^spzw/$',SpzwView.as_view()),
        url(r'^cspg/$',CspgView.as_view()),
        url(r'^search/$',SearchView.as_view()),
        url(r'^login/$',TemplateView.as_view(template_name="blog/login.html")),
        url(r'^register/$',TemplateView.as_view(template_name="blog/register.html")),
        url(r'^forgetpassword/$',TemplateView.as_view(template_name="blog/forgetpassword.html")),
        url(r'^resetpassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',TemplateView.as_view(template_name="blog/resetpassword.html")),
        url(r'^column/(?P<column>\w+)$',ColumnView.as_view()),
        url(r'^user/(?P<slug>\w+)$',UserView.as_view()),
        url(r'^news/$',NewsView.as_view()),
        url(r'^news/(?P<pk>\w+)$',DetailView.as_view(model=News)),
        url(r'^tag/(?P<tag>\w+)/$',TagView.as_view()),
        url(r'^category/(?P<category>\w+)/$',CategoryView.as_view()),
]
