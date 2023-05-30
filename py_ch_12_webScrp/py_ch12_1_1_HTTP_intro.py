
# Courses: colt_py_bootcamps    224, 225

# -----------    HTTP-intro    -----------

# How we work with internet using python
    # How we get data (in JSON) from API


# HTTP and Internet basics (already covered in web dev)
# Hypertext Transfer Protocol : HTTP



# -----------    request/response cycle    -----------
# 1. Describe what happens when you type a URL in the URL bar 
    # Describe the request/response cycle
        # 1.	DNS Lookup (lookup perticular IP address)
                    # It is a kind of "PhoneBook" for the iternet containing series of IP-Address
                    # Takes a DOMIN NAME "google.com" and turns into an IP address "172.217.9.142"
                    # IP-address are UNIQUE

        # 2.	Computer makes a REQUEST to a SERVER
                    # To send data computer makes POST request
                    # To get data (search in browser) computer makes GET request
                        # HTTP code 200 (ok) sends the data with "this kind of status code"
                        # Server sends HTML files
            # CHROME developer Network - tab

        # 3.	Server processes the REQUEST
        # 4.	Server issues a RESPONSE

        # "2, 3, 4" are called the "request/response cycle"



# -----------    request/response Header    -----------
# 2. Explain what a request or response header is, and give example
    # -----------    HTTP Headers    -----------
        # It's a METADATA
        # URL is the most important hing here
        # Sent with both requests and responses 
        # Provide 'additional information' about the "request" or "response"

    # -----------    Header Examples    -----------
        # Request Headers
            # Accept - Acceptable content-types for response (e.g. html, json, xml)
            # Cache-Control - Specify caching behavior 
            # User-Agent - 'Information' about the "software" used to make the request
    
        # Response Headers
            # Access-Control-Allow-Origin - specify domains that can make requests
            # Allowed - HTTP verbs that are allowed in requests



# -----------    status codes    -----------
# 3. Explain the different categories of response codes 
    # Response Status Codes
        # •	2xx - Success
        # •	3xx - Redirect
        # •	4xx - Client Error (your fault!)
        # •	5xx - Server Error (not your fault!)



# 4. Compare GET and POST requests
    # GET: Search
    # POST: Posting information to server. Using "HTML-Form"
    
    
