#coding:utf-8
from blog.models import Article,Category,Carousel,Nav,Column,News

import xadmin
from xadmin.layout import Main, Fieldset

class CategoryAdmin(object):
    search_fields = ('name',)
    list_filter = ('status','create_time')
    list_display = ('name','parent','rank','status')
    fields = ('name','parent','rank','status')



class ArticleAdmin(object):
    search_fields = ('title','summary')
    list_filter = ('status','category','is_top','create_time','update_time','is_top')
    list_display = ('title','category','author','status','is_top','update_time')

    form_layout = (
        Fieldset(u'基本信息',
                    'title','en_title','img','category','tags','author','is_top','rank','status'
                    ),
        Fieldset(u'内容',
                    'content'
                    ),
        Fieldset(u'摘要',
                    'summary'
                    ),
        Fieldset(u'时间',
                    'pub_time'
                    )
    )


class NewsAdmin(object):
    search_fields = ('title','summary')
    list_filter = ('news_from','create_time')
    list_display = ('title','news_from','url','create_time')
    fields = ('title','news_from','url','summary','pub_time')


class NavAdmin(object):
    search_fields = ('name',)
    list_display = ('name','url','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','url','status')


class ColumnAdmin(object):
    search_fields = ('name',)
    list_display = ('name','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','status','article','summary')
    filter_horizontal = ('article',)


class CarouselAdmin(object):
    search_fields = ('title',)
    list_display = ('title','article','img','create_time')
    list_filter = ('create_time',)
    fields = ('title','article','img','summary')


class GlobalSetting(object):
    site_title = u"ChinaDRM后台管理"
    site_footer = u"ChinaDRM"


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "欢迎",
            "content": "<h3> Welcome to Vmaig! </h3>\
                        <p>欢迎来到 ChinaDRM测试评估平台 ,如果有任何问题可以加:<br/>\
                        我的QQ：348878516<br/>\
                        email:levylll@163.com <br/><br/>\
                        <br/>"},
        ],
    ]


# xadmin.site.register(xadmin.views.CommAdminView,GlobalSetting)
xadmin.site.register(xadmin.views.website.IndexView, MainDashboard)

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Article,ArticleAdmin)
# xadmin.site.register(News,NewsAdmin)
# xadmin.site.register(Nav,NavAdmin)
# xadmin.site.register(Column,ColumnAdmin)
# xadmin.site.register(Carousel,CarouselAdmin)
