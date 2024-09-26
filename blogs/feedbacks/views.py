from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "feedbacks/review.html"
    success_url = "/reviews/thank-you"


"""
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "feedbacks/review.html"
    success_url = "/reviews/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


"""

"""
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "feedbacks/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/reviews/thank-you")

        return render(request, "feedbacks/review.html", {
            "form": form
        })
"""


class ThankYouView(TemplateView):

    # this works for any get type requst !
    template_name = "feedbacks/thank_you.html"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# class ReviewsListView(TemplateView):
#     template_name = "feedbacks/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "feedbacks/review_list.html"
    model = Review
    # context_object_name = "reviews" # To access the object by this keyword in the frontend
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=2)
        return data


class SingleReviewView(DetailView):
    template_name = "feedbacks/single_review.html"
    model = Review


# Create your views here.


# def review(request):
#     return render(request, "feedbacks/review.html")

# Create your views here.

# def review(request):
# if request.method == 'POST':
#     entered_username = request.POST['username']
#     print(entered_username)
#     # return HttpResponseRedirect("reviews/thank-you")
#     return HttpResponseRedirect("thank-you")

# return render(request, "feedbacks/review.html")
# if request.method == 'POST':
#     entered_username = request.POST['username']

#     if entered_username == "" and len(entered_username) >= 100:
#         return render(request, "reviews/review.html", {
#             "has_error": True
#         })
#     print(entered_username)
#     return HttpResponseRedirect("/thank-you")

# return render(request, "feedbacks/review.html", {
#     "has_error": False
# })


# class SingleReviewView(TemplateView):
#     template_name = "feedbacks/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

# def thank_you(request):
#     return render(request, "feedbacks/thank_you.html")


"""
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
        # form = ReviewForm(request.POST)

        # if form.is_valid():
        #     review = Review(
        #         user_name=form.cleaned_data['user_name'],
        #         review_text=form.cleaned_data['review_text'],
        #         rating=form.cleaned_data['rating'])
        #     review.save()
            return HttpResponseRedirect("/reviews/thank-you")

    else:
        form = ReviewForm()

    return render(request, "feedbacks/review.html", {
        "form": form
    })
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         
    #         valid input & is required & cleans & validated data
    #        
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect("/reviews/thank-you")

    # form = ReviewForm()

    # return render(request, "feedbacks/review.html", {
    #     "form": form
    # })
"""
