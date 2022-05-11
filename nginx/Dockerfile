FROM jwilder/nginx-proxy:0.9

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY vhost.d/default /etc/nginx/vhost.d/default