import matplotlib.pyplot as plt
import matplotlib
from urllib.parse import quote

matplotlib.rcParams['mathtext.fontset'] = 'cm'

latex_expression = r"$f(x) = \frac{x}{y} \sin (\omega t)$"

url_expression = quote(latex_expression)
print("URL-encoded LaTeX expression:", url_expression)

fig = plt.figure(figsize=(3, 0.5))  # Dimensions of figsize are in inches
text = fig.text(
    x=0.5,  # x-coordinate to place the text
    y=0.5,  # y-coordinate to place the text
    s=latex_expression,
    horizontalalignment="center",
    verticalalignment="center",
    fontsize=16,
)

plt.savefig("function.svg")