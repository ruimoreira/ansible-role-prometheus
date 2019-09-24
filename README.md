Ansible-Role-Prometheus
=========

Role that aims to install prometheus on debian

https://kifarunix.com/install-and-configure-prometheus-on-debian-9/

Build Status
------------
[![Build Status](https://travis-ci.org/ruimoreira/ansible-role-prometheus.svg?branch=master)](https://travis-ci.org/ruimoreira/ansible-role-prometheus)

Requirements
------------

Ansible 2.7+

Role Variables
--------------

prometheus_user: user we want to run the service undert

prometheus_user_shell: prometheus user shell, it's /bin/false by default


Dependencies
------------

This role is not dependent of any other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-prometheus, x: 42 }

License
-------

BSD

Author Information
------------------

Name: Rui Moreira

Website: https://ruimoreira.co.uk

email: ruimoreira29@gmail.com
