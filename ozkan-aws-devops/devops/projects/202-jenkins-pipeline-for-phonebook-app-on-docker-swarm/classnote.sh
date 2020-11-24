Project-202: Jenkins Pipeline for Dockerized Phonebook Application (Python Flask & MySQL) Deployed on Docker Swarm

- Infrastructure
    - Public repository on Github 
    - Docker swarm as orchestrator
        - 3 manegers
        - 2 workers
    - Image repository (AWS ECR)
    - Should be able to
        - Every EC2 is abe to talk eache other (EC2 Connect CLI, IAM policy)
        - Grand master can pull and push image to AWS ECR
        - MAnagers and workers can pull image from AWS ECR

- Application Deployment
    - Dockerfile
    - docker-compose.yml (Web server and Mysql)
 