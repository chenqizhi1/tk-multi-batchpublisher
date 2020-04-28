from sgtk.platform import Application

class BacthPublisherApp(Application):
    def init_app(self):
        app_payload = self.import_module("app")
        menu_callback = lambda: app_payload.batchpublisher.show_dialog(self)
        self.engine.register_command("Batch Publisher...", menu_callback)