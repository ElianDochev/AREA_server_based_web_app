⭐AreaCraft
AreaCraft is a web and mobile application that allows users to create and share custom maps of their favorite areas. Users can add markers to the map to indicate points of interest, and can also add comments and photos to each marker.

⭐Getting Started
To get started with AreaCraft, follow these steps:

1. Clone the repository to your local machine.
2. Install the dependencies for the server, web, and mobile components by running npm install in the server, web, and mobile directories.
3. Start the server by running python3 main.py in the server directory.
4. Start the web component by running npm run serve in the web directory.
5. Start the mobile component by running npm expo start --tunnel in the mobile directory.

You should now be able to access the web component at http://localhost:8080 and the mobile component using the Expo app on your mobile device.
Swagger documentation https://app.swaggerhub.com/apis-docs/VASILIYNOVIKOV/AREA/1.0

⭐Commands
To run the server run docker compose up --build at the /server of the repository

## FYI:
### The following .env is reqired in /server
```
SERVER_SECRET_KEY=08e0626e1fae5b9c5c247edb605a385df961754f6c780007911a72a2a979f48b // can be anything
DATABASE_URI=sqlite:///../Area.db
VIRSION=1.0
PORT=8080
SERVER_URL=http://51.20.135.59:${PORT} // Public IP address (WEBHOOKS)
API_TRELLO = API_KEY
API_SECRET = API_SECRET
ADMIN_PASSWORD =  'adminRootDataCore' // the admin user
ADMIN_USERNAME = 'admin'
CHATGPT_API_KEY = API_KEY
CALLR_LOGIN = CALLR_CREDENTIALS
CALLR_PASSWORD = CALLR_CREDENTIALS
GITHUB_CLIENT_ID = API_ID
GITHUB_CLIENT_SECRET = API_SECRET
API_NASA = API_KEY
```

⭐Acknowledgements
AreaCraft was created by the following team:
Eliyan, Vlad, Charles, Vasiliy and Luc
