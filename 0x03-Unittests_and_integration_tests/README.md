# 0x03. Unittests and Integration Tests

This project contains integration tests for the `GithubOrgClient` class. The integration tests verify the behavior of the `public_repos` method of the `GithubOrgClient` class under different scenarios using fixtures.

## Requirements

- Python 3.x
- `unittest` module
- `requests` library (for mocking HTTP requests)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/DeeGemini/alx-backend-python/0x03-Unittests_and_integration_tests

## Navigate to the project directory:
>> cd github-org-client-integration-tests

## Running Tests
>> To run the integration tests, execute the following command from the project directory:
python -m unittest test_integration.py

## Fixtures
The project includes fixtures that contain example payloads for testing purposes. These fixtures are used by the integration tests to simulate responses from the GitHub API.

org_payload: Payload representing organization information.
repos_payload: Payload representing repository information.
expected_repos: Expected list of public repositories.
apache2_repos: Expected list of repositories with the Apache 2.0 license.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
>> Nontuthtuzelo Ngwenya - DeeGemini
For any questions or feedback, please contact DeeGemini.

