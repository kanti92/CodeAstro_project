from package.plotting import general_plots 
import os

def test_saving():
    """
    Test that the method general_plots._savefig() saves the figure
    """
    # Define the data as a tuple of tuples:
    data = ((9,7,5), (8,6,5), (3,1,2), (33,4,55), (4,5,6))

    # Define the file path and name:
    file_path = "./test_fig.png"

    # Delete the file if it already exists:
    if os.path.isfile(file_path):
        os.remove(file_path)

    # Create the object:
    ob = general_plots((1,1), display=False, save_path=file_path)

    # Call the method:
    ob.line(data,[1,2])

    # Check that the file exists:
    assert os.path.isfile(file_path)

if __name__ == "__main__":
    test_saving()