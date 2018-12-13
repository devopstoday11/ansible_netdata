import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sources_directories(host):
    d = host.file("/opt/netdata")
    assert d.exists
    assert d.is_directory
    assert d.user == 'root'
    assert d.group == 'root'


def test_conf_directories(host):
    d = host.file("/etc/netdata")
    assert d.exists
    assert d.is_directory
    assert d.user == 'root'
    assert d.group == 'netdata'


def test_config_file(host):
    f = host.file("/etc/netdata/netdata.conf")
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'netdata'


def test_service(host):
    s = host.service('netdata')
    assert s.is_enabled
    assert s.is_running


def test_sockets_open(host):
    s = host.socket("tcp://127.0.0.1:19999")
    assert s.is_listening
