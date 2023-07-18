pipeline {
  agent {
    kubernetes {
        yaml """\
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        builder: promotion
    spec:
      serviceAccountName: jenkins-agent
      containers:
      - name: awscli
        image: amazon/aws-cli
        command:
        - cat
        tty: true
    """.stripIndent()
    }
  }
  stages {
    stage('Promote to Production') {
      steps {
          container(name: 'awscli') {
            script {
              buildNumber = Jenkins.instance.getItem(projectName).lastSuccessfulBuild.number
            }
            sh '''
            export AWS_DEFAULT_REGION=us-east-1
            imgNum=''' + buildNumber + '''
            APIMANIFEST=$(aws ecr batch-get-image --repository-name sre-course --image-ids imageTag=${imageAPIDevName}${imgNum} --query 'images[].imageManifest' --output text)
            DBMANIFEST=$(aws ecr batch-get-image --repository-name sre-course --image-ids imageTag=${imageDBDevName}${imgNum} --query 'images[].imageManifest' --output text)
            ACMANIFEST=$(aws ecr batch-get-image --repository-name sre-course --image-ids imageTag=${imageACDevName}${imgNum} --query 'images[].imageManifest' --output text)
            # Check API
            if [ $(aws ecr describe-images --repository-name sre-course | grep "${imageAPIProdName}${imgNum}" | wc -l) -eq 0 ]
            then
              # We don't have prod so tag Dev to prod
              if ! aws ecr put-image --repository-name sre-course --image-tag ${imageAPIProdName}${imgNum} --image-manifest "$APIMANIFEST"
              then
                exitvalue=1
              fi
            fi
            # Check DB
            if [ $(aws ecr describe-images --repository-name sre-course | grep "${imageDBProdName}${imgNum}" | wc -l) -eq 0 ]
            then
              # We don't have prod so tag Dev to prod
              if ! aws ecr put-image --repository-name sre-course --image-tag ${imageDBProdName}${imgNum} --image-manifest "$DBMANIFEST"
              then
                exitvalue="${exitvalue}2"
              fi
            fi
            # Check AutoClient
            if [ $(aws ecr describe-images --repository-name sre-course | grep "${imageACProdName}${imgNum}" | wc -l) -eq 0 ]
            then
              # We don't have prod so tag Dev to prod
              if ! aws ecr put-image --repository-name sre-course --image-tag ${imageACProdName}${imgNum} --image-manifest "$ACMANIFEST"
              then
                exitvalue=3
              fi
            fi

          case ${exitvalue} in
            0) echo "Update OK"
               ;;
            1) echo "API failed to push to repository"
               ;;
            2) echo "DB failed to push to repository"
               ;;
            3) echo "AC failed to push to repository"
               ;;
            12) echo "API and DB failed to push to repository"
               ;;
            13) echo "API and AC failed to push to repository"
               ;;
            23) echo "DB and AC failed to push to repository"
               ;;
            123) echo "All images failed to push to repository"
               ;;
          esac

          exit ${exitvalue}
'''
        }
      }
    }
  }
  environment {
    ECR_REPO = '108174090253.dkr.ecr.us-east-1.amazonaws.com/sre-course'
    imageAPIDevName='r000stevesapi-dev-'
    imageAPIProdName='r000stevesapi-prod-'
    imageDBDevName='r000stevesdb-dev-'
    imageDBProdName='r000stevesdb-prod-'
    imageACDevName='r000stevesac-dev-'
    imageACProdName='r000stevesac-prod-'
    projectName='r000steves'
  }
}