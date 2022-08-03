version=2021
hub=docker.io
imageName=jeyrce/jeyrce:${version}
tag=${hub}/${imageName}
commitId=$(shell git rev-parse --short HEAD)

.phony: all
all: image index

.phony: image
image:
	docker build --build-arg commitId=${commitId} -t ${tag} .
	docker push ${tag}

.phony: index
index:
	docker run -it --rm --name jeyrce -d ${tag}
	docker cp jeyrce:/jeyrce/index.html .
	docker stop jeyrce
