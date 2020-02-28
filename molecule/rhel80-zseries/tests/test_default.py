import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_golang_toolchain(host):
    assert host.file("/tmp/golang_test").exists
    assert host.file("/tmp/golang_test/toolchain_version").exists
    assert host.file("/tmp/golang_test/toolchain_version").contains("testing_golang_sha")

    cmd = host.run("GOROOT=/tmp/golang_test/go1.7 /tmp/golang_test/go1.7/bin/go version")
    assert cmd.stdout == """go version go1.7.6 linux/amd64
"""

    cmd = host.run("GOROOT=/tmp/golang_test/go1.8 /tmp/golang_test/go1.8/bin/go version")
    assert cmd.stdout == """go version go1.8.7 linux/amd64
"""

    cmd = host.run("GOROOT=/tmp/golang_test/go1.9 /tmp/golang_test/go1.9/bin/go version")
    assert cmd.stdout == """go version go1.9.7 linux/amd64
"""

    cmd = host.run("GOROOT=/tmp/golang_test/go1.10 /tmp/golang_test/go1.10/bin/go version")
    assert cmd.stdout == """go version go1.10.8 linux/amd64
"""

    cmd = host.run("GOROOT=/tmp/golang_test/go1.11 /tmp/golang_test/go1.11/bin/go version")
    assert cmd.stdout == """go version go1.11.9 linux/amd64
"""

    cmd = host.run("GOROOT=/tmp/golang_test/go1.12 /tmp/golang_test/go1.12/bin/go version")
    assert cmd.stdout == """go version go1.12.8 linux/amd64
"""
