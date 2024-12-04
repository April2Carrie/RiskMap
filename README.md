# RiskMap
Code for Risk Map Developing Website App. Created for the RMI 700 course at WSB.

This web application allows users to create a risk map by entering risk categories and their associated frequency and severity ranges. Users can dynamically add data, view it in a table, and generate a visualized risk map.

## Before using this project, ensure that you have the following installed on your computer:

1. **Python 3.7** or higher
  - Download Python from the official Python website.
  - Make sure to check the box to add Python to your system's PATH during installation.
  - Pip (Python package manager)

2. **Pip** is included with Python. You can verify its installation by running:
  - bash
  - Copy code
  - pip --version

3. **Git** (optional, if cloning the repository)
  - Download Git from the official Git website.

4. **Web Browser**
  - Any modern web browser (e.g., Google Chrome, Firefox, Edge) to access the web application.

## Steps for Use:
Follow these steps to set up and run the application:

1. Clone or Download the Repository
  - Option 1: Clone the repository using Git:
    git clone https://github.com/your-username/risk-map-generator.git
  - Option 2: Download the repository as a ZIP file from GitHub and extract it to your desired location.
2. Navigate to the Project Directory
  - Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS/Linux) and navigate to the directory where the project is located. For example:
    cd path/to/risk-map-generator
3. Install Required Python Libraries
  - Install the dependencies listed in the requirements.txt file by running:
    pip install -r requirements.txt
  - This will install the following:
    Flask: To run the web application
    pandas: For data handling
    matplotlib: For graph plotting
    numpy: For numerical operations
4. Run the Flask Application
  - Start the web application by running:
    python app.py
  - If the command is successful, you will see output similar to this:
    csharp
   * Running on http://127.0.0.1:5000

## Access the Web Application:

1. Open your web browser and go to: http://127.0.0.1:5000
2. Enter the following fields:
   - Risk Category: Name or description of the risk (e.g., "Cyber Risk").
   - Freq_lb: Lower bound of the frequency range.
   - Freq_ub: Upper bound of the frequency range.
   - Sev_lb: Lower bound of the severity range.
   - Sev_ub: Upper bound of the severity range.
3. Click the "Add Line" button to save the entry.
4. The entered data will appear in a table below the input form.
5. Click the "Generate Graph" button to visualize the risk map. The map will display a grid with your data points and ranges plotted.
6. Add more rows or refresh the page to restart.

## Additional Notes
- Static Folder: The risk map image is saved as plot.png in the static folder.
- Browser Refresh: Refreshing the page will reset the entered data.
- Custom Ports: If port 5000 is unavailable, modify the app.run() line in app.py to use another port, e.g.: app.run(debug=True, port=5001)
