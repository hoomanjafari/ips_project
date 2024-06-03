from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.http import JsonResponse
import json
from .models import IpsProjects


# this is for rendering the main page for projects and we use paginator to separate the projects pages
class IpsProjectsView(View):
    def get(self, request):
        all_projects = IpsProjects.objects.all()
        paginator = Paginator(all_projects, 9)
        page = request.GET.get('page')
        projects = paginator.get_page(page)
        return render(request, 'projects/project.html', {'projects': projects})


# this view create a session to save the selected filter id_number
class IpsProjectFilteringView(View):
    def post(self, request):
        data = json.loads(request.body)
        request.session['filter_id'] = data['selected_filter_value']
        return JsonResponse({'data': data}, safe=True)


# this view take the selected filter id_number from the session and query to database and filter the specific projects
# and create the template for that projects and in front we use this view by using ajax to render the template
class FilterChangeTemplate(View):
    def get(self, request):
        data = request.session.get('filter_id')
        all_projects = None
        if data == '1':
            all_projects = IpsProjects.objects.all()
        elif data == '2':
            all_projects = IpsProjects.objects.filter(is_office=True)
        elif data == "3":
            all_projects = IpsProjects.objects.filter(is_coffe_restaurant=True)
        elif data == '4':
            all_projects = IpsProjects.objects.filter(is_home_villa=True)
        elif data == '5':
            all_projects = IpsProjects.objects.filter(is_zero_to_hundred=True)
        elif data == '6':
            all_projects = IpsProjects.objects.filter(is_facade=True)
        paginator = Paginator(all_projects, 9)
        page = request.GET.get('page')
        projects = paginator.get_page(page)

        return render(request, 'projects/projects_filtering.html', {'projects': projects})


# project details template
class IpsProjectDetailsView(View):
    def get(self, request, **kwargs):
        project = IpsProjects.objects.get(pk=kwargs['pk'])
        return render(request, 'projects/projects_details.html', {
            'project': project
        })


# searching view and it staffs
class SearchView(View):
    def get(self, request):
        if request.GET.get('search'):
            search = request.GET.get('search')
            request.session['searched_text'] = search
        searched_text = request.session.get('searched_text')
        result = None
        result_as_title = IpsProjects.objects.filter(project_title__contains=searched_text)
        result_as_details = IpsProjects.objects.filter(project_details__contains=searched_text)
        if result_as_title.exists():
            result = IpsProjects.objects.filter(project_title__contains=searched_text)
        elif result_as_details.exists():
            result = IpsProjects.objects.filter(project_details__contains=searched_text)
        elif result_as_details.exists() and result_as_title.exists():
            result = IpsProjects.objects.filter(
                project_title__contains=searched_text, project_details__contains=searched_text
                )
        if result is not None:
            paginator = Paginator(result, 9)
            page = request.GET.get('page')
            final_result = paginator.get_page(page)
            print('result is result :', final_result)
            return render(request, 'projects/search_result.html', {
                'projects': final_result, 'search_text': searched_text
            })
        return render(request, 'projects/search_result.html', {
            'projects': result, 'search_text': searched_text
        })
