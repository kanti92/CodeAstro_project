import sys
import numpy as np
import pandas as pd
from package.plotting_class import general_plots 

if __name__ == "__main__":

    x  = np.linspace(0, 10, 1000)
    y1 = np.cos(x)
    y2 = np.tan(x)
    y3 = np.sin(x)

    data = list([x, y1, y2, y3])
    data0 = np.transpose(data)
    data1 = pd.DataFrame(data0, columns=['x', 'cos', 'tan', 'sin'])
    data2 = ((9,7,5), (8,6,5), (3,1,2), (33,4,55), (4,5,6))
    data3 = [(9,7,5), (8,6,5), (3,1,2), (33,4,55), (4,5,6)]

    nb_rows_col = (1,1)
    c = general_plots(nb_rows_col)
    #c.line(data1,['sin','tan'], fig_name='test')
    c.line(data0,[1,2], fig_name='test')