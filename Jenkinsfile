pipeline{
 agent any
  stages{
    stage('test stage'){
      steps{
        script{
          currentBuild.description = "${env.CHANGE_ID}"
          echo 'test'
        }
      }
    }
  }
}
