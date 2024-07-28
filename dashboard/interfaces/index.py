from typing import List, Literal, Tuple


class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def remove_observer(self, observer):
        self._observers.remove(observer)


class Observer:
    def update(self, observable: Observable):
        pass


class IData:
    def __init__(self, month, year, value):
        self.month = month
        self.year = year
        self.value = value


class IDataBaseManager(Observable):
    def __init__(self):
        super().__init__()

    def update(self, company_name):
        pass

    def get_current_name(self) -> str:
        return ""

    def get_current_symbol(self) -> str:
        return ""

    def get_all_company_names(self) -> list[str]:
        return []

    def is_banking(self) -> bool:
        return False

    def get_data(self, metrics, y_range, statement_key) -> list[IData]:
        return []


class IApp:
    pages = []
    databaseManager: IDataBaseManager

    def start_app(self):
        pass
