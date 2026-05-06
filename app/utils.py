from typing import List, Dict, Any
from .schemas import SaleItem


def analyze_sales_data(data : List[SaleItem]) -> Dict[str, Any]:
    dishes = []
    total_revenue = 0.0
    total_margin = 0.0
    for dish in data:
        # Считаем показатели для каждого блюда
        revenue = dish.selling_price * dish.quantity
        cost = dish.cost_price * dish.quantity
        margin = revenue - cost
        margin_percent = (revenue / cost) * 100

        # Увеличиваем общие доход и маржу
        total_revenue += revenue
        total_margin += margin

        # Добавляем в список словарей текущее блюдо
        dishes.append({
            "dish": dish.dish,
            "margin_percent": margin_percent,
            "margin": margin,
            "revenue": revenue,
            "quantity": dish.quantity,
            "selling_price": dish.selling_price
        })

    dishes.sort(key=lambda x: x['margin_percent'], reverse=True)  # Сортируем блюда по маржинальности

    top_margin_dishes = [x['dish'] for x in dishes[:3]]  # Берём первых 3 по маржинальности

    # Все блюда с маржой меньше 30% Закидываем в этот словарь
    loss_making = [x['dish'] for x in dishes if x['margin_percent'] < 30]

    suggestions = []
    suggestions.append(f'Возможно стоит поднять цену на {dishes[-1]['dish']}')

    # Добавляем предложения в массив suggestions
    for dish in dishes:
        if dish['margin'] > 100:
            suggestions.append(
                f'{dish['dish']} очень выгодно продаётся, возможно, стоит продвигать это блюдо активнее?')

        if dish['margin'] < 30:
            suggestions.append(
                f'{dish['dish']} продаётся с низкой маржой, возможно стоит повысить цену?')

    # Берем первые 3 предложения, чтобы не было огромных массивов с предложениями
    suggestions = suggestions[:3]

    return {
        "top_margin_dishes": top_margin_dishes,
        "loss_making": loss_making,
        "total_revenue": total_revenue,
        "total_margin": total_margin,
        "suggestions": suggestions}