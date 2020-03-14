

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'lightgreen',
    'text': 'purple'

}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dash with love',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-family': "Times New Roman"
        }
    ),

    html.H3(
        children='Меня зовут Александра, это мой новый учебный сайтик',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'text-decoration': 'overline',
            'font-family': "Helvetica"
        }
    ),

    html.Div(children='Потом добавлю "о себе"', style={
        'textAlign': 'center',
        'color': colors['text'],
        'font-family': "Helvetica",
        'border': '1px solid blue',
        'margin-top': '30px',
        'margin-bottom': '30px',
        'margin-right': '500px',
        'margin-left': '500px',
        'background-color': 'lightgreen'
    }),

    html.Div(children='А пока вот фоточка:)', style={
        'textAlign': 'center',
        'color': 'purple',
        'font-family': "Helvetica"
    }),

    html.A(html.Button('Ссылочка на сайт ВШЭ', id='button'), href= 'https://www.hse.ru', style={
        'margin-top': '30px',
        'margin-bottom': '30px',
        'margin-right': '500px',
        'margin-left': '150px'
        
                                                                                
    }),

  

    html.Div([
        html.Img(src='https://sun9-44.userapi.com/c857628/v857628649/9660f/k6oBj8RJ1VQ.jpg', style={
        'width':'75%', 'margin-left':150, 'margin-top':30, 'textAlign': 'center'
    }),

    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)
