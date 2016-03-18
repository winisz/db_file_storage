# django
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.translation import ugettext as _
from wsgiref.util import FileWrapper
# project
from db_file_storage.storage import DatabaseFileStorage


storage = DatabaseFileStorage()


def get_file(request, add_attachment_headers):
    name = request.GET.get('name')

    try:
        _file = storage.open(name)
    except Exception:
        return HttpResponseBadRequest(_('Invalid request'))

    response = HttpResponse(
        FileWrapper(_file),
        content_type=_file.mimetype
    )

    if add_attachment_headers:
        response['Content-Disposition'] = \
            'attachment; filename=%(name)s' % {'name': _file.filename}

    return response
