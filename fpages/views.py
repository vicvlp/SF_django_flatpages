from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import get_object_or_404, render


@staff_member_required(login_url="/accounts/login/")
def private_flatpage(request):
    """Render the protected FlatPage only for active staff/admin users."""
    flatpage = get_object_or_404(
        FlatPage,
        url="/private/",
        sites__id=settings.SITE_ID,
    )
    template_name = flatpage.template_name or "flatpages/default.html"
    return render(request, template_name, {"flatpage": flatpage})
