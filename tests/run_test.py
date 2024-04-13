import pytest

def run_tests():
    # 这里可以指定任何命令行参数
    # 例如：['tests/', '-v', '--cov=my_package']
    pytest.main(['', '-v'])

if __name__ == "__main__":
    run_tests()
