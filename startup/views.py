from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resource
from .serializers import ResourceSerializer
from openpyxl import load_workbook

class ResourceListView(APIView):
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

def CreateStartupResources(request):

    # Load the workbook
    file_path = "Book1.xlsx"  # Replace with your file path
    workbook = load_workbook(file_path)

    # Access a sheet by name
    sheet = workbook["Sheet1"]
    
    # Iterate through rows
    rows = []
    for row in sheet.iter_rows(values_only=True): # Each row as a tuple
        rows.append(row)
    
    i = 0
    j = len(rows)
    articles = []
    videos = []
    while j:
        if rows[i][2]:
            articles.append(rows[i][2])
        if rows[i][3]:
            videos.append(rows[i][3])
        prompt = rows[i][1]
        i += 1
        while rows[i][0] == None:
            if rows[i][2]:
                articles.append(rows[i][2])
            if rows[i][3]:
                videos.append(rows[i][3])
            i += 1
        print(prompt, articles, videos)
        Resource.objects.create(
            prompt = prompt,
            articles = articles,
            videos = videos
        )
        articles = []
        videos = []
        j -= 1