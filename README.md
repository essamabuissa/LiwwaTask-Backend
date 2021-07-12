<h1>Clone Project</h1>
<p>git clone https://github.com/essamabuissa/LiwwaTask-Backend.git</p>

<h2>Activate Virtual Enviroment</h2>
<p>pipenv shell</p>

<h2>Install Dependencies</h2>
<p>pip install -r requirements.txt</p>

<h2>Install Table Plus</h2>
<p>https://tableplus.com/</p>
<h3>Connect it to the database</h3>
<ol>
    <li>Open table plus</li>
    <li>Create new connection</li>
    <li>Add name for connection</li>
    <li>Add Path for connection , is the path to the repo/db.sqlite , example (/Users/essamabuissa/Desktop/Development/Python/hr-backend/db.sqlite)</li>
</ol>

<h2>Start Project</h2>
<p>flask run</p>

<h2>Test Endpoints</h2>

<h3>Create New User</h3>
<p>Method : POST</p>
<p>http://localhost:5000/users</p>

<h3>Get All Users</h3>
<p>Method : GET</p>
<p>http://localhost:5000/users</p>

<h3>Get Single Users</h3>
<p>Method : GET</p>
<p>http://localhost:5000/users/:userId </p>
