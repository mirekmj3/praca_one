from django.shortcuts import render
from .models import SWATH
from .forms import SWATHform, SWATHform3
from tablib import Dataset
from .resources import SWATHResource
import plotly.express as px
import pandas
from matplotlib import pyplot

# Create your views here.

def home(request):
    form = SWATHform()
    context = {'form': form}
    return render (request, "glowna/home.html", context)

def importExcel(request):
    if request.method == 'POST':
        SWATH_resource = SWATHResource()
        dataset = Dataset()
        new_SWATH = request.FILES['plikExcel']
        imported_data = dataset.load(new_SWATH.read(), format='xlsx')
        for data in imported_data:
            value = SWATH(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
            )
            value.save()
    return render(request, 'glowna/wczytaj.html')


def graf(request):
    daneSwath = SWATH.objects.all()
    # daneSwath1 = daneSwath.values()
    # daneSwath2 = pandas.DataFrame(daneSwath1)
    poczatek = request.GET.get('poczatek')
    koniec = request.GET.get('koniec')

    if poczatek:
        daneSwath = daneSwath.filter(Hp_26695__gte=poczatek)
    if koniec:
        daneSwath = daneSwath.filter(Hp_26695__lte=koniec)

    #1
    
    

    figure = px.scatter(
        x = [c.Hp_26695 for c in daneSwath],        
        y= [[c.comp_delta for c in daneSwath],[c.comp_wt for c in daneSwath],[c.delta_wt for c in daneSwath]],
        title="wyniki analizy SWATH-MS",        
        labels={'x':'geny H. pylori', 'value':'relatywna ekspresja', 'variable':'porownywane warianty'}
    )

    # figure.update_layout(title={
    #     'font_size':22,
    #     'xanchor':'center',
    #     'x': 0.5
    # })

    #2
    
    # figure, axs = px.subplots(2)

    # axs[0].plot(daneSwath2['Hp_26695'], daneSwath2['comp_delta'],'o', color='g', label='comp_delta')
    # axs[0].plot(daneSwath2['Hp_26695'], daneSwath2['comp_wt'],'o', color='r', label='comp_delta')
    # axs[0].plot(daneSwath2['Hp_26695'], daneSwath2['delta_wt'],'o', color='b', label='comp_delta')
    # axs[0].set_xlim([650,680])
    # axs[0].set_ylim([0,15])
    # axs[0].legend()

    # axs[1].plot(daneSwath2['Hp_26695'], daneSwath2['comp_delta'],'o', color='g', label='comp_delta')
    # axs[1].plot(daneSwath2['Hp_26695'], daneSwath2['comp_wt'],'o', color='r', label='comp_delta')
    # axs[1].plot(daneSwath2['Hp_26695'], daneSwath2['delta_wt'],'o', color='b', label='comp_delta')
    # axs[1].set_xlim([650,680])
    # axs[1].set_ylim([0,15])
    # axs[1].legend()

    #3

    # figure = px.scatter(
    #     daneSwath2, x='Hp_26695', y=['comp_delta','comp_wt','delta_wt'],
    #     title="wyniki analizy SWATH-MS",
    #     labels={'x':'geny H. pylori', 'y':'relatywna ekspresja'}
    #     )
    
    figure.update_layout(
        title={'font_size':22,'xanchor':'center','x': 0.5},
        )

    newnames = {'wide_variable_0':'comp/delta', 'wide_variable_1':'comp/wt', 'wide_variable_2':'delta/wt'}
    figure.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )

    graf = figure.to_html()
    context = {'graf': graf, 'form':SWATHform3()}
    return render(request, "glowna/graf.html", context)