import dash
from dash import dcc, html
import plotly.graph_objs as go

# Inicializar o dash
app = dash.Dash()

# Criar o gráfico, porém dividindo em duas etapas
app.layout = html.Div([
    html.H1("Gráfico interativo com dash e plotly"),
    dcc.Graph(
        id = 'grafico-1',
        figure = {
            'data':[
                go.Scatter(
                    x=[1,2,3,4,5],
                    y=[10,11,12,13,14],
                    mode='lines+markers',
                    name='Linha 1'
                )
            ],
            'layout': go.Layout(
                title = 'Gráfico de linha interativo',
                xaxis = {'title': 'Eixo X'},
                yaxis = {'title': 'Eixo Y'}
            )
        }
    )
])

# Rodamos o servidor
if __name__ == '__main__':
    app.run(debug=True)