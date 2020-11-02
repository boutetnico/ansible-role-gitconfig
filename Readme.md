ansible-role-git-config
=======================

This role configures git.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                | Required | Default              | Choices | Comments                                  |
|-------------------------|----------|----------------------|---------|-------------------------------------------|
| git_config_settings     | yes      | `[]`                 | list    | Settings to set. See `defaults/main.yml`. |

Dependencies
------------

- `git` should be installed.

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-git-config
          git_config_settings:
            - name: alias.ci
              scope: global
              value: commit
            - name: alias.remotev
              value: remote -v
            - name: user.email
              repo: /role_test
              scope: local
              value: root@root
Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
