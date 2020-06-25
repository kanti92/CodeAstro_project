from package.plotting import general_plots 

def test_tuple():
    """
    Test that the method general_plots.line() reads tuples
    """
    # Define the data as a tuple of tuples:
    data = ((9,7,5), (8,6,5), (3,1,2), (33,4,55), (4,5,6))

    # Create the object:
    ob = general_plots((1,1), display=False, save_path="./test_fig.png")

    # Call the method:
    #try:
    ob.line(data,[1,2])
    #except:
        #print("general_plots.line() cannot read data as tuples")

if __name__ == "__main__":
    test_tuple()