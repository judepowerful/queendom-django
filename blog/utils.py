from blog.forms import FeedbackForm

def inject_form(request):
    return {'feedback_form': FeedbackForm()}