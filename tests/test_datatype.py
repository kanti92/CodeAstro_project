from package.plotting import general_plots 
import numpy as np
import pandas as pd
import pytest

@pytest.fixture
def data_init():
    """
    Initialize the data for the different methods
    """
    x  = np.linspace(0, 10, 1000)
    y1 = np.cos(x)
    y2 = np.tan(x)
    y3 = np.sin(x)
    data_list = [x, y1, y2, y3]
    data = np.transpose(data_list)

    return data

def test_array(data_init):
    """
    Test that the method general_plots.line() reads the data as arrays
    """
    # Define the data as an array:
    data = data_init
    # Create the object:
    ob = general_plots((1,1), display=False)
    # Call the method:
    ob.line(data,[0,1])

def test_list(data_init):
    """
    Test that the method general_plots.line() reads the data as lists
    """
    # Create the object:
    ob = general_plots((1,1), display=False)
    # Call the method:
    ob.line(data_init,[0,1])

def test_dataframe(data_init):
    """
    Test that the method general_plots.line() reads the data as a dataframe
    """
    # Define the data as a dataframe:
    data = pd.DataFrame(data_init, columns=['x', 'cos', 'tan', 'sin'])
    # Create the object:
    ob = general_plots((1,1), display=False)
    # Call the method:
    ob.line(data,['x','sin'])

def test_tuple():
    """
    Test that the method general_plots.line() reads the data as tuples
    """
    # Define the data as a tuple of tuples:
    data = ((9,7,5), (8,6,5), (3,1,2), (33,4,55), (4,5,6))
    # Create the object:
    ob = general_plots((1,1), display=False)
    # Call the method:
    #try:
    ob.line(data,[1,2])
    #except:
        #print("general_plots.line() cannot read data as tuples")

if __name__ == "__main__":    
    test_array()
    test_list()
    test_dataframe()
    test_tuple()