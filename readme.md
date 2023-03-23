# DNS-to-DNS-over-TLS Proxy

This program is a DNS-to-DNS-over-TLS proxy written in Python. It listens on port 12853 for DNS queries from clients, and forwards the queries to a DNS-over-TLS server over TCP. The server's response is then sent back to the client.

## Requirements
- Python 3.6 or higher
- socket and ssl modules (should be installed by default with Python)
- Docker

## Installation

- Create docker image by using Dockerfile which is in the root directory by run this command:
    `docker build -t dns-over-tls .`
- Create docker network by using this command:
    `docker network create --subnet 172.168.1.0/24 myNetwork`
- Run the container by using that docker image we created in the previous step by run this command:
    `docker run -p 12853:12853/tcp --net myNetwork -it dns-over-tls`
- You can test this by making nslookup or dig request
    `dig @127.0.0.1 -p 12853 +tcp google.com`

## Security Concerns

If this proxy were deployed in a production infrastructure, there would be several security concerns to address. Some potential issues include:

- Encryption: While this proxy uses DNS-over-TLS to encrypt DNS queries and responses, it's possible for an attacker to perform a man-in-the-middle attack to intercept and decrypt the traffic. To prevent this, the DNS-over-TLS server should be authenticated using a trusted certificate.

- Authentication: The current implementation of this proxy does not perform any authentication of client requests. This could allow an attacker to use the proxy to perform DNS queries on their behalf, potentially leading to information disclosure or other security issues. To mitigate this, the proxy could be configured to only allow requests from trusted IP addresses or require some form of authentication (such as a username and password).

- Denial of Service: The proxy does not implement any rate limiting or other measures to prevent malicious clients from overwhelming the server with requests. This could lead to a denial of service attack, where legitimate clients are unable to access the DNS service. To prevent this, the proxy could implement rate limiting or other measures to limit the number of requests per client.

## Integration in a Microservices Architecture
To integrate this solution into a distributed, microservices-oriented and containerized architecture, several approaches could be taken:

- Service Discovery: To enable other microservices to discover and use the proxy, a service discovery mechanism such as Consul or Kubernetes could be used. This would allow microservices to dynamically discover the IP address and port of the proxy without having to hardcode it.

- Load Balancing: To handle high volumes of DNS traffic, a load balancer such as HAProxy or NGINX could be used to distribute the traffic across multiple instances of the proxy.

## Possible Improvements
Some potential improvements that could be made to this project include:

- Caching: The proxy could implement caching of DNS responses to reduce the number of requests to the DNS-over-TLS server and improve performance.
- Logging: The proxy could log requests and responses to aid in debugging and monitoring.
Metrics: The proxy could expose metrics such as the number of requests and response times for monitoring and performance analysis.
- Configuration: The proxy could be configured using a configuration file or environment variables to make it easier to customize and deploy.
- Security: As mentioned earlier, several security improvements could be made to the proxy, such as implementing authentication and rate limiting.
- IPv6 Support: The current implementation only supports IPv4. IPv6 support could be added to make the proxy more compatible with modern networks.

Overall, the DNS-to-DNS-over-TLS proxy is a simple but useful tool that can improve the security and privacy of DNS traffic. With some additional features and security improvements, it could be a valuable addition to any network architecture.

## Test
- Test 1 <br>
![test1](https://user-images.githubusercontent.com/22475831/227200438-9fdc7d96-3ae1-4b5f-b0d2-9051f4c255c8.PNG)

- Test 2 <br>
![test2](https://user-images.githubusercontent.com/22475831/227200516-bbf28b6b-7cff-4f87-bec8-2ac9d855ef39.PNG)

- Test 3 <br>
![test3](https://user-images.githubusercontent.com/22475831/227200577-b3b6ff23-2fac-4008-93c9-4ca8d94c47de.PNG)
