node {
    checkout scm

    docker.withRegistry('https://hub.docker.com/', 'dockerhub-ram') {

        def customImage = docker.build("rmap91:wog")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
