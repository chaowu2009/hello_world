node {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      deleteDir()
      sh "cp -rf /opt/hello_world hello_world"
      if (!fileExists("hello_world/Dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Unit Test') {
      // run the unit tests
      dir("hello_world") {
         sh ". .env/bin/activate"
         sh "pip install -r requirements.txt"
         sh "python -m pytest tests/test_app.py"
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
       dir("hello_world") {
         sh "docker build -t helloworldapp-${BUILD_ID} ."
       }
   }
}
