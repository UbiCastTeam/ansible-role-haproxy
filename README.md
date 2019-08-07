HAproxy
=======

Install HAProxy.

Requirements
------------

None.

Role Variables
--------------

See `./defaults/main.yml` for defaults and examples values.

You may end up using these variables:
- Action to perform when role is invoked: `haproxy_action`
- List of global settings: `haproxy_globals`
- List of defaults settings for backends: `haproxy_defaults`
- List of listens and their settings: `haproxy_listens`
- List of backends and their settings: `haproxy_backends`
- List of frontends and their settings: `haproxy_frontends`

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- hosts: servers
  vars:
    haproxy_frontends:
      - name: https-in
        settings:
          - bind 0.0.0.0:443 ssl crt /path/to/bundle/crt alpn h2,http/1.1
          - bind :::443 ssl crt /path/to/bundle/crt alpn h2,http/1.1
          -
          - option forwardfor
          - http-request add-header X-Forwarded-Proto https
          -
          - acl host_one hdr(host) -i one.example.net
          - acl host_two hdr(host) -i two.example.net
          -
          - use_backend one if host_one
          - use_backend two if host_two
          -
          - default_backend default
      - name: http-in
        settings:
          - bind 0.0.0.0:80
          - bind :::80
          -
          - acl host_letsencrypt path_beg /.well-known/acme-challenge/
          -
          - use_backend letsencrypt if host_letsencrypt
          -
          - redirect scheme https code 301 if !host_letsencrypt
    haproxy_backends:
      - name: one
        settings:
          - server one 192.168.0.1:80
      - name: two
        settings:
          - server two 192.168.0.2:80
      - name: default
        settings:
          - server default 192.168.0.3:80
      - name: letsencrypt
        settings:
          - server letsencrypt 192.168.0.4:8080
  roles:
    - ansible-role-haproxy
...
```
