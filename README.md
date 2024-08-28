### User Guide: Test Branch Automated Testing Workflow

#### Table of Contents
1. [Overview](#overview)
2. [Branch Structure](#branch-structure)
3. [Automated Testing Workflow](#automated-testing-workflow)
4. [Usage Steps](#usage-steps)
   - [1. Setting Up the Workflow](#1-setting-up-the-workflow)
   - [2. Writing and Managing Test Cases](#2-writing-and-managing-test-cases)
   - [3. Pushing Code and Triggering Tests](#3-pushing-code-and-triggering-tests)
   - [4. Viewing Test Results](#4-viewing-test-results)
5. [Workflow Configuration File Explanation](#workflow-configuration-file-explanation)
6. [Possible Questions](#possible-questions )

---

### Overview
The `Test` branch is designed to manage the automated testing workflow for the `Data-Loading-Module` branch. This user guide provides detailed instructions on how to use the automated testing features within the `Test` branch, ensuring that every code change in the `Data-Loading-Module` branch is automatically tested and reports are generated.

### Branch Structure

```plaintext
Test branch/
├── .github/
│   └── workflows/
│       └── ci-data-loading.yml  # GitHub Actions workflow configuration file
|       └── other.yml
├── tests/
│   ├── data_loading/
│   │   ├── test_data_loading.py  # Test script file
│   │   └── requirements.txt      # Test dependencies
|   ├── other/
|   |   ├── test_other.py 
│   │   └── requirements.txt  
└── README.md                     # User guide (this document)
```

### Automated Testing Workflow

The workflow in the `Test` branch is implemented through GitHub Actions and is designed to run automatically when changes are made to the `Data-Loading-Module` branch. This workflow performs the following key tasks:

1. Check out the test scripts and dependencies from the `Test` branch.
2. Check out the code from the `Data-Loading-Module` branch into a specified directory in the virtual machine.
3. Set up the Python environment and install dependencies.
4. Run the test scripts and generate test reports.

### Usage Steps

#### 1. Setting Up the Workflow

Ensure that the `.github/workflows/ci-data-loading.yml` file is correctly configured and located in the `Test` branch.

#### 2. Writing and Managing Test Cases

Write and manage your test cases in the `tests/data_loading/` directory within the `Test` branch. Make sure the test files follow the naming conventions of `pytest` or `unittest` (e.g., filenames starting with `test_`) so that the workflow can automatically detect and run these tests.

**Example Test File: `test_data_loading.py`**

```python
import sys
import unittest

sys.path.insert(0, './code/Code/Sprint2/Loading_Module')

from data_loading_module import load_gtfs_data

class TestDataLoadingModule(unittest.TestCase):
    def test_load_gtfs_data_valid(self):
        result = load_gtfs_data('tests/test_data/gtfs_data.zip')
        self.assertIsInstance(result, dict)
        self.assertIn('routes', result)

    def test_load_gtfs_data_invalid(self):
        with self.assertRaises(Exception):
            load_gtfs_data('tests/test_data/invalid_gtfs.zip')

if __name__ == '__main__':
    unittest.main()
```
#### Notice:
```python
sys.path.insert(0, './code/Code/Sprint2/Loading_Module')
```
-  [x]  **`/Code/Sprint2/Loading_Module` The path location of the file to be tested in the branch, modify according to theactual file**
- [x] **modify according to the actual file**
```python
from data_loading_module import load_gtfs_data
```
- [x] **Import the `load_gtfs_data` function in the `data_loading_module.py` file into the current test script, The `data_loading_module.py` file must be located in the `./code/Code/Sprint2/Loading_Module` directory**
- [x] **modify according to the actual file**

#### 3. Pushing Code and Triggering Tests

Each time you push code to the `Data-Loading-Module` branch or create a pull request (PR), the workflow will automatically trigger and run in GitHub Actions.

#### 4. Viewing Test Results

Navigate to your GitHub repository and click on the "Actions" tab. Here you can view the status of each workflow run and the results of the tests. By clicking on a specific workflow run, you can see detailed logs and the test report.

### Workflow Configuration File Explanation

**`ci-data-loading.yml` File Content**

```yaml
name: Data Loading Module CI

on:
  push:
    branches:
      - Data-Loading-Module
  pull_request:
    branches:
      - Data-Loading-Module
    
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Test branch for tests and dependencies
      uses: actions/checkout@v3
      with:
        ref: Test

    - name: Checkout Data-Loading-Module branch for code
      uses: actions/checkout@v3
      with:
        ref: Data-Loading-Module
        path: ./code

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r tests/data_loading/requirements.txt

    - name: Run Data-Loading-Module tests
      run: |
        pytest tests/data_loading/
    # The test scripts in the directory will be run (can be modified here)
```

### Possible Questions 

**1. Why isn't the workflow automatically triggered?**
   - Ensure that the `.yml` file is correctly placed in the `.github/workflows/` directory of the `Test` branch.
   - Check if the `.yml` file's trigger conditions are correctly configured to monitor the `Data-Loading-Module` branch for pushes and PRs.

**2. How can I view detailed test reports?**
   - Go to the "Actions" tab in your repository, find the relevant workflow run, and click on it to view detailed logs and the test report.

**3. Can I add new test cases?**
   - Yes, you can add new test case files in the `tests/data_loading/` directory of the `Test` branch and push them to the branch.
   - If you need to test other branches, create a new `.yml` and folder in `tests` according to the above format

**4. What should I do if a test fails?**
   - Review the logs in GitHub Actions to identify the cause of the failure, then make the necessary fixes in the `Data-Loading-Module` branch.

