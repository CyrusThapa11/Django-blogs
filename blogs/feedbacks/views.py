from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
from django.views import View

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


def thank_you(request):
    return render(request, "feedbacks/thank_you.html")


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
