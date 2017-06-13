import pytest
import sys

# global property
@pytest.fixture(scope="session")
def log_global_env_facts(f):
    print("log_global_env_facts")
    print(f)
    if pytest.config.pluginmanager.hasplugin('junitxml'):
        my_junit = getattr(pytest.config, '_xml', None)
        my_junit.add_global_property('ARCH', 'PPC-CPP')
        my_junit.add_global_property('STORAGE_TYPE', 'CEPH')

@pytest.mark.usefixtures(log_global_env_facts)
def start_and_prepare_env():
    print("start_and_prepare_env")
    pass
    # assert False

class TestMe:
    def test_foo(self):
        assert True
# ------------------------------------------------

# record_xml_property
# property under TestCase
def test_function(record_xml_property):
    print("test_function")
    record_xml_property("example_key", 1)
    assert 0
# -------------------------------------------

# raise exception
def test_zero_division():
    print('test_zero_division')
    with pytest.raises(ZeroDivisionError):
        1/0
# --------------------------------------------------

# The capsys and capfd fixtures
def test_myoutput(capsys): # or use "capfd" for fd-level
    print ("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print ("next")
    out, err = capsys.readouterr()
    assert out == "next\n"
# ----------------------------------------

@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    print ("callattr_ahead_of_alltests called")
    seen = set([None])
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()
            seen.add(cls)