import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_service_running_and_enabled(Service):
    assert Service('redis').is_running
    assert Service('redis').is_enabled


def test_redis_config(File):
    assert File('/etc/redis.conf').contains('bind 0.0.0.0')
