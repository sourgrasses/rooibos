from django import template
from rooibos.storage import get_thumbnail_for_record

register = template.Library()

@register.simple_tag
def thumbnail(record):
    media = get_thumbnail_for_record(record)    
    return media and media.get_absolute_url() or ''

@register.inclusion_tag('ui_record.html')
def record(record, selectable=False, selected_records=()):
    media = get_thumbnail_for_record(record)
    return {'record': record,
            'selectable': selectable,
            'selected': record.id in selected_records,
            'thumbnail': media and media.get_absolute_url() or '/static/images/nothumbnail.png'}

@register.inclusion_tag('ui_record_list.html')
def record_list(record, selectable=False, selected_records=()):
    return {'record': record,
            'selectable': selectable,
            'selected': record.id in selected_records,
            'icon': None or '/static/images/filetypes/none.png'}

@register.inclusion_tag('ui_session_status.html', takes_context=True)
def session_status(context):
    return {'selected': len(context['request'].session.get('selected_records', ())),
            }


@register.simple_tag
def dir2(var):
    return dir(var)

@register.filter
def scale(value, params):
    try:
        omin, omax, nmin, nmax = map(float, params.split())
        return (value - omin) / (omax - omin) * (nmax - nmin) + nmin
    except:
        return ''