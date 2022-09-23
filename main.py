
from datetime import datetime

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.CopyToClipboardAction import \
    CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import \
    RenderResultListAction
from ulauncher.api.shared.event import ItemEnterEvent, KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from src.calc import handle_calc


class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        time = event.get_argument() or ''

        item = ExtensionResultItem(
            icon='images/icon.png',
            name='Usage: [s=08:00] or [s=08:00 e=08:30] or [30]',
            on_enter=HideWindowAction()
        )

        if time:
            result = handle_calc(time, datetime.now())

            item = ExtensionResultItem(
                icon='images/icon.png',
                name=str(result),
                on_enter=CopyToClipboardAction(str(result))
            )

        return RenderResultListAction([item])


if __name__ == '__main__':
    DemoExtension().run()
