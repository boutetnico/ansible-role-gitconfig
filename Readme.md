[![tests](https://github.com/boutetnico/ansible-role-gitconfig/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-gitconfig/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.gitconfig-blue.svg)](https://galaxy.ansible.com/boutetnico/gitconfig)

ansible-role-gitconfig
======================

This role configures git.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

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
        - ansible-role-gitconfig
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
