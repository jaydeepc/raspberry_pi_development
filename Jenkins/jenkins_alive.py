import jenkinsapi
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080')

for job in J.jobs:
    print job