from pywinauto.application import Application

app = Application(backend="uia").connect(title='NCALayer')
NCALayer_window = app.top_window()

textboxes = NCALayer_window.descendants(control_type="Edit")
textboxes[1].type_keys("Aa1234")
NCALayer_window.child_window(title="Открыть", control_type="Button").click()

app = Application(backend="uia").connect(title='NCALayer', timeout=10)
NCALayer_window = app.top_window()
NCALayer_window.type_keys("{ENTER}")
NCALayer_window.child_window(title="Подписать", control_type="Button").click()