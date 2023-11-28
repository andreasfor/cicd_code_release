# cicd_code_resease
Demonstrating how to use GitHub Actions to run tests and push a code release (a tag) from the dev branch to the test branch

- Create the two brances.
- Create a a workflow in Actions that triggers manually on dispatch and on pull requests.
- The workflow should basically only run automatic tests.
- When you want to create a version of your code, create a code release, which will be associated with a tag.
- Do a pull request to move code from the development branch to the test branch, and the code release will follow. The test will be triggered automatically.

In your IDE:
- Clone the repo
- Switch to test branch
- run "git checkout tags/<<tag>> -b <<branch>>" to create a new branch based on the code release tag
