# SSRF Detection Tool

## Overview
This Python script is a basic Server-Side Request Forgery (SSRF) detection tool. It tests a specified endpoint in a web application to see if it is vulnerable to SSRF attacks by attempting to make requests to various internal and external resources.

## Disclaimer
**Important:** This tool is intended for educational purposes and authorized testing only. Do not use this script against any application without explicit permission from the owner. Unauthorized testing may be illegal and unethical.

## Prerequisites
- Python 3.x
- `requests` library
  - You can install it using pip:
    ```bash
    pip install requests
    ```

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using Python:
    ```bash
    python ssrf.py
    ```
5. When prompted, enter the target URL that you want to test (e.g., `http://example.com/vulnerable-endpoint`).
6. The script will send requests using predefined SSRF payloads and output the results, including response status codes and snippets from the responses.

## Understanding the Output
The script will return:
- **Payload**: The URL payload that was tested.
- **Status Code**: The HTTP status code returned by the server for that request.
- **Response**: A snippet of the response body (first 100 characters) to help determine if any sensitive information was leaked or a SSRF vulnerability was present.

## Customization
You can modify the list of SSRF payloads found in the `ssrf_payloads` variable in the script to include additional URLs that you want to test against. This can allow for targeted testing based on the application's expected behavior.

## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. You can also report issues or suggestions on the GitHub project page.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
