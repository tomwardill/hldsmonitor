from SourceLib import SourceQuery

class Hldsmonitor:
    def __init__(self, agentConfig, mainLogger, rawConfig):
        self.agentConfig = agentConfig
        self.mainLogger = mainLogger
        self.rawConfig = rawConfig

    def run(self):
        data = {}

        server = SourceQuery.SourceQuery(self.rawConfig['Hldsmonitor']['server'], int(self.rawConfig['Hldsmonitor']['port']))
        info = server.info()
        data = {}
        data['ping'] = info['ping']
        data['numplayers'] = info['numplayers']
        data['maxplayers'] = info['maxplayers']
        data['secure'] = info['secure']
        return data
