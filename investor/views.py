from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InvestorResource
from .serializers import ResourceSerializer
from openpyxl import load_workbook
from rest_framework.pagination import LimitOffsetPagination

class InvestorResourceListView(APIView):
    def get(self, request):
        resources = InvestorResource.objects.all()
    
        if resources:
            paginator = LimitOffsetPagination()
            paginated_list = paginator.paginate_queryset(
                resources, request)
            data = ResourceSerializer(
                paginated_list, many=True).data
        else:
            paginator, data = None, []
    
        return Response(
            {
                "count": paginator.count,
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
                "result": data,
                "message": "Investor resources fetched successfully."
            },
            status=200
        )

def CreateInvestorResources(request):

    # Load the workbook
    file_path = "Book2.xlsx"  # Replace with your file path
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
        InvestorResource.objects.create(
            prompt = prompt,
            articles = articles,
            videos = videos
        )
        articles = []
        videos = []
        j -= 1