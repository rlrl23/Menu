from django import template
from ..models import MenuItem, Menu
from django.shortcuts import get_object_or_404

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu):
    """Формируем пункты меню (по названию меню)"""
    try:
        # Получаем пункты определенного меню из БД
        menu_items = MenuItem.objects.filter(menu__name=menu)
        # Фильтруем пункты на дочерние и родительские
        parents = menu_items.filter(level=1).values()
        children = menu_items.exclude(level=1).values()
        for parent in parents:
            #Для каждого родительского элемента получаем список дочерних
            parent['children']=get_child(children, parent['id'])
        # Находим активный элемент меню по текущему url страницы
        current_url = context.request.get_full_path()
        try:
            active_item=get_object_or_404(menu_items, url=current_url)
            # Получаем список из id текущего и родительских пунктов меню
            selected_item_id_list = get_selected_item_id_list(active_item, parents, active_item.id)
            context['open_items'] = selected_item_id_list
        except:
            context['open_items']=[]

        return {
            "menu": parents,
            'context':context,
        }
    except Menu.DoesNotExist:
        return {'menu': menu_items, 'context': context}


def get_child(children, parent_id):
    """Получаем список всех дочерних элементов по id родителя"""
    item_list = children.filter(parent=parent_id)
    if item_list:
        for item in item_list:
            # Ищем дочерние элементы для каждого дочернего элемента
            item['children']=get_child(children, item['id'])
    #возвращаем вложенный список дочерних элементов
    return item_list

def get_selected_item_id_list(parent, primary_item, selected_item_id):
    """Получаем список id открытых элементов меню"""
    selected_item_id_list = []

    while parent:
        selected_item_id_list.append(parent.id)
        parent = parent.parent
    if not selected_item_id_list:
        for item in primary_item:
            if item['id'] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list