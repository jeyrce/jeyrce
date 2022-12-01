tag=latest
commitId=$(shell git rev-parse --short HEAD)

.phony: all
all: image

.phony: image
image:
	docker buildx build -t jeyrce/jeyrce:${tag} -t jeyrce/jeyrce:latest \
		--platform=linux/amd64,linux/arm64/v8,linux/386 \
		--build-arg commitId=${commitId} \
		--pull \
		--push \
		.

.phony: index
index:
	docker run --rm --name jeyrce -d jeyrce/jeyrce:latest
	docker cp jeyrce:/jeyrce/index.html .
	docker stop jeyrce
