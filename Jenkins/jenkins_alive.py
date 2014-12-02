import jenkinsapi
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080')

J.build_job("test_job")