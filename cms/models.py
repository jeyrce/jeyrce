from django.db import \
    models
from django.core.exceptions import \
    ValidationError
from django.utils.translation import \
    gettext_lazy as _

link = "link"
banner = "banner"
avatar = "avatar"


# 轮播图资源
class Banner(models.Model):
    name = models.CharField(max_length=64, verbose_name="图片名称", blank=False, null=False)
    image = models.ImageField(verbose_name="图片", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = "轮播图"

    def __str__(self):
        return self.name


# 百分比校验,只允许录入 60-100 范围
def validate_percent(value):
    if value < 60 or value > 100:
        raise ValidationError(
            _("%(value) is out of range"),
            params={
                "value": value}
        )


# 技能列表
class Skill(models.Model):
    percent = models.IntegerField(
        blank=False, null=False, verbose_name="熟练度", validators=(
        validate_percent,), help_text="范围[60,100]"
    )
    desc = models.TextField(max_length=128, blank=False, verbose_name="技能描述")

    class Meta:
        verbose_name_plural = verbose_name = "技能"

    def __str__(self):
        return self.desc


# 工作经历
class Experience(models.Model):
    start = models.DateField(verbose_name="开始时间", blank=False, null=True)
    end = models.DateField(verbose_name="结束时间", blank=True, null=True)
    company = models.CharField(max_length=64, blank=False, null=False, verbose_name="公司名称")
    role = models.CharField(max_length=20, blank=False, null=False, verbose_name="职位")
    desc = models.TextField(max_length=200, blank=False, null=False, verbose_name="工作描述")

    class Meta:
        verbose_name_plural = verbose_name = "工作经历"

    def __str__(self):
        return self.company


work_project = "work"
self_project = "self"


# 项目
class Project(models.Model):
    project_types = (
        (
        work_project,
        "工作项目"),
        (
        self_project,
        "自有项目"),
    )
    name = models.CharField(max_length=32, blank=False, verbose_name="项目名称")
    type = models.CharField(max_length=16, blank=False, choices=project_types, verbose_name="项目类型", help_text="区分工作项目和自己的项目")
    url = models.URLField(blank=True, null=True, verbose_name="线上地址")
    desc = models.TextField(max_length=300, verbose_name="项目描述", blank=False)

    class Meta:
        verbose_name_plural = verbose_name = "项目"

    def __str__(self):
        return self.name


# 系统配置
class System(models.Model):
    title = models.CharField(max_length=64, blank=False, verbose_name="网页标题", unique=True)
    avatar = models.ImageField(verbose_name="头像")
    center = models.CharField(max_length=20, blank=False, verbose_name="页面中心标题")
    introduction = models.TextField(max_length=200, verbose_name="自我介绍", blank=False)
    about = models.TextField(max_length=500, blank=False, verbose_name="关于我")
    skill_desc = models.TextField(max_length=200, blank=True, verbose_name="技能描述")
    exp_desc = models.TextField(max_length=200, blank=True, verbose_name="经历描述")
    mail = models.EmailField(blank=False, null=False, verbose_name="联系邮箱")
    page = models.URLField(blank=False, null=False, verbose_name="联系网址")
    footer = models.CharField(blank=False, max_length=64, verbose_name="底部字样")
    icp = models.CharField(blank=True, max_length=128, verbose_name="工信部备案")
    icp_link = models.URLField(blank=True, verbose_name="工信部验证地址")
    pcp = models.CharField(max_length=128, blank=True, verbose_name="公安网备案")
    pcp_link = models.URLField(blank=True, verbose_name="公安网验证地址")

    class Meta:
        verbose_name_plural = verbose_name = "系统配置"

    def __str__(self):
        return self.title


# SEO 站长平台
class Spider(models.Model):
    name = models.CharField(max_length=64, verbose_name="搜索引擎", blank=False, null=False)
    code = models.CharField(max_length=64, verbose_name="认证代码", blank=False, null=False)

    class Meta:
        verbose_name_plural = verbose_name = "站长平台"

    def __str__(self):
        return self.name
