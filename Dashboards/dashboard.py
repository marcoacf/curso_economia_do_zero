import vizro.plotly.express as px
from vizro import Vizro
import vizro.models as vm
import pandas as pd

cvm = pd.read_excel("CVM.xlsx", index_col="DATA")

page1 = vm.Page(
    title="Economia do Zero",
    layout=vm.Layout(grid=[[0,0],[1,2]]),
    components=[
        vm.Graph(id="scatter_chart1", figure=px.scatter(cvm, y="CAPTAÇÃO", color="NOME")),
        vm.Graph(id="bar_chart1", figure=px.bar(cvm, y="RESGATES", color="NOME")),
        vm.Graph(id="bar_chart_novo", figure=px.line(cvm, y="COTISTAS", color="NOME"))
    ],
    controls=[
        vm.Filter(column="NOME", selector=vm.Dropdown(value=["ALL"])),
    ],
)

page2 = vm.Page(
    title="Investimentos",
    components=[
        vm.Graph(id="scatter_chart2", figure=px.scatter(cvm, y="CAPTAÇÃO", color="NOME")),
        vm.Graph(id="bar_chart2", figure=px.bar(cvm, y="RESGATES", color="NOME")),
    ],
    controls=[
        vm.Filter(column="NOME", selector=vm.Dropdown(value=["ALL"])),
    ],
)

dashboard = vm.Dashboard(pages=[page1, page2],
                         navigation=vm.Navigation(
                            pages={"Investimentos no Brasil": ["Economia do Zero"],
                                "Investimentos no exterior": ["Investimentos"]})
)

Vizro().build(dashboard).run()