import sys
import numpy as np
import pandas as pd
from package.plotting_class import general_plots 

def main():
    x  = np.linspace(0, 10, 1000)
    y1 = np.cos(x)
    y2 = np.tan(x)
    y3 = np.sin(x)

    data = list([x, y1, y2, y3])
    data = np.transpose(data)
    dd = pd.DataFrame(data, columns=['x', 'cos', 'tan', 'sin'])

    nb_rows_col = (1,1)
    c = general_plots(nb_rows_col)
    c.line(dd,['sin','tan'], fig_name='test')

if __name__ == "__main__":
    main()
