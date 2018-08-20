from django.shortcuts import render


def project_list(request):
    return render(request, 'budget/project-list.html')


def project_detail(request, project_slug):
    # fetch correct project
    return render(request, 'budget/project-detail.html')
