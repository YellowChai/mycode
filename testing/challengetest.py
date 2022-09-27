import challenge
import pytest
import os

def test():

    with pytest.raises(Exception) as slappysquirrel:

        os.path.isfile('/home/student/mycode/testing/testing.txt')


    assert "Network access not allowed" in str(slappysquirrel.value)


