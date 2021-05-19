from mycroft import MycroftSkill, intent_file_handler


class Prepararrefeicoes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prepararrefeicoes.intent')
    def handle_prepararrefeicoes(self, message):
        self.speak_dialog('prepararrefeicoes')


def create_skill():
    return Prepararrefeicoes()

