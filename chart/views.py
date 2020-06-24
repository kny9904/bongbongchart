# chart/views.py
from django.shortcuts import render
from .models import Passenger
from .models import Covid19_co
from .models import Covid19_de
from .models import Covid19_re
from .models import Covid19_coun
from django.db.models import Count, Q
from django.db.models import FloatField
from django.db.models.functions import Cast
import json
import pandas as pd
import numpy as np


def home(request):
    return render(request, 'home.html')


def covid19_korea(request):
# chart/views.py
# ...
    # Date,Australia,China,Japan,"Korea, South",Malaysia
 # 리스트 3종에 형식화된 값을 등록
    dataset = Covid19_co.objects.values('Date', 'Australia', 'China', 'Japan', 'Korea_South', 'Malaysia').order_by('Date')

    # 빈 리스트 3종 준비 (series 이름 뒤에 '_data' 추가)
    Date_data = list()  # for xAxis
    Australia_data = list()  # for series named 'Survived'
    China_data = list()  # for series named 'Not survived'
    Japan_data = list()
    Korea_South_data = list()
    Malaysia_data = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        Date_data.append(entry['Date'])
        Australia_data.append(entry['Australia'])
        China_data.append(entry['China'])
        Japan_data.append(entry['Japan'])
        Korea_South_data.append(entry['Korea_South'])
        Malaysia_data.append(entry['Malaysia'])

    Australia_rate = {
        'name': 'Australia',
        'data': Australia_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    China_rate = {
        'name': 'China',
        'data': China_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Japan_rate = {
        'name': 'Japan',
        'data': Japan_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Korea_South_rate = {
        'name': 'Korea, South',
        'data': Korea_South_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Malaysia_rate = {
        'name': 'Malaysia',
        'data': Malaysia_data,
        'pointInterval': 24 * 3600 * 1200,
    }

    chart = {
        'chart': {'type': 'spline', "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {'text': '[Covid-19] 확진자'},
        'subtitle': {'text': 'For the USA, China, Germany, France, United Kingdom, and Korea, South Confirm'},
        'xAxis': {'type': 'datetime', 'labels': {'format': '{value: %d. %b}'}},
        'yAxis': {'labels': {'format': '{value} 건/백만명', 'style': {'color': 'blue'}},
                  'title': {'text': '# of Cases per 1,000,000 People', 'style': {'color': 'blue'}}},
        'plotOptions': {'spline': {'lineWidth': 3, 'states': {'hover': {'lineWidth': 5}}}},
        'series': [Australia_rate, China_rate, Japan_rate, Korea_South_rate, Malaysia_rate],
        'navigation': {'menuItemStyle': {'fontSize': '10px'}}
    }

    dump = json.dumps(chart)
    return render(request, 'covid19_korea.html', {'chart': dump})



##Date,Australia,China,Japan,"Korea, South",Malaysia
def covid19_death(request):
    dataset = Covid19_de.objects.values('Date', 'Australia', 'China', 'Japan', 'Korea_South', 'Malaysia').order_by('Date')

    # 빈 리스트 3종 준비 (series 이름 뒤에 '_data' 추가)
    Date_data = list()  # for xAxis
    Australia_data = list()  # for series named 'Survived'
    China_data = list()  # for series named 'Not survived'
    Japan_data = list()
    Korea_South_data = list()
    Malaysia_data = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        Date_data.append(entry['Date'])
        Australia_data.append(entry['Australia'])
        China_data.append(entry['China'])
        Japan_data.append(entry['Japan'])
        Korea_South_data.append(entry['Korea_South'])
        Malaysia_data.append(entry['Malaysia'])

    Australia_rate = {
        'name': 'Australia',
        'data': Australia_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    China_rate = {
        'name': 'China',
        'data': China_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Japan_rate = {
        'name': 'Japan',
        'data': Japan_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Korea_South_rate = {
        'name': 'Korea, South',
        'data': Korea_South_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Malaysia_rate = {
        'name': 'Malaysia',
        'data': Malaysia_data,
        'pointInterval': 24 * 3600 * 1200,
    }

    chart = {
        'chart': {'type': 'spline', "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {'text': '[Covid-19] 사망자'},
        'subtitle': {'text': 'For the Australia,China,Japan,Korea, South,Malaysia Death'},
        'xAxis': {'type': 'datetime', 'labels': {'format': '{value: %d. %b}'}},
        'yAxis': {'labels': {'format': '{value} 건/백만명', 'style': {'color': 'blue'}},
                  'title': {'text': '# of Cases per 1,000,000 People', 'style': {'color': 'blue'}}},
        'plotOptions': {'spline': {'lineWidth': 3, 'states': {'hover': {'lineWidth': 5}}}},
        'series': [Australia_rate, China_rate, Japan_rate, Korea_South_rate, Malaysia_rate],
        'navigation': {'menuItemStyle': {'fontSize': '10px'}}
    }

    dump = json.dumps(chart)
    return render(request, 'covid19_death.html', {'chart': dump})


##Date,Australia,China,Japan,"Korea, South",Malaysia
def covid19_recover(request):
    dataset = Covid19_re.objects.values('Date', 'Australia', 'China', 'Japan', 'Korea_South', 'Malaysia').order_by('Date')

    # 빈 리스트 3종 준비 (series 이름 뒤에 '_data' 추가)
    Date_data = list()  # for xAxis
    Australia_data = list()  # for series named 'Survived'
    China_data = list()  # for series named 'Not survived'
    Japan_data = list()
    Korea_South_data = list()
    Malaysia_data = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        Date_data.append(entry['Date'])
        Australia_data.append(entry['Australia'])
        China_data.append(entry['China'])
        Japan_data.append(entry['Japan'])
        Korea_South_data.append(entry['Korea_South'])
        Malaysia_data.append(entry['Malaysia'])

    Australia_rate = {
        'name': 'Australia',
        'data': Australia_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    China_rate = {
        'name': 'China',
        'data': China_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Japan_rate = {
        'name': 'Japan',
        'data': Japan_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Korea_South_rate = {
        'name': 'Korea, South',
        'data': Korea_South_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Malaysia_rate = {
        'name': 'Malaysia',
        'data': Malaysia_data,
        'pointInterval': 24 * 3600 * 1200,
    }

    chart = {
        'chart': {'type': 'spline', "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {'text': '[Covid-19] 회복자'},
        'subtitle': {'text': 'For the Australia,China,Japan,Korea, South,Malaysia Recover'},
        'xAxis': {'type': 'datetime', 'labels': {'format': '{value: %d. %b}'}},
        'yAxis': {'labels': {'format': '{value} 건/백만명', 'style': {'color': 'blue'}},
                  'title': {'text': '# of Cases per 1,000,000 People', 'style': {'color': 'blue'}}},
        'plotOptions': {'spline': {'lineWidth': 3, 'states': {'hover': {'lineWidth': 5}}}},
        'series': [Australia_rate, China_rate, Japan_rate, Korea_South_rate, Malaysia_rate],
        'navigation': {'menuItemStyle': {'fontSize': '10px'}}
    }

    dump = json.dumps(chart)
    return render(request, 'covid19_recover.html', {'chart': dump})



##Date,Australia,China,Japan,"Korea, South",Malaysia
def covid19_country(request):
    dataset = Covid19_coun.objects.values('Date', 'Australia', 'China', 'Japan', 'Korea_South', 'Malaysia').order_by('Date')

    # 빈 리스트 3종 준비 (series 이름 뒤에 '_data' 추가)
    Date_data = list()  # for xAxis
    Australia_data = list()  # for series named 'Survived'
    China_data = list()  # for series named 'Not survived'
    Japan_data = list()
    Korea_South_data = list()
    Malaysia_data = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        Date_data.append(entry['Date'])
        Australia_data.append(entry['Australia'])
        China_data.append(entry['China'])
        Japan_data.append(entry['Japan'])
        Korea_South_data.append(entry['Korea_South'])
        Malaysia_data.append(entry['Malaysia'])

    Australia_rate = {
        'name': 'Australia',
        'data': Australia_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    China_rate = {
        'name': 'China',
        'data': China_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Japan_rate = {
        'name': 'Japan',
        'data': Japan_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Korea_South_rate = {
        'name': 'Korea, South',
        'data': Korea_South_data,
        'pointInterval': 24 * 3600 * 1200,
    }
    Malaysia_rate = {
        'name': 'Malaysia',
        'data': Malaysia_data,
        'pointInterval': 24 * 3600 * 1200,
    }

    chart = {
        'chart': {'type': 'spline', "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {'text': '[Covid-19] 합계'},
        'subtitle': {'text': 'For the Australia,China,Japan,Korea, South,Malaysia Country'},
        'xAxis': {'type': 'datetime', 'labels': {'format': '{value: %d. %b}'}},
        'yAxis': {'labels': {'format': '{value} 건/백만명', 'style': {'color': 'blue'}},
                  'title': {'text': '# of Cases per 1,000,000 People', 'style': {'color': 'blue'}}},
        'plotOptions': {'spline': {'lineWidth': 3, 'states': {'hover': {'lineWidth': 5}}}},
        'series': [Australia_rate, China_rate, Japan_rate, Korea_South_rate, Malaysia_rate],
        'navigation': {'menuItemStyle': {'fontSize': '10px'}}
    }

    dump = json.dumps(chart)
    return render(request, 'covid19_country.html', {'chart': dump})







def ticket_class_view_2(request):  # 방법 2
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False)),
                  averages_count=Cast(Count('ticket_class', filter=Q(survived=True)), FloatField()) / Cast(Count('ticket_class'),FloatField()) * 100
                  ) \
        .order_by('ticket_class')

    # 빈 리스트 3종 준비
    categories = list()             # for xAxis
    survived_series = list()        # for series named 'Survived'
    not_survived_series = list()    # for series named 'Not survived'
    averages_series = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])    # for xAxis
        survived_series.append(entry['survived_count'])          # for series named 'Survived'
        not_survived_series.append(entry['not_survived_count'])  # for series named 'Not survived'
        averages_series.append(entry['averages_count'])

    # json.dumps() 함수로 리스트 3종을 JSON 데이터 형식으로 반환
    return render(request, 'ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series),
        'averages_series': json.dumps(averages_series)
    })