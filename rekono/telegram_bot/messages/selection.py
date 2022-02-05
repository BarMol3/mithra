from telegram.utils.helpers import escape_markdown
from telegram_bot.models import TelegramChat

ASK_FOR_PROJECT = 'Choose a Rekono project'
SELECTED_PROJECT = 'Project {project} has been selected'
NO_PROJECTS = 'You have no projects. Go to Rekono to create one or ask your administrator for assign you to existing one'


SELECTION = '''
*SELECTED ITEMS*

💼 _Project_   *{project}*
🎯 _Target_    *{target}*
'''

def create_selection_message(chat: TelegramChat) -> str:
    return SELECTION.format(
        project=escape_markdown(chat.project.name if chat.project else '', version=2),
        target=escape_markdown(chat.target.target if chat.target else '', version=2)
    )
