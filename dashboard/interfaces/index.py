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


class IDatabaseManager(Observable):
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

    def get_datas(self, key, year_range, statement_key, to_million=True) -> list[IData]:
        return []

    def get_data(self, key, statement_key, to_million=True) -> IData:
        return IData(0, 0, 0)


class IApp:
    pages = []
    databaseManager: IDatabaseManager

    def start_app(self):
        pass


class IAssetStuctureGraph:
    def __init__(self, observable: IDatabaseManager, height):
        self.equity: IData = IData(0, 0, 0)
        self.liabilities: IData = IData(0, 0, 0)
        self.short_debt: IData = IData(0, 0, 0)
        self.long_debt: IData = IData(0, 0, 0)

    def update(self, observable: IDatabaseManager):
        pass

    def setBehavior(self, behavior):
        pass

    def init_graph(self):
        pass
