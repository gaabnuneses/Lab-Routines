import plotly.graph_objects as go
def initializePlot(xlim,ylim,title,xtitle,ytitle):
    fig = go.Figure()
    fig.update_layout(
        autosize=False,
        width=800,
        height=800,
        template="plotly_white",
        xaxis_showgrid=False, yaxis_showgrid=False,
    )
    fig.update_xaxes(showline=True,ticks="inside",tickwidth=2, linewidth=2, linecolor='black', mirror=True,title_text=xtitle)
    fig.update_yaxes(showline=True,ticks="inside",tickwidth=2, linewidth=2, linecolor='black', mirror=True,title_text=ytitle)

        # Título do gráfico
    #     fig.update_layout(title="$\\text{Água (Deionizada), }\\dot{\\Omega} = "+str(Ac)+"rad/s^2, T=25^0C$",title_x=0.5)
    #     fig.update_layout(title="$\\text{PEO Mv = 0.6M, C=750ppm, }\\dot{\\Omega} = "+str(Ac)+"rad/s^2, T=25^0C$",title_x=0.5)

def digaOi():
    print("OI")