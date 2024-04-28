![github-header-image](https://github.com/tech-with-upeh/Thor/assets/67229614/884a562d-9303-4ca6-892e-2611729344d5)

<h1>Welcome to the Thor Web Server repository!</h1>
<p>This project aims to create a simple web server using Python's socket library.</p>

<p>You can follow the progress on youtube using the link : www.youtube.com/@techwithupeh</p>

<h1>Features</h1>
<ul>
  <li>Serve web content (HTML, CSS, JavaScript, images, etc.).</li>
  <li> Handle HTTP requests.</li>
  <li>Support for basic HTTP response codes (200 OK, 404 Not Found, etc.).</li> 
  <li>Simple configuration and customization.</li> 
  <li>Dynamic url Routing </li>
  <li> Fast Rendering </li>
  <li> added security </li>
  <li>etc..</li>
</ul>

<h1>Getting Started</h1>  
<p>Follow these steps to get started with the Thor Web Server: </p>

<h1> Prerequisites </h1>
<ul>
  <li>Python 3</li>
</ul>
<h1>Installation </h1>
<ul>
  <li> 1.  Clone The Repository </li>

```
git clone https://github.com/tech-with-upeh/Thor

```
  <li>2. Navigate to directory </li>
```
cd Thor

```
</ul>

<h1> Usage </h1>
<p> import Thor file </p>
<p> Thor will soon be availaple as a pip package</p>
<p>initialize the server with ip, port and path </p>
<p>Define Routes and run the server </p>

```
from thor import Thor

ip = '0.0.0.0'
port = 80
path = '/htdocs'
server = Thor(ip, port, path)

@server.route('/')
def home():
  return 'Thor server is live'

server.run()
```
