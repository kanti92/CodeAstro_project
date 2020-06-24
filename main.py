import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class general_plots:
    def __init__(self, nb_rows_col):
        self.nb_rows = nb_rows_col[0]
        self.nb_col = nb_rows_col[1]
        self.nb_plot = self.nb_rows * self.nb_col
        #self.fig_name = "Plot"

    def line(self, data, col_list, fig_name="Plot"):

        
       if type(data).__module__ == 'pandas.core.frame':
            if all(isinstance(item, int) for item in data) == True:
                x = data[col_list[0]]
                y = data[col_list[1]]
            elif all(isinstance(item, str) for item in data) == True:
                x = data[col_list[0]]
                y = data[col_list[1]]
            else:
                print('there is something wrong')

        if type(data).__module__ == 'numpy':
            if all(isinstance(item, int) for item in data) == True:
                x = data[col_list[0]]
                y = data[col_list[1]]
            elif all(isinstance(item, str) for item in data) == True:
                x = data[col_list[0]]
                y = data[col_list[1]]
            else:
                print('there is something wrong')
        
        
        print('hello')

        fig, ax = plt.subplots(self.nb_rows, self.nb_col, figsize=(7,7))

        ax.set(xlim=(0, 10), ylim=(-2, 2), xlabel='x', ylabel='y(x)',title=fig_name)
        ax.plot(x, y, c='red', linestyle='-', alpha = 0.8, label='sin', linewidth=2)
        #ax.plot(x, y2, c='blue', linestyle='dashed', alpha = 0.4, label='cos', linewidth=1)
        # ax.plot(x,y3, c='purple', linestyle='-.', alpha = 0.4, label='cos', linewidth=1)
        ax.grid(linestyle=':', linewidth =1, alpha=0.5)
        ax.hlines(y = 1, xmin = 0, xmax = 4, color='green', linestyle=':', linewidth =3) 
        ax.vlines(x = 1, ymin = 0, ymax = 4, color='pink', linestyle='--', linewidth =3) 
        ax.tick_params(axis="x", labelsize=13)
        ax.tick_params(axis="y", labelsize=13)
        ax.set_xlabel('X', fontsize=18)
        ax.set_ylabel('Y', fontsize=18)
        ax.legend(loc=4, ncol=1, framealpha=0.7, title='legend', markerscale=0.3)
        plt.show()

        return 0

    def load_data(self):
        
        return 0

    def dataframe(self, data_dict):
        #nb_col = len(data.values())
        col_name_list = data_dict.keys() 
        df = pd.DataFrame(data=data_dict, columns=col_name_list)
        
        return df

    def save_fig(self):
        print("save")
        return 


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
    general_plots()