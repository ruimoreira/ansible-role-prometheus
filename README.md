Role Name
=========

Role that aims to install prometheus on debian

https://kifarunix.com/install-and-configure-prometheus-on-debian-9/

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

prometheus_user: user we want to run the service undert

prometheus_user_shell: prometheus user shell, it's /bin/false by default


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

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
