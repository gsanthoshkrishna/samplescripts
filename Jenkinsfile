pipeline{
 agent any
  stages{
    stage('test stage'){
      steps{
        script{
         currentBuild.displayName = "build-${env.BUILD_NUMBER}"
         currentBuild.description = "description-l--${env.CHANGE_ID}"
         echo "From sub branch"
          echo "CHANGEID ${env.CHANGE_ID}"
         echo "build-id ${env.BUILD_ID}"
        }
      }
    }
  }
}
