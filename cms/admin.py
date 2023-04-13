from django.contrib import \
    admin

from cms.models import *

admin.site.site_header = "CMS"
admin.site.site_title = "CMS"

class Admin(admin.ModelAdmin):
    list_per_page = 100


class BannerAdmin(Admin):
    pass


admin.site.register(Banner, BannerAdmin)


class SkillAdmin(Admin):
    pass


admin.site.register(Skill, SkillAdmin)


class ExperienceAdmin(Admin):
    pass


admin.site.register(Experience, ExperienceAdmin)


class ProjectAdmin(Admin):
    pass


admin.site.register(Project, ProjectAdmin)


class SystemAdmin(Admin):
    pass


admin.site.register(System, SystemAdmin)


class SpiderAdmin(Admin):
    pass


admin.site.register(Spider, SpiderAdmin)
