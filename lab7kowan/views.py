from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def render_index_page(request):
    context = {}
    if request.method == "POST":
        side_square = request.POST.get("side_square")
        side_cube = request.POST.get("side_cube")
        area_square = request.POST.get("area_square")
        area_cube = request.POST.get("area_cube")
        context["side_square"] = side_square
        context["side_cube"] = side_cube
        context["area_square"] = area_square
        context["area_cube"] = area_cube
        if "count_area_square" in request.POST:
            if side_square == None:
                area_square = "empty"
            elif not side_square.isdigit():
                area_square = "invalid"
            else:
                area_square = request_area_square(side_square)
            context["area_square"] = area_square
        elif "count_area_cube" in request.POST:
            if side_cube == None:
                area_cube = "empty"
            elif not side_cube.isdigit():
                area_cube = "invalid"
            else:
                area_cube = request_area_cube(side_cube)
            context["area_cube"] = area_cube
    return render(request, "index.html", context)

def request_area_square(side_square):
    url = "http://3.87.87.42:8080/function/area-square"
    json_req = {"side_square": int(side_square)}
    response = requests.post(url, json=json_req)
    area_square = response.json()["area_square"]
    return area_square

def request_area_cube(side_cube):
    url = "http://3.90.113.138:8080/function/area-cube"
    json_req = {"side_cube": int(side_cube)}
    response = requests.post(url, json=json_req)
    area_cube = response.json()["area_cube"]
    return area_cube