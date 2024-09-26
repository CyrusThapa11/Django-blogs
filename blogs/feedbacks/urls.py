from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    # path("thank-you", views.thank_you)
    path("all", views.ReviewsListView.as_view(), name="review-list"),
    path("thank-you", views.ThankYouView.as_view()),
    # DYNAMIC PATH SEGMENT !
    path("<int:pk>", views.SingleReviewView.as_view())
]
