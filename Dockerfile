FROM --platform=linux/amd64 python:3.8.12-slim AS builder
WORKDIR /jeyrce
COPY base.html jeyrce.yml make.py requirements.txt ./
RUN pip install -r requirements.txt \
    -i https://mirrors.aliyun.com/pypi/simple/  \
    --trusted-host mirrors.aliyun.com \
    --no-cache-dir && \
    python make.py

FROM --platform=linux/amd64 nginx:1.21.5-alpine AS runner
MAINTAINER jeyrce<jeyrce@gmail.com>
WORKDIR /jeyrce
COPY css/ css/
COPY font/ font/
COPY images/ images/
COPY js/ js/
COPY --from=builder /jeyrce/index.html .
COPY 404.html README.md ./
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf
