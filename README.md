<h1>Clone Project</h1>
<p>git clone https://github.com/essamabuissa/LiwwaTask-Backend.git</p>

<h2>Important Message</h2>
<h4>You will see all the Views,Models,Schemas in app.py file , i had problem in structuring them and keep giving me (Circular import error) so i put them all in the app.py file , but you will find file for each one with a commented code inside to show you that i know how the structure goes but sadly it didnt work with me and i put them all in one file </h4>

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
    <li>I have uploaded a db.sqlite file with the repo so when you open it you will have data. </li>
</ol>

<h2>Start Project</h2>
<p>flask run</p>

<h2>Test Endpoints</h2>

<h3>Create New User</h3>
<p>Method : POST</p>
<p>http://localhost:5000/users</p>
<p>When creating a new user it checks if had the header:X-ADMIN=1, if it had it it gives it a prop called role with the value "admin" , and if not it gives value "candidate".</p>
<p>I made so i can use it in the response in the frontend and control whatever i want there.</p>

<h3>Get All Users</h3>
<p>Method : GET</p>
<p>http://localhost:5000/users</p>

<h3>Get Single Users</h3>
<p>Method : GET</p>
<p>http://localhost:5000/users/:userId </p>
