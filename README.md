# cicd_code_resease
This repo serves as a demonstrattion of: 
Demo 1, How to use GitHub Actions to run tests and push a code release (a tag) from the dev branch to the test branch.
Demo 2, How to set PYTHONPATH correctly for VS Code in order to beeing able to call a python package from another package

## Demo 1
- Create the two brances.
- Set a branch protection rule to not allow direct pushes to test branch by going to Settings --> Branches --> Require a pull request before merging. 
- Create a a workflow in Actions that triggers manually on dispatch and on pull requests.
- The workflow should basically only run automatic tests.
- When you want to create a version of your code, create a code release, which will be associated with a tag.
- Do a pull request to move code from the development branch to the test branch, and the code release will follow. The test will be triggered automatically.

In your IDE:
- Clone the repo
- Create a virtual environment with opening the terminal and write: python -m venv .venv
- Activate virtual environment: source .venv/Scripts/activate

- Switch to test branch
- run "git checkout tags/(tag_version) -b (new_branch_name)" to create a new branch based on the code release tag

## Demo 2,

Ensure that your project is situated within a folder such such as the C drive, as opposed to locations like the Documents folder, as the latter may introduce complications to the file path. 

### Step 1,
Check your workspace location:
- run check_python_path.py then take the output

### Step 2,
VS Code setting:
- Set PYTHONPATH in File -> Preferences -> Settings -> Then go to the top right corner, third logo from right, open the JSON settings and paste the location of your src file e.g. "terminal.integrated.env.windows": {  "PYTHONPATH": "c:/Users/anforsbe/Visual Studio Code/SCMBI/cicd_code_resease". 
- Note that you could add multiple locations after each other  "Users/anforsbe/Visual Studio Code/SCMBI/cicd_code_resease:/Users/anforsbe/Visual Studio Code/SCMBI/cicd_code_resease/tests"

### Step 3,
Validate your PYHTONPATH
- Open validate_python_path.py
- Paste your path in the variable src_path_str
- Run file
- If the Dir exists and all characters is a match then your PYTHONPATH is set appropriately
