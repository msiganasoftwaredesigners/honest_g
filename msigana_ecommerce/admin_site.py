from django.contrib.admin import AdminSite as DjangoAdminSite
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _
from django.urls import resolve
from django.http import Http404


class AdminSite(DjangoAdminSite):
    site_header = 'Samia Login'
    site_title = 'Samia Admin'

    def each_context(self, request):
        context = super().each_context(request)
        # Always include the Google Analytics link globally in the admin context
        # context['google_analytics_link'] = '<a href="https://analytics.google.com/analytics/web/#/p475799612/reports/intelligenthome" target="_blank">Google Analytics</a>'
        return context

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Get the resolved app_label from the request URL
        resolved_url = resolve(request.path_info)
        app_label = resolved_url.kwargs.get('app_label')

        if app_label:
            # If app_label is present in the URL, filter app_list accordingly
            app_list = [app_dict.get(app_label)]
        else:
            # If no app_label present, show all apps
            app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        order = [
        'reservations', 'catering', 'menu', 'store',
        'blog', 'happening', 'heads', 'footer',
        'gallery', 'video_gallery'
        ]  

        reordered = []
        for label in order:
            app = next((a for a in app_list if a['app_label'] == label), None)
            if app:
               app_list.remove(app)
               reordered.append(app)

        # Add remaining apps (not listed in `order`) at the end
        reordered += app_list

        return reordered

        


    
      
    
    
    def app_index(self, request, app_label, extra_context=None):
        app_list = self.get_app_list(request)

        if not app_list:
            raise Http404("The requested admin page does not exist.")

        context = {
            **self.each_context(request),
            "title": _("%(app)s administration") % {"app": app_list[0]["name"]},
            "subtitle": None,
            "app_list": app_list,
            "app_label": app_label,
        **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(
            request,
            self.app_index_template
            or ["admin/%s/app_index.html" % app_label, "admin/app_index.html"],
            context,
        )



admin_site = AdminSite(name='admin')