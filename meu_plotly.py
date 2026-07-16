import plotly.graph_objects as go

x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

fig = go.Figure(
    data=go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        name='Linha 01'
    )
)

fig.update_layout(
    title = "Gráfico de Linha Interativo",
    xaxis_title = "Eixo X",
    yaxis_title = "Eixo Y"
)

fig.show()