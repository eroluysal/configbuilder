from configbuilder.builder.base import BaseIniBuilder


class ToxBuilder(BaseIniBuilder):
    available_commands = (
        'setenv',
        'passenv',
        'recreate',
        'downloadcache',
        'sitepackages',
        'args_are_paths',
        'deps',
        'envlist',
        'pip_pre',
        'platform',
        'commands',
        'changedir',
        'basepython',
        'ignore_errors',
        'install_command',
        'whitelist_externals',
        'skip_missing_interpreters',
        'list_dependencies_command',
        'envtmpdir',
        'envlogdir',
        'indexserver',
        'envdir',
        'usedevelop',
        'skip_install',
        'ignore_outcome',
        'extras',
    )
