from django.views import generic
from CustomUser.mixins import LoginRequiredMixin
from posts.models import Post
import datetime

class DashboardView(generic.TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        user = self.request.user

        # How many leads we have in total
        total_lead_count = Post.objects.all().count()

        # How many new leads in the last 30 days
        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)

        # total_in_past30 = Lead.objects.filter(
        #     organisation=user.userprofile,
        #     date_added__gte=thirty_days_ago
        # ).count()
        total_in_past30 = 15

        # How many converted leads in the last 30 days
        # converted_category = Category.objects.get(name="Converted")
        converted_in_past30 = Post.objects.all().count()

        context.update({
            "total_lead_count": total_lead_count,
            "total_in_past30": total_in_past30,
            "converted_in_past30": converted_in_past30
        })
        return context
