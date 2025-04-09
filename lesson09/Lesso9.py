# x and y given as array_like objects

import plotly.express as px

fig = px.line(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

fig.show()
# load built-in gapminder dataset from plotly

# gapminder = px.data.gapminder()

# df = px.data.gapminder().query("continent == 'Asia'")

# fig2 = px.line(df, x='year', y='lifeExp', color='country')

# fig2.show()