\# Health Facilities Locator

This project is a backend application written in Django with PostGIS, designed to manage health facilities' locations and provide recommendations for the nearest health facility based on the user's location.

\## Table of Contents

\- \[Features\](#features)

\- \[Requirements\](#requirements)

\- \[Installation\](#installation)

\- \[Usage\](#usage)

\- \[API Endpoints\](#api-endpoints)

\- \[Contributing\](#contributing)

\- \[License\](#license)

\## Features

\- \*\*Manage Health Facilities\*\*: Add, update, and delete health facilities' information.

\- \*\*Geolocation\*\*: Store and manage geographical data using PostGIS.

\- \*\*Proximity Algorithm\*\*: An algorithm that recommends the nearest health facility based on the user's location.

\## Requirements

\- Docker

\- Docker Compose

\## Installation

1\. \*\*Clone the repository\*\*

\`\`\`bash

git clone https://github.com/yourusername/health-facilities-locator.git

cd health-facilities-locator

\`\`\`

2\. \*\*Set up environment variables\*\*

Create a \`.env\` file in the root directory and configure the necessary environment variables:

\`\`\`plaintext

POSTGRES\_DB=your\_db\_name

POSTGRES\_USER=your\_db\_user

POSTGRES\_PASSWORD=your\_db\_password

POSTGRES\_HOST=db

POSTGRES\_PORT=5432

\`\`\`

3\. \*\*Start the services\*\*

\`\`\`bash

docker-compose up --build

\`\`\`

This command will build and start the Docker containers for the Django application and PostgreSQL database with PostGIS.

4\. \*\*Apply migrations\*\*

\`\`\`bash

docker-compose exec web python manage.py migrate

\`\`\`

5\. \*\*Create a superuser\*\*

\`\`\`bash

docker-compose exec web python manage.py createsuperuser

\`\`\`

\## Usage

\### Adding Health Facilities

1\. \*\*Log in to the admin panel\*\*

Open your browser and go to \`http://localhost:8000/admin\`. Log in with the superuser credentials you created earlier.

2\. \*\*Add health facilities\*\*

Use the admin interface to add health facilities with their respective location data.

\### Getting the Nearest Health Facility

1\. \*\*API Endpoint\*\*

You can use the \`/api/nearest-facility/\` endpoint to get the nearest health facility. This endpoint requires the user's latitude and longitude as query parameters.

Example request:

\`\`\`http

GET /api/nearest-facility/?latitude=40.7128&longitude=-74.0060

\`\`\`

Example response:

\`\`\`json

{

"facility\_name": "Health Facility 1",

"address": "123 Main St, New York, NY",

"distance": "0.5 miles"

}

\`\`\`

\## API Endpoints

\- \*\*List Health Facilities\*\*

\`\`\`http

GET /api/facilities/

\`\`\`

\- \*\*Retrieve Health Facility Details\*\*

\`\`\`http

GET /api/facilities/{id}/

\`\`\`

\- \*\*Get Nearest Health Facility\*\*

\`\`\`http

GET