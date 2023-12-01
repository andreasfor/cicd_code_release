# cicd_code_resease
Demonstrating how to use GitHub Actions to run tests and push a code release (a tag) from the dev branch to the test branch

- Create the two brances.
- Set a branch protection rule to not allow direct pushes to test branch by going to Settings --> Branches --> Require a pull request before merging. 
- Create a a workflow in Actions that triggers manually on dispatch and on pull requests.
- The workflow should basically only run automatic tests.
- When you want to create a version of your code, create a code release, which will be associated with a tag.
- Do a pull request to move code from the development branch to the test branch, and the code release will follow. The test will be triggered automatically.

In your IDE:
- Clone the repo
- Switch to test branch
- run "git checkout tags/(tag_version) -b (new_branch_name)" to create a new branch based on the code release tag


VS Code setting:
- Set PYTHONPATH in File -> Preferences -> Settings -> Then go to the top right corner, third logo from right, open the JSON settings and paste the location of your src file e.g. "terminal.integrated.env.windows": {  "PYTHONPATH": "C:/Users/anforsbe/OneDrive - Capgemini/Documents/Visual Studio Code/test_cicd/cicd_code_resease/src". 
- Note that you could add multiple locations after each other  "C:/Users/anforsbe/OneDrive - Capgemini/Documents/Visual Studio Code/test_cicd/cicd_code_resease/src:  "C:/Users/anforsbe/OneDrive - Capgemini/Documents/Visual Studio Code/test_cicd/cicd_code_resease/tests"
