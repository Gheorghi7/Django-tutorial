from django.shortcuts import render


class About:
    @staticmethod
    def home(request, *args, **kwargs):
        my_context = {
            "my_text": "This is something about me",
            "my_num": 123,
            "my_list": [1,2,3,4,5]
        }
        return render(request, "home.html", my_context)

    @staticmethod
    def contact(request, *args, **kwargs):
        return render(request, "contact.html", {})
