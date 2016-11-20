class BaseBuilder(object):
    available_commands = []
    available_values = []

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self._check_attributes()

    def _check_attributes(self):
        if self.available_commands.__len__():
            for key, value in self.kwargs.items():
                if key not in self.available_commands:
                    raise AttributeError(
                        '`%s` attribute is invalid for %s. Available commands:'
                        ' %s' % (
                            key, self.__class__.__name__,
                            self.available_commands.__str__()
                        )
                    )

                if self.available_values.__len__():
                    if key in self.available_values and \
                            value not in self.available_values[key]:
                        raise AttributeError(
                            '`%s` value is invalid. Available values: %s' % (
                                value, self.available_values[key].__str__()
                            )
                        )


class BaseIniBuilder(BaseBuilder):
    def __init__(self, section, **kwargs):
        super(BaseIniBuilder, self).__init__(**kwargs)
        self.section = section

    def __str__(self):
        output = []
        if self.section is not None:
            output.append('[%s]' % self.section)
        for key, value in self.kwargs.items():
            output.append('%s = %s' % (key, value))
        return "\n".join(sorted(output)) + "\n"


class BaseYmlBuilder(BaseBuilder):
    def __str__(self):
        import yaml
        return yaml.dump(self.kwargs, default_flow_style=False)
