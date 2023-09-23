from Design_patterns.Observerpattern.Observable.StocksObservable import StocksObservable


class IphoneObservable(StocksObservable):
    observer_list = []
    stock_count = 0

    def add(self, observer):
        self.observer_list.append(observer)

    def remove(self, observor):
        self.observer_list.remove(observor)

    def notify_subscribers(self):
        for observer in self.observer_list:
            observer.update()

    def set_stock_count(self, new_stock_added):
        if self.stock_count == 0:
            self.notify_subscribers()

        self.stock_count += new_stock_added

    def get_stock_count(self):
        return self.stock_count

    def set_stock_count_to_zero(self):
        self.stock_count = 0
