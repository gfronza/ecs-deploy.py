import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '-xrs',
            '--cov', 'ecs-deploy.py',
            '--cov-report', 'term-missing',
            '--pep8',
            '--cache-clear'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


# class PyTest(TestCommand):
#     test_package_name = 'ecs-deploy.py'
#
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         _test_args = [
#             '--verbose',
#             '--ignore=build',
#             '--cov={0}'.format(self.test_package_name),
#             '--cov-report=term-missing',
#             '--pep8',
#         ]
#         extra_args = os.environ.get('PYTEST_EXTRA_ARGS')
#         if extra_args is not None:
#             _test_args.extend(extra_args.split())
#         self.test_args = _test_args
#         self.test_suite = True
#
#     def run_tests(self):
#         import pytest
#         from pkg_resources import normalize_path, _namespace_packages
#
#         # Purge modules under test from sys.modules. The test loader will
#         # re-import them from the build location. Required when 2to3 is used
#         # with namespace packages.
#         if sys.version_info >= (3,) and getattr(self.distribution,
#                                                 'use_2to3', False):
#             # module = self.test_args[-1].split('.')[0]
#             module = self.test_package_name
#             if module in _namespace_packages:
#                 del_modules = []
#                 if module in sys.modules:
#                     del_modules.append(module)
#                 module += '.'
#                 for name in sys.modules:
#                     if name.startswith(module):
#                         del_modules.append(name)
#                 map(sys.modules.__delitem__, del_modules)
#
#             # Run on the build directory for 2to3-built code
#             # This will prevent the old 2.x code from being found
#             # by py.test discovery mechanism, that apparently
#             # ignores sys.path..
#             ei_cmd = self.get_finalized_command("egg_info")
#
#             # Replace the module name with normalized path
#             # self.test_args[-1] = normalize_path(ei_cmd.egg_base)
#             self.test_args.append(normalize_path(ei_cmd.egg_base))
#
#         errno = pytest.main(self.test_args)
#         sys.exit(errno)


tests_require = [
    'pytest-pep8',
    'pytest-cov',
    get_requirements('-dev')
]

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='ecs-deploy',
    version='0.1.0',
    url='http://github.com/cuttlesoft/flask-bitmapist',
    download_url='https://github.com/cuttlesoft/flask-bitmapist/tarball/0.1.0',
    license='MIT',
    author='Cuttlesoft, LLC',
    author_email='engineering@cuttlesoft.com',
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
