node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-ram') {

        def customImage = docker.build("world_of_games:1.0")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
