from .models import Measurement
from app_mail.models import User

def add_variable_to_context(request):
    try:
        xx = User.objects.get(username=request.user.username)
        measurement = Measurement.objects.get(uid=xx.id)
        return {
            "measured":measurement
            }
    except:
        return {}

 