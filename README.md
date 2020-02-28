Ansible role for golang-toolchain
=================================

Installs the golang toolchain.

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/actions?query=workflow%3A%22Release%22)

Explanation
-----------
This role will pass the value of `golang_toolchain_sha` to its dependent role: `ansible-role-toolchain`.

    golang_toolchain_sha: c2b22e6b09e856aed18bcfddbdccb3aa70c70ece

The ansible-role-toolchain will first check if the host has an existing golang toolchain installed at `/opt/golang`.

If so, `ansible-role-toolchain` will then check if there is a `toolchain_version` file present in `/opt/golang/toolchain_version`.

If the version file is present, it will then compare versions to see if we need to download a new toolchain. If the versions match, then no further work is required.

If the versions are different, `ansible-role-toolchain` will then proceed to download the specified toolchain version from AWS and place the tarball into the `/tmp` directory.

From here, the `ansible-role-golang-toolchain` will then delete the old toolchain and then move the newly downloaded toolchain to the correct directory, `/opt/golang`.

Finally, this role will then create a `toolchain_version` file with your specified `golang_toolchain_sha` and place it in `/opt/golang/toolchain_version` for use in future runs.

Requirements
------------

`ansible-role-toolchain` must be up to date in your `requirements.yml`

    ---
    - src: git+https://github.com/mongodb-ansible-roles/ansible-role-toolchain.git
      version: v1.1.0

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `golang_toolchain_sha` | SHA of the golang toolchain you want to download | string | `""` | yes |
| `golang_toolchain_final_dest` | Final destination of the golang toolchain | string | `/opt/golang` | yes |
| `golang_toolchain_url` | You may specify a custom URL to download the golang toolchain from | string | `""` | no |

Dependencies
------------

- [`mongodb-ansible-roles.ansible-role-toolchain`](https://github.com/mongodb-ansible-roles/ansible-role-toolchain)

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-toolchain-golang
      vars:
        golang_toolchain_sha: "001ac697f8f64d5d89625373a0ffa6aae13270a8"
```

Testing
-------

Testing for this role in GitHub Actions and/or locally requires you to set up secrets and/or environment variables respectively.

The required variables you need to set up are:
1. `REDHAT_REGISTRY_SERVICE_ACCOUNT_USERNAME`
2. `REDHAT_REGISTRY_SERVICE_ACCOUNT_PASSWORD`
3. `RHEL80_ZSERIES_DEV`
4. `PRIVATE_KEY`

`RHEL80_ZSERIES_DEV` is formatted as username@host for the rhel80-zseries box
`PRIVATE_KEY` is a private key that has access to the hosts

License
-------

[Apache License](LICENSE)

