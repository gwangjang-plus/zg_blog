from django import template 

#注册过滤器
register = template.Library()

@register.inclusion_tag("my_tag/headers.html")
def banner(menu_name):
    img_list=["https://img1.baidu.com/it/u=1347492434,3189251794&fm=253&fmt=auto&app=120&f=JPEG?w=1422&h=800",
              "https://img0.baidu.com/it/u=2554737646,2600608678&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500",
              "https://img2.baidu.com/it/u=72752476,2781962848&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
    ]
    return {"img_list":img_list}