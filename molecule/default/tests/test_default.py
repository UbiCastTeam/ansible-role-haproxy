import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_haproxy_pkg(host):
    if host.system_info.distribution == "debian":
        p = host.package("haproxy")
    elif host.system_info.distribution == "centos":
        p = host.package("rh-haproxy18")

    assert p.is_installed


def test_haproxy_service(host):
    if host.system_info.distribution == "debian":
        s = host.service("haproxy")
    elif host.system_info.distribution == "centos":
        s = host.service("rh-haproxy18-haproxy")

    assert s.is_running


def test_haproxy_socket(host):
    s = host.socket("tcp://80")

    assert s.is_listening
