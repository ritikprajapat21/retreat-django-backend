from .models import Retreat, Booking
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import datetime
import requests


# To add seed data
def seed(request):
    url = "https://669f704cb132e2c136fdd9a0.mockapi.io/api/v1/retreats"
    res = requests.get(url)
    retreats = res.json()

    for retreat in retreats:
        item = Retreat(
            id=int(retreat["id"]),
            title=retreat["title"],
            description=retreat["description"],
            date=datetime.datetime.fromtimestamp(retreat["date"]),
            location=retreat["location"],
            price=retreat["price"],
            type=retreat["type"],
            condition=retreat["condition"],
            image=retreat["image"],
            tag=retreat["tag"],
            duration=retreat["duration"],
        )
        item.save()

    return Response({"message": "Data added"})


# To get all the data
class RetreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retreat
        fields = "__all__"


# I have used allow any for now, which in future can be changed to isAuthenticated for authenticated user only
@api_view(["GET"])
@permission_classes(
    [
        AllowAny,
    ]
)
def fetchRetreats(request):
    # to fetch all the retreats
    query = request.GET.get("filter", "")
    search = request.GET.get("search", "")
    location = request.GET.get("location", "")
    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 10))

    print(search, page)
    retreats = (
        Retreat.objects.all()
        .filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(condition__icontains=search)
            | Q(condition__icontains=query)
            | Q(location__iexact=location)
        )
        .values()
    )

    paginator = Paginator(retreats, limit)
    if page > paginator.num_pages:
        return Response({"data": "No more results"})
    list = paginator.get_page(page)

    data = RetreatSerializer(list, many=True).data
    return Response({"data": data})


# I have used allow any for now, which in future can be changed to isAuthenticated for authenticated user only
@api_view(["POST"])
@permission_classes(
    [
        AllowAny,
    ]
)
def book(request):
    user_id = request.data["userId"]
    retreat_id = request.data["retreatId"]
    payment_details = request.data["paymentDetail"]
    booking_date = request.data["date"]

    try:
        retreat = Retreat.objects.get(pk=retreat_id)

        user = User.objects.get(pk=user_id)

        booking = Booking(
            date=booking_date,
            payment_detail=payment_details,
            retreat=retreat,
            user=user,
        )

        booking.save()
        return Response({"data": "Booked successfully!"})
    except:
        return Response({"error": "Booking already done"})
