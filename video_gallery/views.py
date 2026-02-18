from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video


from django.shortcuts import render



from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Video

def video_gallery(request):
    return render(request, "video_gallery.html")



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer  # Import the VideoSerializer
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from .models import Video
from .serializers import VideoSerializer

@api_view(['GET'])
def video_list(request):
    # Get the page number from the request, default to 1
    page_number = request.GET.get('page', 1)

    try:
        page_number = int(page_number)
    except ValueError:
        page_number = 1  # If the page parameter is invalid, fallback to page 1

    # Fetch all videos from the database
    videos = Video.objects.all().order_by('-uploaded_at')

    # Paginate the videos (6 videos per page)
    paginator = Paginator(videos, 6)

    # Handle the pagination and catch the `EmptyPage` exception
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        raise Http404("Invalid page.")  # Raise 404 if page is out of range

    # Serialize the videos
    serializer = VideoSerializer(page.object_list, many=True)

    # Return the paginated response
    return Response({
        'results': serializer.data,
        'count': paginator.count,
        'page': page.number,
        'pages': paginator.num_pages,
    })
